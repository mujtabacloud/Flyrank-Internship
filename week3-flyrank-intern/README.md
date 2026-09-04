Flyrank Backend — Week 3

A FastAPI backend application for the Flyrank Week 3 internship task.

Requirements
Python 3.12+
PostgreSQL 16+
Python virtual environment

Docker is optional. The application can be run directly with Python/Uvicorn if PostgreSQL is available locally.

Setup
1. Clone or open the project
cd "D:\Flyrank Back-End intern\week3-flyrank-intern"

2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root.

Example:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/tasks


Use the variables required by the application if your project already provides a .env.example file.

Database

The Docker Compose configuration uses:

Database: tasks
User: postgres
Password: postgres
PostgreSQL port: 5432

The initial database schema is located at:

sql/init.sql


If PostgreSQL is running locally, make sure the tasks database exists and initialize it using sql/init.sql.

Run the Application

With the virtual environment activated:

uvicorn main:app --host 0.0.0.0 --port 8000


The API will be available at:

http://localhost:8000


FastAPI interactive documentation:

http://localhost:8000/docs


Alternative documentation:

http://localhost:8000/redoc

Docker

If Docker is available, the complete application and PostgreSQL database can be started with:

docker compose up --build


The application will then be available at:

http://localhost:8000

Project Structure
week3-flyrank-intern/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── sql/
│   └── init.sql
│
└── README.md

API

The API is implemented using FastAPI.

After starting the application, visit:

http://localhost:8000/docs


to view and test the available endpoints.

Development

To stop the local server, press:

CTRL + C


To restart it:

uvicorn main:app --host 0.0.0.0 --port 8000