-- we use CREATE command to create user and GRANT to grant priveleges to certain user
IF 'user_0d_1'@'localhost' NOT EXISTS CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY  'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON '.' TO 'user_0d_1'@'localhost'; 
