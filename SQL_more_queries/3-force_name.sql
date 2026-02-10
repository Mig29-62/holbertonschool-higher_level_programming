-- we use CREATE TABLE to create the table and also add elements.COMMENT is used to add comment specified by per Holberton task rules.
USE DATABASE "$1";
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL,
	) COMMENT ='table for holberton';
