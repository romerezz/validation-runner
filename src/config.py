import json
from src.errors import ValidationError

def load_config() -> dict:
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        raise ValidationError("Configuration file not found")
    
CONFIG = {
    "allowed_test_types": ["smoke", "regression", "negative"],
    "default_timeout_seconds": 5,
    "logs_enabled": True,
}