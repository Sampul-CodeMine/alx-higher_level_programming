-- SQL script to create a DB in the MySQL DB

-- Creating the DB if it does not exist
CREATE SCHEMA IF NOT EXISTS `hbtn_0d_usa`;

-- Creates a table if not existing and assign fields to the table
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL,
	UNIQUE(`id`)
);
