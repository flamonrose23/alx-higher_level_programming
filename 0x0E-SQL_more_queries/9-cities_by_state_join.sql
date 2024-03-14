-- Writing script listing all cities contained in database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id;
