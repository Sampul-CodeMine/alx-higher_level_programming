-- SQL script to create a table unique_id on the MySQL Server
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
