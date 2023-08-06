import yaml
from yaml import SafeLoader
from caddo_file_parser.settings.generation_settings import GenerationSettings
from caddo_file_parser.settings.generation_settings_loader import GenerationSettingsLoader

class SettingsReader:
    def __init__(self, settings_path=''):
        self.settings_path = settings_path

    def load(self):
        print("LOADING SETTINGS")
        return self.load_settings()

    def read_settings_file(self):
        with open(self.settings_path) as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data

    def load_settings(self):
        settings_file = self.read_settings_file()
        loader = GenerationSettingsLoader()
        print(settings_file)
        settings: GenerationSettings = loader.load_settings_object(settings_file)
        return settings
