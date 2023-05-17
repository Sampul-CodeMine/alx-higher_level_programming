-- SQL Script that Creates a DB, a table and its fields if they do not exist

-- Creating a Schema
CREATE SCHEMA IF NOT EXISTS `hbtn_0d_usa`;

-- Creating the Table in the Schema
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	UNIQUE(`id`),
	FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
