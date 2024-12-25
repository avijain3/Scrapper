import json
import os
from typing import List, Dict

class StorageManager:
    def __init__(self, file_path: str = "scraped_data.json"):
        self.file_path = file_path

    def save(self, data: List[Dict]):
        # Read existing data if file exists
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Merge new data with existing
        updated_data = existing_data + data

        with open(self.file_path, "w") as file:
            json.dump(updated_data, file, indent=4)

        print(f"Data saved to {self.file_path}")

    def read(self) -> List[Dict]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []

