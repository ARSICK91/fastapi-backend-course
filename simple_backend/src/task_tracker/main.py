from typing import List, Dict

from fastapi import FastAPI, HTTPException

from utils import load_tasks, save_tasks
from models import Tasks

app = FastAPI()
tasks: List[Tasks] = load_tasks()

@app.get('/tasks')
def get_tasks() -> List[Tasks]:
    return tasks

@app.post('/tasks')
def create_task(task: Tasks) -> Tasks:
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail='Таска с таким id уже существует')
    tasks.append(task)
    save_tasks(tasks)
    return task

@app.put('/tasks/{task_id}')
def put_task(task_id: int, update_task: Tasks) -> Tasks:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = update_task
            save_tasks(tasks)
            return tasks[index]
    raise HTTPException(status_code=404, detail=f'Нет таски с таким id = {task_id}')

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int) -> Dict[str, str]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            save_tasks(tasks)
            return {'detail': 'Таска была удалена'}
    raise HTTPException(status_code=404, detail=f'Нет таски с таким id = {task_id}')