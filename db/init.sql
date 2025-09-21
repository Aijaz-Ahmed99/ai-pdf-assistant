CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    registration_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pdfs (
    id SERIAL PRIMARY KEY,
    user_id TEXT REFERENCES users(user_id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    upload_date TEXT NOT NULL,
    pdf_text TEXT,
    last_updated TEXT
);
