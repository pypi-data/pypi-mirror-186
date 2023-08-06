from copy import deepcopy

from caddo_file_parser.caddo_file_parser import CaddoFileParser
from caddo_file_parser.models.index_set import IndexSet
from pandas import DataFrame

from caddo_tool.modules import Attributes
from caddo_tool.settings.settings import Settings


class DataLoader:
    def init_metadata(self) -> dict:
        caddo_file = self._get_caddo_file()
        return self._load_metadata(caddo_file)

    def init_attributes_dict(self) -> dict:
        caddo_file = self._get_caddo_file()
        return self._load_attributes(caddo_file)

    def _get_caddo_file(self):
        caddo_file_parser = CaddoFileParser()
        return caddo_file_parser.read_data(Settings.input_data_file)

    def _load_attributes(self, caddo_file) -> dict:
        attributes = dict()
        attributes[Attributes.X_RAW] = self._get_raw_x(caddo_file.data)
        attributes[Attributes.Y_RAW] = self._get_raw_y(caddo_file.data)
        return attributes

    def _get_raw_x(self, data) -> DataFrame:
        return data.filter(regex="^[xX]__", axis=1)

    def _get_raw_y(self, data):
        return data.filter(regex="^[yY]__", axis=1)

    def _load_metadata(self, caddo_file) -> dict:
        metadata = dict()
        metadata[Attributes.RUNS] = caddo_file.runs
        return metadata

    def create_train_attributes(self, attributes, index_set: IndexSet):
        train_attributes = dict()
        train_attributes[Attributes.X] = deepcopy(attributes[Attributes.X].iloc[index_set.train_indexes])
        train_attributes[Attributes.Y] = deepcopy(attributes[Attributes.Y].iloc[index_set.train_indexes])
        train_attributes[Attributes.MODEL] = attributes[Attributes.MODEL]
        return train_attributes

    def create_test_attributes(self, attributes, index_set: IndexSet):
        test_attributes = dict()
        test_attributes[Attributes.X] = deepcopy(attributes[Attributes.X].iloc[index_set.test_indexes])
        test_attributes[Attributes.MODEL] = attributes[Attributes.MODEL]
        return test_attributes

    def enchance_with_proper_responses(self, attributes, index_set: IndexSet, test_attributes):
        test_attributes[Attributes.Y_TRUE] = attributes[Attributes.Y].iloc[index_set.test_indexes]
        return test_attributes
