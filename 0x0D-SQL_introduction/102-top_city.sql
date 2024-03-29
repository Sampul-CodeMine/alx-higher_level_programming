-- SQL script that displays 3 cities temperature from July to August order by temperature
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` WHERE `month` BETWEEN 7 AND 8
GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
