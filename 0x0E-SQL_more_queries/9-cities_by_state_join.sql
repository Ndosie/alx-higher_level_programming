-- Lists all the cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = state.id
ORDER BY cities.id ASC;
