-- Create the hbnb_dev_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user with the password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant SELECT privileges on the performance_schema database to the 'hbnb_dev' user at the 'localhost' host.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;