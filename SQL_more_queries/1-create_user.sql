-- Create the user if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the entire server to this user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reload the privilege tables to apply changes
FLUSH PRIVILEGES;
