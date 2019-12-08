#use these commands on you terminal
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo su - postgres
psql
CREATE DATABASE rate;
CREATE USER rate_user WITH PASSWORD 'root';
ALTER ROLE rate_user SET client_encoding TO 'utf8';
ALTER ROLE rate_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE rate_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE rate TO rate_user;

#use this command after activating your environment
pip install django psycopg2
