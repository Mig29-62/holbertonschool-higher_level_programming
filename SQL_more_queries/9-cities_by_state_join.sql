-- we use where command inside a where command to take information out of other tables
SELECT id, name 
FROM cities 
JOIN states
ON cities.state_id=states.id
ORDER BY id ASC
