"""
G-UNIT Platform Kernel

Lifecycle Manager

Controls service startup and shutdown.
"""


from typing import Dict, Any

from .states import ServiceState



class LifecycleManager:
    """
    Manages service lifecycle.
    """



    def __init__(self):

        self.states: Dict[str, ServiceState] = {}



    def register(
        self,
        service_name: str
    ):

        self.states[
            service_name
        ] = ServiceState.CREATED



    def initialize(
        self,
        service_name: str,
        service
    ):

        try:

            if hasattr(
                service,
                "initialize"
            ):

                service.initialize()


            self.states[
                service_name
            ] = ServiceState.INITIALIZED


        except Exception:

            self.states[
                service_name
            ] = ServiceState.FAILED

            raise



    def start(
        self,
        service_name: str,
        service
    ):

        try:

            self.states[
                service_name
            ] = ServiceState.STARTING



            if hasattr(
                service,
                "start"
            ):

                service.start()



            self.states[
                service_name
            ] = ServiceState.RUNNING



        except Exception:

            self.states[
                service_name
            ] = ServiceState.FAILED

            raise



    def stop(
        self,
        service_name: str,
        service
    ):

        try:

            self.states[
                service_name
            ] = ServiceState.STOPPING



            if hasattr(
                service,
                "stop"
            ):

                service.stop()



            self.states[
                service_name
            ] = ServiceState.STOPPED



        except Exception:

            self.states[
                service_name
            ] = ServiceState.FAILED

            raise



    def status(
        self,
        service_name: str
    ):

        return self.states.get(
            service_name
        )