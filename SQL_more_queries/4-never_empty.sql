-- Create a table named id_not_null with an id column that cannot be NULL
CREATE TABLE id_not_null (
    id INT NOT NULL,          -- id must always have a value, but duplicates are allowed
    name VARCHAR(255) NOT NULL -- name cannot be NULL either
);
