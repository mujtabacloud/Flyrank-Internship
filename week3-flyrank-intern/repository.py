import os
import psycopg


class TaskRepository:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")

    def get_all(self):
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, title, done FROM tasks ORDER BY id"
                )
                return cur.fetchall()

    def get(self, task_id):
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, title, done FROM tasks WHERE id = %s",
                    (task_id,)
                )
                return cur.fetchone()

    def create(self, title):
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO tasks (title, done)
                    VALUES (%s, %s)
                    RETURNING id
                    """,
                    (title, False)
                )
                task_id = cur.fetchone()[0]
            conn.commit()
            return task_id

    def update(self, task_id, title, done):
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE tasks
                    SET title = %s, done = %s
                    WHERE id = %s
                    """,
                    (title, done, task_id)
                )
            conn.commit()

    def delete(self, task_id):
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM tasks WHERE id = %s",
                    (task_id,)
                )
            conn.commit()
