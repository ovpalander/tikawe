CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    pwd_hash TEXT
);
CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    companyname TEXT UNIQUE,
    address TEXT,
    postal_code TEXT,
    apartment_count INTEGER,
    registration_date TEXT,
    completion_year
);

CREATE TABLE users_companies (
    user_id INTEGER NOT NULL,
    company_id INTEGER,
    PRIMARY KEY (user_id, company_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(company_id) REFERENCES companies(id) ON DELETE CASCADE
);
