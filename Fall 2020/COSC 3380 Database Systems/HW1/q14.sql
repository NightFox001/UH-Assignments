/*
 Jonathan Hirsch
 Query 14: list booking code and names of passengers in bookings with 3 or more passengers together
Write your query and store the result in table booking_code.
*/

DROP TABLE IF EXISTS booking_code;
CREATE TABLE booking_code(
    book_ref character(6),
    passenger_name text

);

INSERT INTO booking_code
SELECT book_ref,
       passenger_name
FROM bookings.ticket
WHERE book_ref IN (
    SELECT book_ref
    FROM bookings.ticket
    GROUP BY book_ref
    HAVING COUNT(passenger_id) > 2
)
;

SELECT * FROM booking_code;
