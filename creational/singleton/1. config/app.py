from config_manager import ConfigManager

manager = ConfigManager()
manager.set("name", "duy")
other = ConfigManager()
print(other.get("name"))