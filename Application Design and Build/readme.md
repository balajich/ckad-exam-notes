<!-- TOC -->
* [Prerequisites](#prerequisites)
* [Define, build and modify container images](#define-build-and-modify-container-images)
  * [Define](#define)
  * [Build](#build)
  * [Run](#run)
  * [Modify](#modify)
* [Choose and use the right workload resource (Development, DaemonSet,CronJob, etc.)](#choose-and-use-the-right-workload-resource-development-daemonsetcronjob-etc)
  * [Pods](#pods)
    * [Single Container Pod](#single-container-pod)
    * [Multi Container Pod](#multi-container-pod)
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

![Kubernetes Resources.drawio.png](Kubernetes%20Resources.drawio.png)
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
# The application can be accessed on port assigned by the minikube
# The port number may be different in your case.
curl http://127.0.0.1:53190/
```
### ReplicaSet
- It helps in application high availability.
- Provides load balancing and scaling.
- Makes pod fault tolerant.
- ReplicaSet ensures that a specified number of pod replicas are running at any given time. It is often used to guarantee the availability of a specified number of identical Pods.
- Lets two pods of python-app0 using ReplicaSet.
```bash
kubectl create -f replicaset-def-python-app0.yml
kubectl get replicaset
# You can see two pods of python-app0 are running.
kubectl get pods
minikube service python-app0-service
curl http://127.0.0.1:55775/
```
- Scale the replicaset to 3 pods
```bash
kubectl scale --replicas=3 replicaset python-app0-replicaset
# You can see three pods of python-app0 are running.
kubectl get pods
```
- You can scale the application based on load as well.
- Horizontal Pod Autoscaler to scale the application based on CPU utilization.
- Vertical Pod Autoscaler to scale the application based on memory utilization.
- Custom Metrics Adapter to scale the application based on custom metrics.
- External Metrics Adapter to scale the application based on external metrics.
### Deployment
- It is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features.
- Key features
    - Rollout and Rollback
    - Scaling
    - Pause and Resume
    - Rollout History
    - Deployment Strategies
- Lets deploy the python-app0 using Deployment
```bash
kubectl create -f deployment-def-python-app0.yml
kubectl get deployments
kubectl get replicasets
kubectl get pods
minikube service python-app0-service
```
### DaemonSet
A DaemonSet ensures that a copy of a Pod runs on all (or some) nodes in the cluster. It’s typically used for background tasks like logging, monitoring, or other node-specific services.
Every time a new node is added to a cluster, the pod is added to it, and when a node is removed from the cluster, the pod is removed. When a DaemonSet is deleted, Kubernetes removes all the pods created by it.
- Lets create a python application that checks for the health of websites and logs the status.
```bash
python app2.py
# Build docker image
docker build -t app2 -f Dockerfile-app2 .
# Run the docker image to test the application
docker run  -it app2
# Tag the image
docker tag app2:latest balajich/app2:latest
# Push the image to the docker hub
docker push balajich/app2:latest
```
- Deploy the application as DaemonSet
```bash
kubectl create -f daemonset-def-app2.yml
kubectl get daemonsets
kubectl get pods
# Add a new node
minikube node add
# observe the new pod is created on the new node
kubectl get pods -o wide
```
### Job
- A Job creates one or more Pods and ensures that a specified number of them successfully terminate. As pods successfully complete, the Job tracks the successful completions. When a specified number of successful completions is reached, the task (ie, Job) is complete.
- Lets create a python application that computes pie value and logs the value.
```bash
python app3.py
# Build docker image
docker build -t app3 -f Dockerfile-app3 .
# Run the docker image to test the application
docker run  -it app3
# Tag the image
docker tag app3:latest balajich/app3:latest
# Push the image to the docker hub
docker push balajich/app3:latest
```
- Deploy the application as Job
```bash
kubectl create -f job-def-app3.yml
kubectl get jobs
kubectl get pods
# Check the logs of the pod
kubectl logs app3-job-7z5z2
```