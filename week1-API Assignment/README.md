# FlyRank Backend AI Engineering - Week 1 Assignment

## Overview

This project is a simple REST API built with **FastAPI** as part of the FlyRank Backend AI Engineering internship assignment.

The API exposes two JSON endpoints:

* `/` – Returns a welcome message.
* `/health` – Returns the server health status.

## Technologies Used

* Python 3.12
* FastAPI
* Uvicorn

## Project Structure

```
.
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <https://github.com/mujtaba666/Flyrank-Internship.git>
cd <week1-API Assignment>
```

2. Create and activate a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
python -m uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

## API Endpoints

### GET /

Returns:

```json
{
  "message": "Hello FlyRank! This is Mujtaba(flyrank internee) and this is my first API assignment."
}
```
<img width="1363" height="703" alt="Screenshot 2026-07-12 111544" src="https://github.com/user-attachments/assets/9a3ddf33-5e91-4b66-9c2c-88a18633d86c" />


### GET /health

Returns:

```json
{
  "status": "ok"
}
```
<img width="1365" height="725" alt="Screenshot 2026-07-12 111625" src="https://github.com/user-attachments/assets/abbd8e1e-372c-4695-af53-7bd7c194c078" />


## Testing

Using a browser:

* http://127.0.0.1:8000/
* http://127.0.0.1:8000/health


## Author

Created as part of the FlyRank Backend AI Engineering Internship – Week 1 Assignment.
