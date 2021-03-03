/*
 Jonathan Hirsch
 Query 16:  list model and city for flights where a Boeing airplane departs from or arrives to
Write your query and store the result in table boeing_city.
*/

DROP TABLE IF EXISTS boeing_city;
CREATE TABLE boeing_city(
    model character(25),
    city character(20)
);
--temp table
DROP TABLE IF EXISTS refTable;
SELECT *
INTO refTable
    FROM (
         SELECT departure_airport, arrival_airport, aircraft_code
         FROM bookings.flights
         WHERE aircraft_code IN (
             SELECT aircraft_code
             FROM bookings.aircraft
             WHERE model LIKE 'Boeing%')
         GROUP BY departure_airport, arrival_airport, aircraft_code)
        as Temp5
;
--SELECT * FROM refTable;
INSERT INTO boeing_city
SELECT deps.model, bookings.airport.city
FROM (
    SELECT bookings.aircraft.model, reftable.departure_airport
    FROM reftable
    INNER JOIN bookings.aircraft ON refTable.aircraft_code = aircraft.aircraft_code
    GROUP BY departure_airport, aircraft.model) AS deps
-- Only need to join on departures because if it left an airport it had to arrive there first
INNER JOIN bookings.airport ON deps.departure_airport = airport_code
GROUP BY model, city
ORDER BY model
;

--SELECT * FROM boeing_city;
/*
SELECT model, city
FROM bookings.aircraft, bookings.airport
WHERE aircraft.aircraft_code IN (SELECT aircraft_code FROM refTable)
AND  airport.airport_code IN ((
    SELECT departure_airport, aircraft_code
    FROM bookings.flights
    WHERE (
        flights.aircraft_code IN (
            SELECT departure_airport
            FROM bookings.aircraft
            WHERE model LIKE 'Boeing%'
            GROUP BY departure_airport, aircraft_code
            )
        OR
        flights.aircraft_code IN (
            SELECT arrival_airport, aircraft_code
            FROM bookings.flights
            WHERE aircraft_code IN (
            SELECT aircraft_code
            FROM bookings.aircraft
            WHERE model LIKE 'Boeing%'
         )
         GROUP BY arrival_airport, aircraft_code
)
    )
GROUP BY city, model
order by city
;
*/


