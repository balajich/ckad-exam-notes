# Run MySQL database in docker container and load classicmodel database
```bash
# Run the mysql database in a docker container
docker run -d --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=classicmodels -p 3306:3306  mysql:5.7
# Copy the classicmodels.sql file to the container
docker cp classicmodels.sql mysql-db:/classicmodels.sql
# Load the classicmodels database
docker exec -i mysql-db mysql -uroot -proot classicmodels < classicmodels.sql
# Fetch all the tables in the classicmodels database
docker exec -i mysql-db mysql -uroot -proot -e "show tables" classicmodels
# Drop the classicmodels database
docker exec -i mysql-db mysql -uroot -proot -e "drop database classicmodels"
# Stop the mysql-db container
docker stop mysql-db
# Remove the mysql-db container
docker rm mysql-db
```
# Run python application that reads customers table from classicmodels database
-Prerequisite
```
cd C:\github\ckad-exam-notes\misc\app
set PYTHONHOME=C:\soft\python-3.9.13
set PATH=%PYTHONHOME%;%PYTHONHOME%\Scripts;%PATH%
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
```bash
python app.py
```
- Access the application customers at http://localhost:5000/customers

# Run the python application and database in docker containers using docker-compose
```bash
cd C:\github\ckad-exam-notes\misc\app
docker-compose up --build
```
- Access the application customers at http://localhost:5000/customers
# References
- Download classicmodels database from [classicmodels.sql](https://raw.githubusercontent.com/josephmuli/ckad-exam-notes/main/misc/classicmodels.sql)