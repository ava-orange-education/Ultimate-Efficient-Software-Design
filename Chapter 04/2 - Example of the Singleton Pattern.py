class SettingsManager:
  _instance = None  # Private variable to hold the single instance

  def __new__(cls):
    if not cls._instance:
      cls._instance = super(SettingsManager, cls).__new__(cls)
    return cls._instance

  def load_settings(self):
    # Load settings logic
    pass

  @staticmethod
  def get_instance():
    return SettingsManager._instance

# Accessing the SettingsManager from anywhere in your code
settings = SettingsManager.get_instance()
settings.load_settings()
