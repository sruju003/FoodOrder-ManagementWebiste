--The users of the project
--USers and admin : Here user is customer and admin is the one handling orders

--foodAdmin : password - 'password'
CREATE USER 'foodAdmin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'foodAdmin'@'localhost' IDENTIFIED BY 'password';

--foodCust : password - NONE
CREATE USER 'foodCustomer'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'foodCust'@'localhost' IDENTIFIED BY 'password';
