-- we use CREATE TABLE to create the table and also add elements.DEFAULT is used to put default id value as a condition by holberton task rules.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT DEFAULT 1 UNIQUE PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);
