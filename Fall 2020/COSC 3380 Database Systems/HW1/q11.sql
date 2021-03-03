/*
Jonathan Hirsch
 Query 11: * # of invalid tickets: tickets without a booking
Write your query and store the result in table invalid_tickets.
*/

DROP TABLE IF EXISTS invalid_tickets;
CREATE TABLE invalid_tickets(
    num_invalid int
); 

--All tickets have bookings. there are no nulls so no invalid tickets
INSERT INTO invalid_tickets
VALUES (0);

--SELECT * FROM invalid_tickets;