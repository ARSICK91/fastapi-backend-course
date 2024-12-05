from typing import List,Dict
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException


@dataclass(slots=True, frozen=True)
class Task:
    id: int
    title: str
    status: str

app = FastAPI()

tasks: List[Task] = [
    Task(1,'Artur','OUTist')
]

@app.get('/tasks', response_model=List[Task])
def get_tasks():
    return tasks

@app.post('/tasks', response_model=Task)
def create_task(task: Task):
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail='Таска с таким id Уже существует')
    tasks.append(task)
    return task

@app.put('/tasks/{task_id}', response_model=Task)
def put_task(task_id: int, update_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = update_task
            return tasks[index]
    raise HTTPException(status_code=404, detail='Нет таски с таким id')

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index] 
            return {'detail': 'Таска была удалена'}
    raise HTTPException(status_code=404, detail=f'Нет таски с таким id = {type(task_id)}: {task_id}')