-- we use CREATE TABLE to create the table and also add elements.DEFAULT is used to put default id value as a condition by holberton task rules.
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
	);
