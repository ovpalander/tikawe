CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    pwd_hash TEXT
);
CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    company_name TEXT UNIQUE,
    business_id TEXT UNIQUE,
    city TEXT, 
    address TEXT,
    postal_code TEXT,
    apartment_count INTEGER,
    registration_date TEXT,
    completion_year TEXT
);

CREATE TABLE users_companies (
    user_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, company_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(company_id) REFERENCES companies(id) ON DELETE CASCADE
);

CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file BLOB NOT NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);
