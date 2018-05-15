CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

-- Inserts rows in to flights.
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);

-- Selects all rows/columns from flights.
SELECT * FROM flights;

-- Selects all rows from origin and destination columns from flights.
SELECT origin, destination FROM flights;

-- Selects row with id = 3 and all columns from flights.
SELECT * FROM flights WHERE id = 3;

-- Selects rows with origin = New York and all columns from flights.
SELECT * FROM flights WHERE origin = 'New York';

-- Selects rows with duraction of greater than 500 and all columns from flights.
SELECT * FROM flights WHERE duraction > 500; 
-- Selects rows with destination is paris AND the duration is greater than 500 from flights.
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;

-- Selects rows with destination is paris OR the duration is greater than 500 from flights.
SELECT * FROM flights WHERE destination = 'Paris' or duration > 500;

-- Returns the average duration from flights
SELECT AVG(duration) FROM flights;

-- Returns the average duration from flights where the origin is new york
SELECT AVG(duration) FROM flights WHERE origin = 'New York';

-- Returns the number of entries in flights
SELECT COUNT(*) FROM flights;

-- Other functions include 
-- MIN()
-- MAX()

-- selects
SELECT * FROM flights WHERE origin in ('New York', 'Lima');

-- Selects all origin entries that has an 'a'. %substring%
SELECT * FROM flights WHERE origin LIKE '%a%';

DELETE FROM flights WHERE origin='New York';

SELECT * FROM flights ORDER BY duration ASC;

SELECT * FROM flights ORDER BY duration DESC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

-- Foreign Keys

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 8);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 8);

-- Joins
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';

-- Selects all data from left table
SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;
-- Selects all data from right table
SELECT origin, destination, name FROM flights RIGHT JOIN passengers ON passengers.flight_id = flights.id;

--Indexing