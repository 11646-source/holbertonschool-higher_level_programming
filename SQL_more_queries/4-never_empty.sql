-- Create a table named id_not_null with an id column that cannot be NULL
CREATE TABLE id_not_null (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- Unique identifier, always required
    name VARCHAR(100),                          -- Optional name field
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Automatically stores creation time
);
