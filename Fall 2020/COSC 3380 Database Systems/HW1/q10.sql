/*
Jonathan Hirsch
Query 10:  show the earliest and latest date across all flights,
i.e. to have an idea the time span of the database
Write your query and store the result in table span_date.
*/

DROP TABLE IF EXISTS span_date;
CREATE TABLE span_date(
    earliest timestamptz,
    latest timestamptz
);

INSERT INTO span_date
SELECT MIN(actual_departure), MAX(scheduled_departure)
FROM bookings.flights
;

--SELECT * FROM span_date;

/*
Test code
SELECT MAX(book_date)
FROM bookings
;
SELECT MIN(book_date)
FROM bookings.bookings
;
SELECT book_date
FROM bookings
ORDER BY book_date
LIMIT 10;

DROP TABLE span_date;
CREATE TABLE span_date(
    earliest int,
    latest int
);

*/