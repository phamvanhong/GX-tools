# GX-tools

# 1. Add this function following the path:

src -> metadata_tool -> core -> entities -> table.py ->


def to_dict(self) -> Dict[str, Any]:
        """
        Convert TableEntity to a dictionary.
        Returns:
            Dict[str, Any]: A dictionary representation of the TableEntity.
        """
        entity_dict = super().to_dict()
        entity_dict[COLUMNS] = self.columns
        return entity_dict
        
# 2. Add "COLUMN"

Add COLUMNS to -> from src.metadata_tool.core.entities.common.constants import PATH, QUALIFIED_NAME

# 3. Edit tables name list (tables_name) in main.py you want to write gx

# 4. Edit the null_columns list (in main.py) that refers to the columns want to check null

# 5. After run main.py,following this:

    PowerShell -> cd ..../DataModeling
    
    + Run:
    1. Get-ChildItem -Path "model" -Recurse -Directory | Where-Object { $_.Name -match "plugins|checkpoints|profilers|uncommitted" } | ForEach-Object { Remove-Item -Path $_.FullName -Recurse -Force -Verbose }
    2. Get-ChildItem -Path "model" -Recurse -File | Where-Object { $_.Name -match "great_expectations\.yml|\.ge_store_backend_id|\.gitignore" } | ForEach-Object { Remove-Item -Path $_.FullName -Force -Verbose }
