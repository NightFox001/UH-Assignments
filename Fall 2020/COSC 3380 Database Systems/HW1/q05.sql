/*
Jonathan Hirsch
 Query 5:  aircraft model of planes without any flight, i.e. an airplane that is not used at all
Write your query and store the result in table no_flight.
*/

DROP TABLE IF EXISTS no_flight;
CREATE TABLE no_flight(
    model character(25)
);

INSERT INTO no_flight
SELECT DISTINCT aircraft.model
FROM bookings.aircraft
WHERE aircraft_code NOT IN (SELECT DISTINCT aircraft_code FROM bookings.flights)
;

--SELECT * FROM no_flight;

/*
--Test code works
SELECT DISTINCT model
FROM aircrafts_data
WHERE aircraft_code IN (SELECT DISTINCT aircraft_code FROM flights)
;

--All aircraft codes
SELECT DISTINCT aircraft_code
FROM aircrafts_data;

--All aircraft codes with flights
SELECT DISTINCT aircraft_code
FROM flights
;
*/