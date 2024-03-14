-- Writing script creating database hbtn_0d_usa and table states (in database hbtn_0d_usa)
-- on my MySQL server
-- states description: id INT unique (primary key) and name VARCHAR(256)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE, name VARCHAR(256) NOT NULL);
