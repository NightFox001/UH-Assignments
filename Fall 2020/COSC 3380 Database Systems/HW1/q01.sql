/*
Jonathan Hirsch
 Query 1: count distinct and average range for Boeing models
Write your query and store the result in table boeing.
*/

DROP TABLE IF EXISTS boeing;
CREATE TABLE boeing(
    dist_range int,
    avg_range numeric(6,2)
); 

INSERT INTO boeing
SELECT COUNT(DISTINCT range), -- num of boeing models
       AVG(DISTINCT range)  -- avg of the 3 boeing models
FROM bookings.aircraft
WHERE model LIKE '%Boeing%'
;

select * from boeing;

/* 
--These two select statements get the values in two seperate relations
SELECT COUNT(DISTINCT range) AS "dist_range"
FROM aircrafts_data;
SELECT AVG(DISTINCT range) AS "avg_range"
FROM aircrafts_data;

--returns the num of distinct ranges, and the avg of the distinc ranges
--   as one table with two columns
SELECT COUNT(DISTINCT range), AVG(DISTINCT range)
FROM aircrafts_data;
*/