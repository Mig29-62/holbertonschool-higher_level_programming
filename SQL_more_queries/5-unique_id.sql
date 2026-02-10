-- we use CREATE TABLE to create the table and also add elements.DEFAULT is used to put default id value as a condition by holberton task rules.
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL
	);
