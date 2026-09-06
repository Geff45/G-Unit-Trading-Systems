from gunit.core.contracts.service_contract import ServiceContract
from gunit.core.interfaces.service import IService


class DemoService(ServiceContract):
    @property
    def service_id(self):
        return "demo.service"

    @property
    def service_name(self):
        return "Demo Service"

    @property
    def version(self):
        return "1.0.0"

    def initialize(self):
        self.initialized = True

    def configure(self):
        self.configured = True

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True

    def shutdown(self):
        self.shutdown_called = True


class DemoInterfaceService(IService):
    @property
    def id(self):
        return "demo.interface"

    @property
    def name(self):
        return "Demo Interface"

    @property
    def version(self):
        return "1.0.0"

    def initialize(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def shutdown(self):
        pass


def test_service_contract_is_abstract():
    assert ServiceContract.__abstractmethods__


def test_service_contract_requires_identity():
    required = {
        "service_id",
        "service_name",
        "version",
    }

    assert required.issubset(
        ServiceContract.__abstractmethods__
    )


def test_service_contract_requires_full_lifecycle():
    required = {
        "initialize",
        "configure",
        "start",
        "stop",
        "shutdown",
    }

    assert required.issubset(
        ServiceContract.__abstractmethods__
    )


def test_concrete_service_can_implement_contract():
    service = DemoService()

    assert isinstance(service, ServiceContract)
    assert service.service_id == "demo.service"
    assert service.service_name == "Demo Service"
    assert service.version == "1.0.0"


def test_service_contract_lifecycle():
    service = DemoService()

    service.initialize()
    service.configure()
    service.start()
    service.stop()
    service.shutdown()

    assert service.initialized
    assert service.configured
    assert service.started
    assert service.stopped
    assert service.shutdown_called


def test_iservice_is_abstract():
    assert IService.__abstractmethods__


def test_iservice_requires_identity_and_lifecycle():
    required = {
        "id",
        "name",
        "version",
        "initialize",
        "start",
        "stop",
        "shutdown",
    }

    assert required.issubset(
        IService.__abstractmethods__
    )


def test_iservice_concrete_implementation():
    service = DemoInterfaceService()

    assert isinstance(service, IService)
    assert service.id == "demo.interface"
    assert service.name == "Demo Interface"
    assert service.version == "1.0.0"

def test_contract_package_exports_service_contract():
    from gunit.core import contracts

    assert contracts.ServiceContract is ServiceContract


def test_interface_package_exports_iservice():
    from gunit.core import interfaces

    assert interfaces.IService is IService

def test_legacy_service_remains_available():
    from gunit.core.services import Service

    assert Service.__abstractmethods__


def test_contracts_remain_distinct_from_legacy_service():
    from gunit.core.services import Service

    assert Service is not ServiceContract
    assert Service is not IService
