-- Lists all records of the table second_table of the database hbtn_0c_0
-- Displays only rows where name has a value
-- Shows: score - name
-- Results sorted by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
