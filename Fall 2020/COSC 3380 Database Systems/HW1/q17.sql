/*
 Jonathan Hirsch
 Query 17:  list flight_id,scheduled departure date,departing city, departing airport, arrival city, arrival airport
 for delayed flights for passenger ELENA
Write your query and store the result in table R.
*/

DROP TABLE IF EXISTS elena_delayed;
CREATE TABLE elena_delayed(
    flight_id int,
    scheduled_departure timestamptz,
    d_city character(20),
    departure_airport character(3),
    a_city character(20),
    arrival_airport character(3)
); 

INSERT INTO elena_delayed
SELECT Tempq17.flight_id, scheduled_departure, Tempq17.city, departure_airport, airport.city, arrival_airport
FROM (
    SELECT  flights.flight_id, flights.scheduled_departure, airport.city, flights.departure_airport, arrival_airport
    FROM bookings.flights
    INNER JOIN bookings.airport on flights.departure_airport = airport.airport_code
    WHERE status LIKE 'Delayed'
    AND flight_id IN (
        SELECT flight_id
        FROM bookings.ticket_flights
        WHERE ticket_no IN (
            SELECT ticket_no
            FROM bookings.ticket
            WHERE passenger_name LIKE '%ELENA%'
            )
        )
    ) as Tempq17
INNER JOIN bookings.airport ON Tempq17.arrival_airport = airport_code
;

select * from elena_delayed;