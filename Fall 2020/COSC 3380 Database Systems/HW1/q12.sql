/*
Jonathan Hirsch
 Query 12: atomic: show all unique pairs of departure and 
arrival city of delayed flights on an Airbus airplane
Write your query and store the result in table airbus.
*/

DROP TABLE IF EXISTS airbus;
CREATE TABLE airbus(
    departure_airport character(3),
    arrival_airport character(3)
);

INSERT INTO airbus
SELECT  flights.departure_airport,
        flights.arrival_airport
FROM bookings.flights
WHERE status = 'Delayed'
AND aircraft_code IN (
    SELECT aircraft_code
    FROM bookings.aircraft
    WHERE model LIKE '%Airbus%'
    )
;

--SELECT * FROM airbus;

/* Test code
SELECT DISTINCT model
FROM aircrafts_data
WHERE aircraft_code IN ('320', '321', '319')
;

INSERT INTO airbus
SELECT  flights.departure_airport, 
        flights.arrival_airport
FROM flights
WHERE status = 'Delayed'
AND aircraft_code IN (
    SELECT aircraft_code
    FROM aircrafts_data
    WHERE "model" :: jsonb ? 'Airbus'
    )
;
*/