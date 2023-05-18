# 0x0D. SQL - Introduction

Data is more valuable and in this world of digital development and advancements, most of the activities we do depends on data. For growth measurements, profits, loss, statistical measurements etc, depends on data.

Data can be anything and everything. Data is figure, fact, an information ungrouped elements etc.

At the end of this course we will know about:

### General

- What’s a `Database`
- What’s a `Relational Databases`
- What does `SQL` stand for
- What’s `MySQL`
- How to `create` a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use `MySQL` functions


## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on `Ubuntu 20.04 LTS` using `MySQL 8.0 (version 8.0.25)`
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file:

```shell
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```shell
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

### Connect to your MySQL server:

```shell
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL

In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:

```shell
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

## A Database

A Database can be defined as a container that holds data in an organized and structured way for easy accessibility, addition, manipulation, removal, retrieval, protection and analysis of data and information. Database store these data/information electronically and software used to manage Databases are known as **DBMS (`DataBase Management Systems`)** examples include Oracle, SyBase, MS SQL Server, MySQL, Microsoft Access, SQLite, PostgreSQL, Cassandra etc and these DBMS gives us an inteface to communicate with the DataBase and other application.

Databases are of different types:

- Flat File Database
- Hierachical Database
- Network Database
- Relational Databases
- Non-Retlational Databases

> _Note: The mostly used types of Databases are the **Relational** and **Non-Relational** Databases._
>
> The most widely used Relational Database is **`Oracle`** while the most widely used Non-Relational Database is **`MongoDB`**.

## SQL (Structured Query Language)

Reasons why data are saved in the database are for storage, retrieval, anaylsis, modifications and manipulations. To get information from the database wont be that easy, hence the Language, SQL which is the language used to retrieve, manipulate, set and revoke privileges to/from a database.

SQL Statements for manipulating a DB are classified into:

- DDL - Data Definition Language
- DML - Data Manipulation Language
- Transaction and Locking Statements
- Replication Statements
- Prepared Statements
- Database Administrative Statements
- Utility Statements

## RELATIONAL DATABASES

Relational Databases are DBs that stores data in tabular forms using a row and columns to represent and group data. A `row` represents a `record` while a `column` represents a `field` which is of a specified datatype.
In a Relational Database, `PK - PRIMARY KEY` are used to uniquely identify a record, `FK - FOREIGN KEY` are used to link  2 or more columns within 2 or more tables in a database.

## CREATING A NEW USER

Upon installation, MySQL creates a root user account which you can use to manage your database. This user has full privileges over the MySQL server, meaning it has complete control over every database, table, user, and so on. Because of this, it’s best to avoid using this account outside of administrative functions. This step outlines how to use the root MySQL user to create a new user account and grant it privileges.

To create a new user `sample` on the `localhost` with password `samplepassword` in MySQL,

```bash
$ mysql -u root -p
Enter Password: *********
mysql> CREATE USER 'sample'@'localhost' IDENTIFIED BY 'samplepassword';
```

## GRANTING PRIVILEGES TO NEW USER

After creating your new user, you can grant them the appropriate privileges. Granting all privileges to a user `sample` to all tables in a particular database `test`

```bash
mysql> GRANT ALL PRIVILEGES ON test.* TO 'sample'@'localhost' WITH GRANT OPTION;
```

> _Note: that this statement also includes WITH GRANT OPTION. This will allow your MySQL user to grant any permissions that it has to other users on the system._

## SHOWING THE USERS PRIVILEGES

You can review a user’s current permissions by running the SHOW GRANTS command:

```bash
mysql> SHOW GRANTS FOR 'sample'@'localhost';
```

## DROPPING OR DELETING A USER

Just as you can delete databases with `DROP`, you can use `DROP` to delete a user:

```bash
mysql> DROP USER 'sample'@'localhost';
```

## MYSQL CONSTRAINTS

Constraints are placed on columns or tables. They limit the data that can be inserted into tables.

- `NOT NULL`: A column with a `NOT NULL` constraint, cannot have NULL values.
- `UNIQUE`: The `UNIQUE` constraint ensures that all data are unique in a column.
- `PRIMARY KEY`: The `PRIMARY KEY` constraint uniquely identifies each record in a database table. It is a special case of unique keys. Primary keys cannot be NULL, unique keys can be. There can be more UNIQUE columns, but only one primary key in a table.
- `FOREIGN KEY`: A FOREIGN KEY in one table points to a PRIMARY KEY in another table. It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.
- `ENUM`: An ENUM is a string object with a value chosen from a list of permitted values. They are enumerated explicitly in the column specification at table creation time. `CREATE TABLE Student(Id INTEGER, Name VARCHAR(55), Gender ENUM('Male', 'Female', 'Others'));`
- `SET`: A SET can have zero or more values. Each of the values must be chosen from a list of permitted values. `CREATE TABLE Students(Id INTEGER, Name VARCHAR(55), Certificates SET('A1', 'A2', 'B1', 'C1')); `

## JOINING TABLES

The real power and benefits from relational databases come from joining tables. The `SQL JOIN` clause combines records from two or more tables in a database. There are basically two types of joins: `INNER` and `OUTER`.

### INNER JOIN

The inner join is the most common type of joins. It is the default join also. The inner join selects only those records from database tables that have matching values. We have three types of `INNER JOINS`: 

- INNER JOIN, 
- NATURAL INNER JOIN, and 
- CROSS INNER JOIN. 

> _Note:The `INNER` keyword can be omitted._

### OUTER JOIN

An outer join does not require each record in the two joined tables to have a matching record. There are three types of outer joins. 

- LEFT OUTER JOIN, 
- RIGHT OUTER JOIN

---

> Ehigboria Dukeson Oserefuame [Sampul-CodeMine](https://github.com/Sampul-CodeMine)