from event import Event
from subscriber import Subscriber
from dispatcher import Dispatcher


dispatcher = Dispatcher()

risk = Subscriber("Risk Engine")

ai = Subscriber("AI Engine")

dashboard = Subscriber("Dashboard")


dispatcher.register(risk)

dispatcher.register(ai)

dispatcher.register(dashboard)


event = Event(

    "MarketOpened",

    {
        "symbol": "EURUSD",
        "price": 1.1750
    }

)

print(dispatcher.dispatch(event))

print(dispatcher.queue.size())

print(dispatcher.logger.history())