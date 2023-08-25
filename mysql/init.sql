-- Create the 'users' table for user authentication
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);

-- Create an example user for testing /password
INSERT INTO users (username, email, password) VALUES
    ('test', 'test@example.com', '$2a$04$cCYUWV65Zz.Vpg94IznUDeK7C1tzccI6ucMi5NtHqkEu0lxODrEsK');

-- Add any other tables or data initialization that your application requires below