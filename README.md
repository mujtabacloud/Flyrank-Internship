FlyRank Backend AI Engineering - Week 2 Assignment
Overview

This project is a simple CRUD API built with FastAPI and SQLite.

The API allows users to create, read, update, and delete tasks.

Technologies Used
Python 3.12
FastAPI
Uvicorn
SQLite
Database

The project uses SQLite because it is lightweight and does not require a separate database server.

The database file is:

tasks.db

The tasks table contains:

id - unique task ID
title - task title
done - task completion status

The database and table are automatically created when the application starts.

Three example tasks are added only when the database is empty.

How to Run

Install the dependencies:

py -3.12 -m pip install fastapi uvicorn


Start the server:

py -3.12 -m uvicorn main:app --reload


The API runs at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

API Endpoints
GET /tasks - Get all tasks
GET /tasks/{id} - Get one task
POST /tasks - Create a task
PUT /tasks/{id} - Update a task
DELETE /tasks/{id} - Delete a task
Example SQL Query
SELECT * FROM tasks WHERE done = 1;


This query shows all completed tasks.

Database Screenshot

The SQLite database was opened using DB Browser for SQLite and the tasks table was checked.

Add the database screenshot here.

Persistence

Tasks are stored in SQLite instead of an in-memory list. Therefore, tasks remain available after restarting the server.

Author

Created as part of the FlyRank Backend AI Engineering Internship.