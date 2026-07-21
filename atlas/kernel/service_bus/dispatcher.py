from kernel.service_bus.router import Router
from kernel.service_bus.envelope import Envelope


class Dispatcher:
    """
    Atlas Enterprise Dispatcher

    Responsible for delivering
    messages to the Router.
    """

    def __init__(self, router: Router):

        self.router = router

    def dispatch(
        self,
        envelope: Envelope,
    ):

        self.router.dispatch(
            envelope
        )