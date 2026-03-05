-- Create the dstabase if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist, identified by a password
CREATE USER IF NOT EXISTS 'user_0d_2'@' localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the hbtn_0d_2 database to the user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Apply the changes to the privilege tables
FLUSH PRIVILEGES;
