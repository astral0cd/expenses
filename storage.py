import json
import os

DATA_FILE = 'expenses.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"categories": [], "expenses": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"categories": [], "expenses": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)