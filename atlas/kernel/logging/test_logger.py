from kernel.logging.logger import AtlasLogger

logger = AtlasLogger()

logger.info("Runtime", "Atlas started")
logger.warning("Market", "Spread increasing")
logger.error("Broker", "Connection lost")

for entry in logger.entries():

    print(
        f"[{entry.level.value}] "
        f"{entry.source}: "
        f"{entry.message}"
    )