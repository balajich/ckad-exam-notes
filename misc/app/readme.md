# Python application that uses MySQL Database
# Pre-requisite
# Build the docker images
```bash
cd C:\github\ckad-exam-notes\misc\app
# Build mysql image
docker build -f Dockerfile-MySQL-DB -t balajich/mysql-db:latest .
# Build Python image
docker build -f Dockerfile-Python-App -t balajich/python-app:latest . 
```
# Run the docker containers
```bash
# Run the mysql container
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=rootpass -p 3306:3306 -d balajich/mysql-db:latest
# Run the python container and link it to mysql container
docker run --name python-app -e MYSQL_HOST=mysql-db -e MYSQL_PASSWORD=rootpass -e MYSQL_DB=classicmodels --link mysql-db:mysql-db -p 5000:5000 -d balajich/python-app:latest
```
# Delete the docker containers
```bash
docker stop python-app mysql-db
docker rm python-app mysql-db
```
# Build and Run the docker containers using docker-compose
```bash
docker-compose up --build -d 
```
# Publish the images to docker hub
## Tag the docker images
```bash
docker tag balajich/mysql-db:latest balajich/mysql-db:latest
docker tag balajich/python-app:latest balajich/python-app:latest
```
## Login to docker hub
```bash
docker login
```
## Push the images to docker hub
```bash
docker push balajich/mysql-db:latest
docker push balajich/python-app:latest
```
# Run the docker containers in a pod in Kubernetes
## Start minikube using the docker driver
```bash
minikube start --driver=docker
```
## Deploy application to Kubernetes cluster
```bash
kubectl apply -f pod-definition.yml
```
## access the application
http://localhost:5000/customers