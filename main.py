from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# Connect to database
conn = sqlite3.connect("tasks.db", check_same_thread=False)

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0
)
""")
conn.commit()

# Add 3 example tasks only if database is empty
count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]

if count == 0:
    conn.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Learn Python", 0))
    conn.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Build API", 0))
    conn.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Test API", 1))
    conn.commit()


# GET all tasks
@app.get("/tasks")
def get_tasks():
    cursor = conn.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    return [
        {"id": task[0], "title": task[1], "done": bool(task[2])}
        for task in tasks
    ]


# GET one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

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

    cursor = conn.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (title, 0)
    )
    conn.commit()

    return {
        "id": cursor.lastrowid,
        "title": title,
        "done": False
    }


# PUT - update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
    title = task.get("title")
    done = task.get("done", False)

    existing = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")

    if not title:
        raise HTTPException(status_code=400, detail="Title is required")

    conn.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (title, int(done), task_id)
    )
    conn.commit()

    return {
        "id": task_id,
        "title": title,
        "done": done
    }


# DELETE task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    existing = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")

    conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()

    return {"message": "Task deleted successfully"}
