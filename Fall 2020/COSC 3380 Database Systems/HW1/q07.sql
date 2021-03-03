/*
 Jonathan Hirsch
 Query 7: list bookings and number of passengers with 2 or more passengers together
Write your query and store the result in table bookings_passenger.
*/

DROP TABLE IF EXISTS bookings_passenger;
CREATE TABLE bookings_passenger(
    book_ref character(6),
    passengers int
); 


INSERT INTO bookings_passenger
SELECT book_ref, COUNT(passenger_id)
FROM bookings.ticket
GROUP BY book_ref
HAVING COUNT(passenger_id) > 1
;

--select * from bookings_passenger;

/*
-- Test code
SELECT book_ref, COUNT(passenger_id)
FROM ticket
GROUP BY book_ref
HAVING COUNT(passenger_id) > 1
;

--Testing num of bookings in ticket
SELECT COUNT(book_ref FROM ticket;
SELECT COUNT(DISTINCT book_ref) FROM ticket;

 */
