CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

-- Inserts rows in to flights.
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
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

