import sys

from caddo_tool.settings.settings import Settings


class ModuleLoader:
    def load_model_initializer(self):
        module = self.load_module(Settings.model_initializer_module_path)
        print("Data Loader loaded!")
        return module

    def load_data_preprocessor(self):
        module = self.load_module(Settings.data_preprocessor_module_path)
        print("Data Preprocessor loaded!")
        return module

    def load_model_trainer(self):
        module = self.load_module(Settings.model_trainer_module_path)
        print("Net Trainer loaded!")
        return module

    def load_model_tester(self):
        module = self.load_module(Settings.model_tester_module_path)
        print("Net Tester loaded!")
        return module

    def load_model_evaluator(self):
        module = self.load_module(Settings.model_evaluator_module_path)
        print("Net Evaluator loaded!")
        return module

    def load_module(self, path_to_module):
        __import__(path_to_module)
        return sys.modules[path_to_module]
