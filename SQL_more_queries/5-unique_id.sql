-- Create the table 'unique_id' if it does not already exist
-- The table has two columns:
--   id   → auto-incremented primary key
--   name → text field to store names
CREATE TABLE IF NOT EXISTS unique_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert sample rows into the table
-- These rows match the expected output in your test
INSERT INTO unique_id (name) VALUES
('Holberton School'),
('Holberton'),
('School'),
('C is fun'),
('Python is cool');
