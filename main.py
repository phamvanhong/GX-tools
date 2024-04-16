from constant import *
import sys
sys.path.append(BASE_PATH)

from samples.GX.expectation_cases import ExpectationsCases
from samples.GX.update_sub_tables_metadata import update_tables_metadata
from samples.GX.get_metadata import TablesMetadata


def write_expectation(tables_metadata_path: str) -> None:
    """Writing expectaiton suite for each tables in a specific tier (BRONZE, SILVER or GOLD) 

    Args:
        tables_metadata_path (str): path to json file including tables metadata of a specific tier

    Returns:
        None
    """
    ax = ExpectationsCases(tables_metadata_path)
    # Add expectation that table columns match an order set
    ax.expect_table_columns_match_set()

    # Add expectation that columns value to be not null
    ax.expect_colum_value_not_null()

    # Add expectation that compound columns to be unique
    ax.expect_compound_columns_unique()


if __name__ == "__main__":
    #set up table name
    table_names = ["RTOM_EB_TRAN_MTHLY", "RTOM_REG_AUTODEBIT_BILL", "RTOM_DIGI_ALL_USERS"]

    table_metadata = TablesMetadata(table_names)

    table_metadata.convert_to_json(TABLES_METADATA)

    update_tables_metadata(TABLES_METADATA)

    write_expectation(TABLES_METADATA)


