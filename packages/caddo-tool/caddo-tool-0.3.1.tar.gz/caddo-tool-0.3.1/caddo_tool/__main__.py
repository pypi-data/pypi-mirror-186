from caddo_tool.modules.attributes import Attributes
from caddo_tool.modules.module_loader import ModuleLoader
from caddo_tool.settings.settings_loader import SettingsLoader

from caddo_tool.utils.data_loader import DataLoader


class Caddo:
    def __init__(self):
        SettingsLoader('./settings.yaml').load()
        self.date_loader = DataLoader()
        self.model_initializer_module = None
        self.data_preprocessor_module = None
        self.model_trainer_module = None
        self.model_tester_module = None
        self.model_evaluator_module = None
        self.load_modules()
        self.run()

    def load_modules(self):
        print("LOADING MODULES:")
        module_loader = ModuleLoader()
        self.model_initializer_module = module_loader.load_model_initializer()
        self.data_preprocessor_module = module_loader.load_data_preprocessor()
        self.model_trainer_module = module_loader.load_model_trainer()
        self.model_tester_module = module_loader.load_model_tester()
        self.model_evaluator_module = module_loader.load_model_evaluator()
        print()

    def run(self):
        metadata = self.date_loader.init_metadata()
        print("\nPREPARING DATA")
        attributes = self.date_loader.init_attributes_dict()
        self.summarize_raw_attributes(attributes)
        print("\n\n\nPREPROCESSING FILE")
        attributes = self.data_preprocessor_module.preprocess(attributes)
        self.summarize_preprocessed_files(attributes)
        print("\n\n\nInitializing model")
        attributes = self.model_initializer_module.init_model(attributes)
        print("\nBENCHMARKING MODEL\n")
        for run in metadata[Attributes.RUNS]:
            for index_set in run.index_sets:
                print(f"Running benchmark on Run {run.number} index_set {index_set.number}")
                train_attributes = self.date_loader.create_train_attributes(attributes, index_set)
                test_attributes = self.date_loader.create_test_attributes(attributes, index_set)
                print("Training model")
                self.model_trainer_module.train(train_attributes)
                print("Testing model")
                self.model_tester_module.test(test_attributes)
                print("Evaluating model")
                self.model_evaluator_module.evaluate(
                    self.date_loader.enchance_with_proper_responses(attributes, index_set, test_attributes)
                )
                print()

    def summarize_raw_attributes(self, attributes):
        print("Input data summary")
        print("Raw X head:")
        print(attributes[Attributes.X_RAW].head(5))
        print()
        print("Raw Y head:")
        print(attributes[Attributes.Y_RAW].head(5))

    def summarize_preprocessed_files(self, attributes):
        print("Input data summary after preprocessing")
        print("X head:")
        print(attributes[Attributes.X].head(5))
        print()
        print("Y head:")
        print(attributes[Attributes.Y].head(5))


if __name__ == '__main__':
    Caddo()
