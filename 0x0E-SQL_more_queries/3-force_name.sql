-- Writing script creating the table force_name on my MySQL server
-- force_name description: id INT and name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
