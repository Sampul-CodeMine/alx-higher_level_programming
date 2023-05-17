-- SQL script that creates a DB and a user assigned to the DB

-- Creating the DB if not exist
CREATE SCHEMA IF NOT EXISTS `hbtn_0d_2`;

-- Create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Assign privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
