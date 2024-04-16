from constant import *
import sys
sys.path.append(BASE_PATH)
import os
from src.metadata_tool.core.platform.common.configs import BRONZE
import json
from src.metadata_tool.services.metadata_lookup.dictionary import DictionaryService
from src.metadata_tool.core.platform.filesystem import EntityFileSystem


class TablesMetadata():
    """
    Initial a TablesMetadata object to get table metadata of a sppecific tier
    """

    def __init__(self, table_names: list) -> None:
        """
        Args:
            dict_service (DictionaryService): a DictionaryService object
            entity_filesys (EntityFileSystem): a EntityFileSystem
            tier (str): The tier for the service (BRONZE, SILVER and GOLD)
        """
        self.dict_service = DictionaryService(BASE_PATH, BRONZE)
        self.entity_filesys = EntityFileSystem(BASE_PATH, BRONZE)
        self.table_names = table_names

    def get_tables_metadata(self) -> list:
        """Get tables metadata by name of tables

        Returns:
            list: a list including tables metadata
        """
        tables_metadata = []
        for name in self.table_names:
            # get metadata each table by name
            metadata = self.dict_service.get_table_metadata_dict(name)
            tables_metadata.append(metadata)
        return tables_metadata

    def add_expectation_suite_column(self, tables_metadata: list) -> list:
        """
        Add "expectation_suite" column to sub tables metadata

        Returns:
            list: a sub tables metdata was added Expectaion_suite column
        """
        for table in tables_metadata:
            table_name = table[NAME]
            expectations_suite_name = f"{table_name}_" + EXPECTATION_SUITE
            table[EXPECTATION_SUITE] = expectations_suite_name
        return tables_metadata

    def create_sub_metadata(self) -> list:
        """
        Get features from tables metadata to create sub-tables metadata

        Returns:
            list: a list including sub-tables metadata
        """
        tables_metadata = self.get_tables_metadata()
        sub_tables_metadata = []
        for metadata in self.add_expectation_suite_column(tables_metadata):
            features = {
                NAME: metadata[NAME],
                PATH: metadata[ATTRIBUTES][PATH],
                COLUMNS: metadata[COLUMNS],
                KEYS: metadata[KEYS],
                EXPECTATION_SUITE: metadata[EXPECTATION_SUITE]
            }
            sub_tables_metadata.append(features)

        return sub_tables_metadata

    def convert_to_json(self, json_file_name: str) -> json:
        """
        Convert sub_metadata to json file

        Args:
            json_file_name (str): json file name to write tables metadata (./path/filename.json)

        Returns:
            json: json file
        """
        output_json = json.dumps(self.create_sub_metadata(), indent=2)
        # Write to json file
        with open(json_file_name, WRITE) as json_file:
            return json_file.write(output_json)
