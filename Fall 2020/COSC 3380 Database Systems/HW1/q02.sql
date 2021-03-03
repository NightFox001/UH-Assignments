/*
Jonathan Hirsch
 
Query 2: list passenger name, number of distinct booking ref #, number of tickets
 and # of distinct emails for passenger VLADIMIR MOROZOV
Write your query and store the result in table vladimir.
*/

DROP TABLE IF EXISTS vladimir;
CREATE TABLE vladimir(
    passenger_name text, 
    number_of_booking int,
    number_of_tickets int,
    number_of_emails int
); 

-- V2 
INSERT INTO vladimir
SELECT  DISTINCT passenger_name,
        COUNT(DISTINCT book_ref), 
        COUNT(DISTINCT ticket_no), 
        COUNT(DISTINCT email)
FROM    bookings.ticket
WHERE   passenger_name  LIKE 'VLADIMIR MOROZOV'
GROUP BY passenger_name
;

--SELECT * FROM vladimir;

/*
-- V1.2
INSERT INTO vladimir (passenger_name)
SELECT DISTINCT passenger_name 
FROM ticket
WHERE passenger_name LIKE 'VLADIMIR MOROZOV'
;
INSERT INTO vladimir (number_of_booking)
SELECT COUNT(DISTINCT book_ref) 
FROM ticket
WHERE passenger_name LIKE 'VLADIMIR MOROZOV'
;
INSERT INTO vladimir (number_of_tickets)
SELECT COUNT(DISTINCT ticket_no) 
FROM ticket
WHERE passenger_name LIKE 'VLADIMIR MOROZOV'
;
INSERT INTO vladimir (number_of_emails)
SELECT COUNT(DISTINCT email) 
FROM ticket
WHERE passenger_name LIKE 'VLADIMIR MOROZOV'
;
*/

/* TESTING 
SELECT  passenger_name,
        COUNT(DISTINCT book_ref) AS Bookings, 
        COUNT(DISTINCT ticket_no) AS Tickets, 
        COUNT(DISTINCT email) AS Emails 
FROM ticket
WHERE   passenger_name  LIKE 'VLADIMIR MOROZOV'
GROUP BY passenger_name
;
*/
