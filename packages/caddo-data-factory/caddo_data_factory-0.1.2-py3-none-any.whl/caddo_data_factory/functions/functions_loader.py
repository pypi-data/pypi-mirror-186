import sys
from caddo_file_parser.settings.generation_settings import GenerationSettings



class FunctionsLoader:
    def extract_features_keywords(self, settings: GenerationSettings):
        module = self.load_module(settings.data_extraction_function_path)
        print("Data Loader loaded!")
        return module

    def load_module(self, path_to_module):
        __import__(path_to_module)
        return sys.modules[path_to_module]
