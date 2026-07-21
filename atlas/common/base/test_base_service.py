from common.base.base_service import BaseService


class DemoService(BaseService):

    def __init__(self):
        super().__init__("Demo Service")


service = DemoService()

service.initialize()

service.configure({"mode": "development"})

service.start()

print(service.health())

print(service.metrics())

print(service.information())

service.stop()

print(service.health())