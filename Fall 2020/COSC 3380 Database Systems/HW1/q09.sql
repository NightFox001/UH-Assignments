/*
Jonathan Hirsch
 Query 9:  list cities with 2 or more airports
Write your query and store the result in table city_airport.
*/

DROP TABLE IF EXISTS city_airport;
CREATE TABLE city_airport(
    city character(20)
);

INSERT INTO city_airport
SELECT cities
FROM (SELECT city as cities
    FROM bookings.airport
    GROUP BY city
    HAVING COUNT(airport_code) > 1) AS temp
;

--SELECT * FROM city_airport;

/* Test code to print results
SELECT cities, num
FROM (SELECT city as cities, COUNT(airport_code) as num
FROM airports_data
GROUP BY city
HAVING COUNT(airport_code) > 1) AS temp
;

select count(city), city
   from airport
   group by city;
select count(city), city
   from airport
   group by city
   having count(airport) > 1;

*/