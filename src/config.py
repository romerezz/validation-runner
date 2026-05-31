import json
from src.errors import ValidationError

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        raise ValidationError("Configuration file not found")