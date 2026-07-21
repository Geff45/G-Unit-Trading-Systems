from core.base.component import BaseComponent
from core.base.engine import BaseEngine
from core.base.manager import BaseManager
from core.base.worker import BaseWorker
from core.base.model import BaseModel

component = BaseComponent("Atlas")
print(component.start())

engine = BaseEngine("Trading Engine")
print(engine.execute("Liquidity Scan"))

manager = BaseManager("Worker Manager")
manager.register("worker1", "AI Worker")
print(manager.list())

worker = BaseWorker("Worker-001")
print(worker.assign("Analyze EURUSD"))

model = BaseModel("AtlasGPT", "1.0")
print(model.info())