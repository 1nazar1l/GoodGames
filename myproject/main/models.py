from django.db import models
import json
import io

class JSONData:
    def __init__(self, data_file='games.json'):
        with io.open(data_file, 'r', encoding='Utf-8') as f:
            self.data = json.load(f)
