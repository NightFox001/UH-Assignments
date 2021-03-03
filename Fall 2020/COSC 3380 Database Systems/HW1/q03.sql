/*
Jonathan Hirsch 
 Query 3: list number of seats available per aircraft 
Write your query and store the result in table seats_aircraft.
*/

DROP TABLE IF EXISTS seats_aircraft;
CREATE TABLE seats_aircraft(
    aircraft_code character(3), 
    seats int
); 

--V2
INSERT INTO seats_aircraft
SELECT  aircraft_code,
        COUNT(seat_no)
FROM bookings.seats
GROUP BY aircraft_code
;

--SELECT * FROM seats_aircraft;

/* V1
INSERT INTO seats_aircraft  (aircraft_code), 
                            (seats_aircraft.seats)
SELECT  (seats.aircraft_code),
        (seats.seat_no)
FROM    seats
GROUP BY seats.aircraft_code
;
*/

/* Test code
 SELECT aircraft_code,
        COUNT(seat_no) AS seats
 FROM seats
 GROUP BY aircraft_code
 ;

   select aircraft_code, count(aircraft_code) from seats group by aircraft_code ;
*/

DROP TABLE IF EXISTS seats_aircraft;



