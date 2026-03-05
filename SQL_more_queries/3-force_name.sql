-- 1. Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    -- 2. Define an auto-incrementing ID as the primary key
    id INT NOT NULL AUTO_INCREMENT,
    
    -- 3. Define a column to store the force name
    force_name VARCHAR(100) NOT NULL,
    
    -- 4. Add a timestamp for when the record was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- 5. Set the primary key
    PRIMARY KEY (id)
);
