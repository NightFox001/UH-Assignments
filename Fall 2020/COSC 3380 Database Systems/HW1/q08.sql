/*
Jonathan Hirsch
 Query 8: list all bookings on aug/4/2017 with cost less than 40,000 
Write your query and store the result in table bookings_date.
*/

DROP TABLE IF EXISTS bookings_date;
CREATE TABLE bookings_date(
    book_ref character(6),
    book_date timestamptz,
    total_amount numeric(10,2)
);

INSERT INTO bookings_date
SELECT  book_ref,
        book_date,
        total_amount
FROM bookings.bookings
GROUP BY book_ref
HAVING DATE(book_date) = 'aug/4/2017' AND total_amount < 40000
;

--SELECT * FROM bookings_date;



/* 
SELECT * 
FROM bookings
WHERE book_date = '2017-08-04'
GROUP BY book_ref
HAVING total_amount < 40000
;
*/