-- SQL script that lists the number of records with the same score, group them in Descending order
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
