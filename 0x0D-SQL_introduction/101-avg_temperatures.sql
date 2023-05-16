-- SQL script that displays the average temperature (Fah) by city order by temp desc
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
