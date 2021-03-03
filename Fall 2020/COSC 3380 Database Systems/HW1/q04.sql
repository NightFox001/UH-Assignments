/*
Jonathan Hirsch
 Query 4: list airport code for airports located in Asia
Write your query and store the result in table airport_asia.
*/

DROP TABLE IF EXISTS airport_asia;
CREATE TABLE airport_asia(
    airport_code character(3)
); 

INSERT INTO airport_asia (airport_code) 
SELECT DISTINCT airport_code
FROM bookings.airport
WHERE timezone LIKE 'Asia%'
;

--select * FROM airport_asia;
