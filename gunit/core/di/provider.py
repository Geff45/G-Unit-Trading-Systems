from __future__ import annotations

import inspect
from typing import Any, get_type_hints

from .descriptor import ServiceDescriptor
from .exceptions import ServiceResolutionError
from .lifetime import ServiceLifetime


class ServiceProvider:
    """
    Root dependency-injection provider.

    Owns singleton instances and creates isolated service scopes.
    """

    def __init__(
        self,
        descriptors: dict[type, ServiceDescriptor],
    ) -> None:
        self._descriptors = dict(descriptors)
        self._instances: dict[type, Any] = {}
        self._disposed = False

    @property
    def is_disposed(self) -> bool:
        """
        Return whether the provider has been disposed.
        """
        return self._disposed

    def dispose(self) -> None:
        """
        Dispose the provider and clean up owned singleton instances.

        Disposal is idempotent.

        Only singleton instances owned by this provider are disposed.
        Transient instances are not tracked and scoped instances belong
        to their respective scopes.
        """

        if self._disposed:
            return

        self._disposed = True

        instances = list(self._instances.values())

        for instance in reversed(instances):
            self._cleanup_instance(instance)

        self._instances.clear()

    @staticmethod
    def _cleanup_instance(instance: Any) -> None:
        """
        Clean up an instance using standard Python lifecycle protocols.

        Context-manager cleanup takes precedence over close(), which
        takes precedence over dispose().
        """

        if hasattr(instance, "__exit__"):
            instance.__exit__(None, None, None)
            return

        if hasattr(instance, "close"):
            instance.close()
            return

        if hasattr(instance, "dispose"):
            instance.dispose()

    def get(self, service_type: type) -> Any:
        """
        Resolve a service from the root provider.

        Scoped services resolved directly from the root provider use
        the root provider as their scope.
        """

        if self._disposed:
            raise ServiceResolutionError(
                "Service provider has been disposed"
            )

        return self._resolve(
            service_type,
            resolving=set(),
            scoped_instances=self._instances,
        )

    def create_scope(self) -> ServiceScope:
        """
        Create an isolated service scope.
        """

        if self._disposed:
            raise ServiceResolutionError(
                "Service provider has been disposed"
            )

        return ServiceScope(self)

    def _resolve(
        self,
        service_type: type,
        resolving: set[type],
        scoped_instances: dict[type, Any],
    ) -> Any:
        """
        Resolve a service according to its registered lifetime.
        """

        if self._disposed:
            raise ServiceResolutionError(
                "Service provider has been disposed"
            )

        if service_type not in self._descriptors:
            raise ServiceResolutionError(
                f"Service not registered: {service_type}"
            )

        if service_type in resolving:
            raise ServiceResolutionError(
                f"Circular dependency detected: {service_type}"
            )

        descriptor = self._descriptors[service_type]

        if descriptor.lifetime == ServiceLifetime.SINGLETON:
            if service_type in self._instances:
                return self._instances[service_type]

        elif descriptor.lifetime == ServiceLifetime.SCOPED:
            if service_type in scoped_instances:
                return scoped_instances[service_type]

        resolving = set(resolving)
        resolving.add(service_type)

        implementation = descriptor.implementation_type

        try:
            if inspect.isclass(implementation):
                instance = self._construct_class(
                    service_type,
                    implementation,
                    resolving,
                    scoped_instances,
                )
            else:
                instance = self._invoke_factory(
                    service_type,
                    implementation,
                    resolving,
                    scoped_instances,
                )

        except ServiceResolutionError:
            raise

        except Exception as exc:
            raise ServiceResolutionError(
                f"Failed to resolve service {service_type}: {exc}"
            ) from exc

        if descriptor.lifetime == ServiceLifetime.SINGLETON:
            self._instances[service_type] = instance

        elif descriptor.lifetime == ServiceLifetime.SCOPED:
            scoped_instances[service_type] = instance

        return instance

    def _construct_class(
        self,
        service_type: type,
        implementation: type,
        resolving: set[type],
        scoped_instances: dict[type, Any],
    ) -> Any:
        """
        Construct a class and resolve constructor dependencies.
        """

        signature = inspect.signature(implementation.__init__)

        type_hints = get_type_hints(implementation.__init__)

        dependencies: dict[str, Any] = {}

        for parameter in signature.parameters.values():

            if parameter.name == "self":
                continue

            if parameter.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):
                continue

            dependency_type = type_hints.get(parameter.name)

            if dependency_type is None:

                if parameter.default is not inspect.Parameter.empty:
                    continue

                raise ServiceResolutionError(
                    f"Cannot resolve constructor dependency "
                    f"'{parameter.name}' for {service_type}"
                )

            dependencies[parameter.name] = self._resolve(
                dependency_type,
                resolving,
                scoped_instances,
            )

        return implementation(**dependencies)

    def _invoke_factory(
        self,
        service_type: type,
        factory: Any,
        resolving: set[type],
        scoped_instances: dict[type, Any],
    ) -> Any:
        """
        Invoke a registered factory and resolve its dependencies.
        """

        signature = inspect.signature(factory)

        type_hints = get_type_hints(factory)

        dependencies: dict[str, Any] = {}

        for parameter in signature.parameters.values():

            if parameter.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):
                continue

            dependency_type = type_hints.get(parameter.name)

            if dependency_type is None:

                if parameter.default is not inspect.Parameter.empty:
                    continue

                raise ServiceResolutionError(
                    f"Cannot resolve factory dependency "
                    f"'{parameter.name}' for {service_type}"
                )

            dependencies[parameter.name] = self._resolve(
                dependency_type,
                resolving,
                scoped_instances,
            )

        return factory(**dependencies)


class ServiceScope:
    """
    Isolated dependency-injection scope.

    Singleton instances remain owned by the root provider while
    scoped instances belong exclusively to this scope.
    """

    def __init__(
        self,
        provider: ServiceProvider,
    ) -> None:
        self._provider = provider
        self._instances: dict[type, Any] = {}
        self._disposed = False

    @property
    def is_disposed(self) -> bool:
        """
        Return whether the scope has been disposed.
        """
        return self._disposed

    def get(self, service_type: type) -> Any:
        """
        Resolve a service within this scope.
        """

        if self._disposed:
            raise ServiceResolutionError(
                "Service scope has been disposed"
            )

        return self._provider._resolve(
            service_type,
            resolving=set(),
            scoped_instances=self._instances,
        )

    def dispose(self) -> None:
        """
        Dispose the scope and clean up its scoped instances.

        Instances are cleaned in reverse resolution order.
        """

        if self._disposed:
            return

        self._disposed = True

        instances = list(self._instances.values())

        for instance in reversed(instances):
            ServiceProvider._cleanup_instance(instance)

        self._instances.clear()

    def __enter__(self) -> ServiceScope:
        if self._disposed:
            raise ServiceResolutionError(
                "Service scope has been disposed"
            )

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        self.dispose()
