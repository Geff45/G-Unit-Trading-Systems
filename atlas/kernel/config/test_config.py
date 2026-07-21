from kernel.config.config_manager import ConfigurationManager

manager = ConfigurationManager()

manager.load("atlas.yaml")

print(manager.value("atlas.yaml", "system", "name"))

print(manager.value("atlas.yaml", "runtime", "heartbeat_ms"))

print(manager.value("atlas.yaml", "trading", "mode"))