import requests
from typing import List

from models import Tasks

API_KEY = "$2a$10$afW0S2evt8hkr/cCO3y9Ke8TuXMCzKsvw10KKw832uxoT1IvOA1O."
BASE_URL = "https://api.jsonbin.io/v3"
BIN_ID = "6757aaf7acd3cb34a8b6f5bd"

def load_tasks() -> List[Tasks]:
    """
    Загружает задачи из jsonbin.io
    """
    try:
        url = f"{BASE_URL}/b/{BIN_ID}"
        headers = {"X-Master-Key": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        tasks = data.get("record", [])
        return [Tasks(**task) for task in tasks]
    except requests.RequestException as e:
        print(f"Ошибка при загрузке задач: {e}")
        return []
    except Exception as e:
        print(f"Ошибка обработки данных: {e}")
        return []

def save_tasks(tasks: List[Tasks]):
    """
    Сохраняет задачи на jsonbin.io
    """
    try:
        url = f"{BASE_URL}/b/{BIN_ID}"
        headers = {
            "Content-Type": "application/json",
            "X-Master-Key": API_KEY
        }
        payload = [task.dict() for task in tasks]
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        print("Данные успешно сохранены.")
    except requests.RequestException as e:
        print(f"Ошибка при сохранении задач: {e}")