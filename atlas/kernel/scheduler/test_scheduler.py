from kernel.scheduler.scheduler import AtlasScheduler


scheduler = AtlasScheduler()


def heartbeat():

    print("Heartbeat OK")


def market_update():

    print("Market Update")


scheduler.add_task(

    "heartbeat",

    1,

    heartbeat,

)

scheduler.add_task(

    "market",

    1,

    market_update,

)

scheduler.run_once()