-- List all records with score >= 10
-- from the table second_table
-- Results show score then name, ordered by score descending

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
