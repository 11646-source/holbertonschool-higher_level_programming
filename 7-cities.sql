-- Create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;
CREATE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY,
	state_id INT NOT NULL,
	UNIQUE KEY unique_city (state_id, name),
	FORGEIN KEY (state_id) REFERENCES states(id)
	);
