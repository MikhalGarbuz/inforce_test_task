CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Primary key column
    name VARCHAR(100) NOT NULL,          -- Limit length of name and ensure it is not NULL
    email VARCHAR(255) NOT NULL,  
    signup_date DATE NOT NULL,           -- Date column
    domain VARCHAR(100) NOT NULL         -- Limit length of domain and ensure it is not NULL
);