-- Switch to the hbtn_0c_0 database
USE hbtn_0c_0;

-- Compute the average of the 'score' column in the 'second_table' table
-- The AVG() function calculates the mean value of the specified numeric column
SELECT AVG(score) AS average_score
FROM second_table;
