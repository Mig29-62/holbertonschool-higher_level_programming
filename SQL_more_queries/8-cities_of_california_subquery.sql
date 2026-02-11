-- we use where command inside a where command to take information out of other tables
SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
) 
ORDER BY id ASC
