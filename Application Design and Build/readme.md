<!-- TOC -->
* [Prerequisites](#prerequisites)
* [Define, build and modify container images](#define-build-and-modify-container-images)
  * [Define](#define)
  * [Build](#build)
  * [Run](#run)
  * [Modify](#modify)
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
- We can modify the container image by changing the code in the application.
- We can rebuild the image and run the container.
- We can also modify the container image by running the container in the interactive mode.
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