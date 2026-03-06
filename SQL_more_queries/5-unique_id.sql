-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Select the database to use
USE mydatabase;

-- Create the table 'unique_id' with an auto-incrementing ID column
CREATE TABLE unique_id (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);
