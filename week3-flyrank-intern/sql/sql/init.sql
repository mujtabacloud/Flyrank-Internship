CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO tasks (title, done)
SELECT 'Learn Python', FALSE
WHERE NOT EXISTS (SELECT 1 FROM tasks);

INSERT INTO tasks (title, done)
SELECT 'Build API', FALSE
WHERE NOT EXISTS (SELECT 1 FROM tasks WHERE title = 'Build API');

INSERT INTO tasks (title, done)
SELECT 'Test API', TRUE
WHERE NOT EXISTS (SELECT 1 FROM tasks WHERE title = 'Test API');
