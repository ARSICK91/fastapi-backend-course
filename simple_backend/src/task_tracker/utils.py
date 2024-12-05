import json
from typing import List
from models import Tasks

def load_tasks(filename='tasks.json') -> List[Tasks]:
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return [Tasks(**task) for task in tasks]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks: List[Tasks], filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.dict() for task in tasks], file, ensure_ascii=False, indent=4)
