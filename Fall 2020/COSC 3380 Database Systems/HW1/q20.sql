/*
 Jonathan Hirsch
 Query 20:  show total money amount of all booked tickets in one month (august).
Write your query and store the result in table total_money.
*/

DROP TABLE IF EXISTS total_money;
CREATE TABLE total_money(
    money numeric(13,2)
);

INSERT INTO total_money
SELECT SUM(total_amount)
FROM bookings.bookings
WHERE EXTRACT(MONTH FROM book_date) = 8
;

--SELECT * FROM total_money;


