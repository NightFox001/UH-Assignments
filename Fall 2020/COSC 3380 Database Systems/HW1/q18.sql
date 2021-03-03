/*
 Jonathan Hirsch
 Query 18:  list departing airport, total # of flights and # of delayed flights with more delayed flights
 that is, the most inefficient airport. if there is a tie you can display all tied airports
Write your query and store the result in table R.
*/

DROP TABLE IF EXISTS delayed_airport;
CREATE TABLE delayed_airport(
    departure_airport character(3),
    count_flights int,
    count_delayed int
);

INSERT INTO delayed_airport
SELECT  delayed_cities.delay_airport,
        total_count,
        delayed_cities.delay_count
    FROM
    (   --number of delayed flights for all airports
        SELECT COUNT(flight_id) as delay_count, flights.departure_airport as delay_airport
        FROM bookings.flights
        WHERE status LIKE 'Delayed'
        GROUP BY delay_airport, status) AS delayed_cities,
    (   --total flights for all airports
        SELECT COUNT(flight_id) AS total_count, flights.departure_airport as all_airportC
        FROM bookings.flights
        WHERE departure_airport IN (
            SELECT flights.departure_airport as delay_airport
            FROM bookings.flights
            WHERE status LIKE 'Delayed'
            GROUP BY delay_airport, status) --AS delayed_cities2
        GROUP BY departure_airport) AS all_airports
WHERE delay_count IN ( --relation containing the max num of delayed flights for any airport
    SELECT MAX(delayed_ports.delay_count)
    FROM (
             SELECT delayed_cities.delay_count
             FROM (
                      --number of delayed flights for all airports
                      SELECT COUNT(flight_id) as delay_count, flights.departure_airport as delay_airport
                      FROM bookings.flights
                      WHERE status LIKE 'Delayed'
                      GROUP BY delay_airport, status) AS delayed_cities,
                  (
                      SELECT COUNT(flight_id) AS total_count, flights.departure_airport
                      FROM bookings.flights
                      GROUP BY departure_airport) AS all_airports
         ) AS delayed_ports
    )
AND delay_airport = all_airportC
;

select * from delayed_airport;


-- testing code below
/*SELECT *      -- COUNT(flight_id) as delay_count, flights.departure_airport as delay_airport
        FROM bookings.flights
        WHERE status LIKE 'Delayed'
        --GROUP BY delay_airport, statu) AS delayed_cities,
--GROUP BY departure_airport AS all_airports
*/
