-- prepare  posetgres
-- dev Environment
CREATE DATABASE learningmate_dev;
CREATE USER learningmate_user WITH PASSWORD 'learningmate_123';
GRANT ALL PRIVILEGES ON DATABASE learningmate_dev TO learningmate_user;
