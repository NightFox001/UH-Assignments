/*
 Jonathan Hirsch
Query 19:  show names and # of rows of all tables in descending order.
Write your query and store the result in table top_table.
*/

DROP TABLE IF EXISTS top_table;
CREATE TABLE top_table(
    table_name text,
    total_rows int
); 
-- the following code is modified from https://dataedo.com/kb/query/postgresql/list-of-tables-by-the-number-of-rows
INSERT INTO top_table
SELECT c.relname AS table_names,
       c.reltuples AS ROWS
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE  c.relkind = 'r'
      AND n.nspname NOT IN ('information_schema','pg_catalog')
        AND n.nspname = 'bookings'
            AND c.relname IN (
                SELECT TABLE_NAME
                FROM information_schema.tables
                WHERE table_schema = 'bookings'
            )
ORDER BY c.reltuples DESC;


--select * from top_table;
/*
--
SELECT TABLE_NAME
FROM information_schema.tables
WHERE table_schema = 'bookings'
;

SELECT TABLE_NAME.TABLE_ROWS
FROM airbus,
     information_schema.tables
WHERE table_schema = 'bookings'
GROUP BY TABLE_NAME
ORDER BY table_name
;

SELECT TABLE_NAME, COUNT(COLUMN_NAME)
FROM (
         SELECT information_schema.tables.TABLE_NAME
         FROM information_schema.tables
         WHERE information_schema.tables.table_schema = 'bookings'
         GROUP BY information_schema.tables.table_name
     ) AS tablesRows
limit 50
*/


