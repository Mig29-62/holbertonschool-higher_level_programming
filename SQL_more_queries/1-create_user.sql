-- we use CREATE command to create user and GRANT to grant priveleges to certain user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY  'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'usexr_0d_1'@'localhost'; 
FLUSH PRIVILEGES;
