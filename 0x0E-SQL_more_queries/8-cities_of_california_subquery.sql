-- Lists the cities of Califonia
SELECT id, name FROM cities, states
WHERE state_id = states.id
ORDER BY id ASC;
