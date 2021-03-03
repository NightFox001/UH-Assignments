/*
 Jonathan Hirsch
 Query 13: total fares sales amount by
fare class for flights departing from Moscow
Write your query and store the result in table fares_sales.
*/

DROP TABLE IF EXISTS fares_sales;
CREATE TABLE fares_sales(
    fare_conditions character varying(10),
    amount numeric(12,2)
);

INSERT INTO fares_sales
SELECT fare_conditions, SUM(amount)
FROM bookings.ticket_flights
WHERE ticket_flights.flight_id IN (
    SELECT flight_id
    FROM bookings.flights
    WHERE departure_airport IN (
        SELECT airport_code
        FROM bookings.airport
        WHERE city = 'Moscow'
    )
)
GROUP BY fare_conditions
;

--SELECT * FROM fares_sales;

/*
--This took an hour to figure out...
SELECT airport_code
FROM airports_data
WHERE city -> 'en' = '"Moscow"'
;

*/


