FlyRank Backend AI Engineering - Week 2 Assignment
Overview
This project is a simple CRUD API built with FastAPI and SQLite.

The API allows users to create, read, update, and delete tasks. Tasks are stored in a SQLite database so the data remains available after restarting the server.

Technologies Used
Python 3.12
FastAPI
Uvicorn
SQLite
Database
SQLite is used because it is lightweight and does not require a separate database server.

The database file is:

tasks.db

The database contains a table called tasks with these columns:

Column	Type	Description
id	INTEGER	Unique task ID
title	TEXT	Task title
done	BOOLEAN	Task completion status

The database and table are automatically created when the application starts.

Three example tasks are added only when the database is empty.

Project Structure
.
├── main.py
├── tasks.db
├── requirements.txt
└── README.md

Installation
Install the required packages:

py -3.12 -m pip install fastapi uvicorn

Run the Server
Start the server with:

py -3.12 -m uvicorn main:app --reload

The server will run at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs

API Endpoints
Get all tasks
GET /tasks

Returns all tasks from the SQLite database.

Get one task
GET /tasks/{id}

Returns a specific task.

If the task does not exist, the API returns:

{
  "detail": "Task not found"
}

Create a task
POST /tasks

Example request:

{
  "title": "Buy milk"
}

Update a task
PUT /tasks/{id}

Example request:

{
  "title": "Buy milk and bread",
  "done": true
}

Delete a task
DELETE /tasks/{id}

Deletes the selected task.

Example SQL Query
The following SQL query shows all completed tasks:

SELECT * FROM tasks WHERE done = 1;

Other example queries:

SELECT * FROM tasks;

SELECT COUNT(*) FROM tasks;

UPDATE tasks SET done = 1;

DELETE FROM tasks WHERE done = 1;

Persistence
Unlike the previous in-memory version, this project stores tasks in SQLite.

Therefore, tasks remain available even after the server is stopped and restarted.

Database Screenshot
The tasks.db database was opened using a SQLite database viewer.

The screenshot below shows the tasks table and stored tasks.

<!-- Add your database screenshot here -->
Author
Created as part of the FlyRank Backend AI Engineering Internship – Week 2 Assignment.
