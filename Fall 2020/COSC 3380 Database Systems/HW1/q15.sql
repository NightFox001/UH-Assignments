/*
 Jonathan Hirsch
 Query 15: tickets sold per fare class, only for arrived flights
Write your query and store the result in table tickets_sold.
*/

DROP TABLE IF EXISTS tickets_sold;
CREATE TABLE tickets_sold(
    fare_conditions character varying(10),
    tickets int
    
); 
INSERT INTO tickets_sold
SELECT fare_conditions,
       COUNT(ticket_no)
FROM bookings.ticket_flights
WHERE ticket_flights.flight_id IN (
    SELECT flight_id
    FROM bookings.flights
    WHERE status = 'Arrived'
    )
GROUP BY fare_conditions
;

--select * from tickets_sold;
