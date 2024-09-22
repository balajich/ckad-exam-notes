<!-- TOC -->
* [Prerequisites](#prerequisites)
* [Define, build and modify container images](#define-build-and-modify-container-images)
  * [Define](#define)
  * [Build](#build)
  * [Run](#run)
  * [Modify](#modify)
* [Choose and use the right workload resource (Development, DaemonSet,CronJob, etc.)](#choose-and-use-the-right-workload-resource-development-daemonsetcronjob-etc)
<!-- TOC -->
# Prerequisites
```bash
cd C:\github\ckad-exam-notes\Application Design and Build
set PYTHONHOME=C:\soft\python-3.9.13
set PATH=%PYTHONHOME%;%PYTHONHOME%\Scripts;%PATH%
# Run the following commands only once
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
# Define, build and modify container images
- Lets us create a simple python rest api using flask and containerize it.
- Run the python application on the host machine.
```bash
# Please run prerequisites before running the following commands
pyton app0.py
```
- To containerize the application, we need to create a Dockerfile.
## Define
- **Define** the Image in the Dockerfile
- Please refer the Dockerfile (Dockerfile-Python-App0) in the current directory.
## Build
- **Build** the Image with name python-app0
```bash
docker build -t python-app0 -f Dockerfile-Python-App0 .
```
## Run
- **Run** the Image
- By default, the application port is not exposed to the host machine. So, we need to expose the port.
- The application is running on port 5000. So, we need to map the port 5000 of the container to the port 5000 of the host machine.
- The application is running in the background. So, we need to run the container in the detached mode.
```bash
docker run -d -p 5000:5000 python-app0
```
## Modify
There are various ways to modify the container image.
- Modify the container image by changing the code in the application, rebuild the image and run the container.
- Modify the container image by running the container in the interactive mode.
- In below example, we will modify the container image by running the container in the interactive mode and install curl in the container.
```bash
# Start the container
docker run -d -it python-app0 /bin/bash
# Get the container id
docker ps
# Take shell access to the container using the container id
docker exec -it 097bbc1918b8 /bin/bash
# The container state is modified by installing curl in the container.
# install curl in the container
apt-get update
apt-get install curl
```
- We can commit the container state to the image with name python-curl-app0.
```bash
docker commit 097bbc1918b8  python-curl-app0
```
- Create a new container with the new image python-curl-app0.
```bash
docker run -d -p 5000:5000 python-curl-app0
# Take the shell access to the container
docker exec -it 76effa2153a2 /bin/bash
# Check the curl is installed in the container
curl --version
```
# Choose and use the right workload resource (Development, DaemonSet,CronJob, etc.)
It is important to choose the right **Kubernetes workload resource** based on the requirement of the application. Some applications can be a simple rest api application, some applications can be a batch processing application, some applications can be a real-time processing application. Based on the requirement of the application, we need to choose the right Kubernetes workload resource.
Following are the different types of Kubernetes workload resources:
- Pod
- ReplicaSet
- Deployment
- StatefulSet
- DaemonSet
- Job
- CronJob
## Pods
- The basic unit of deployment in Kubernetes. A Pod represents a group of one or more containers that share storage and network resources. Use Pods for simple, single-container applications or tightly coupled multi-container applications
### Single Container Pod
- Let's create a pod that run python-app0 container.
- Prerequisites: Let's push the python-app0 image to the docker hub.
```bash
docker tag python-app0:latest balajich/python-app0:latest
# push the image to the docker hub
docker push balajich/python-app0:latest
# start the minikube
minikube start
```
- create the pods
```bash
kubectl create -f pod-def-python-app0.yml
kubectl get pods
```
- access the application
```bash
minikube service python-app0-service
# The application can be accessed on port assigned by the minikube
# The port number may be different in your case.
curl http://127.0.0.1:52668/
```
### Multi Container Pod
- Let's containerize the app1.py and app11.py and run them in the same pod.
-  In this example, app1 is going to call app11 
- Before containerizing the app1.py and app11.py, let's run the app1.py and app11.py on the host machine.
```bash
# Run the app1.py and app11.py on the host machine
python app1.py
python app11.py
# access the application app1.py that internally calls app11.py
curl http://localhost:5000/
```
- Build and publish the app1 and app11 images to the docker hub using docker compose
```bash
docker-compose -f docker-compose-app1-app11.yml build
# tag the images
docker tag app1:latest balajich/app1:latest
docker tag app11:latest balajich/app11:latest
#push the images to the docker hub
docker push balajich/app1:latest
docker push balajich/app11:latest
```
- Deploy the multi-container pod on to minikube
```bash
kubectl create -f pod-def-python-app1.yml
kubectl get pods
minikube service python-app1-service
```