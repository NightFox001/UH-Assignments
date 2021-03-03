/*
Jonathan Hirsch
 Query 6: how many available airports are there considering any departure or arrival?
Write your query and store the result in table available_airports.
*/

DROP TABLE IF EXISTS available_airports;
CREATE TABLE available_airports(
    airports int
); 

INSERT INTO available_airports (airports)
SELECT COUNT(DISTINCT airport_code)
FROM bookings.airport
;

--select *  from available_airports;