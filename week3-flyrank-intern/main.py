import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from repository import TaskRepository

load_dotenv()

app = FastAPI()

repo = TaskRepository()


# GET all tasks
@app.get("/tasks")
def get_tasks():
    tasks = repo.get_all()

    return [
        {
            "id": task[0],
            "title": task[1],
            "done": bool(task[2])
        }
        for task in tasks
    ]


# GET one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = repo.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task[0],
        "title": task[1],
        "done": bool(task[2])
    }


# POST - create task
@app.post("/tasks", status_code=201)
def create_task(task: dict):
    title = task.get("title")

    if not title:
        raise HTTPException(status_code=400, detail="Title is required")

    task_id = repo.create(title)

    return {
        "id": task_id,
        "title": title,
        "done": False
    }


# PUT - update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
    title = task.get("title")
    done = task.get("done", False)

    existing = repo.get(task_id)

    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if not title:
        raise HTTPException(status_code=400, detail="Title is required")

    repo.update(task_id, title, done)

    return {
        "id": task_id,
        "title": title,
        "done": done
    }


# DELETE task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    existing = repo.get(task_id)

    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")

    repo.delete(task_id)

    return {"message": "Task deleted successfully"}
