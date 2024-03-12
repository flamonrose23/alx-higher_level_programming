-- Writing script listing all records of the second_table
-- Records should be listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
