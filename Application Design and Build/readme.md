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
- **Define** the Image in the Dockerfile
- Please refer the Dockerfile (Dockerfile-Python-App0) in the current directory. 
- **Build** the Image
```bash
docker build -t python-app0 -f Dockerfile-Python-App0 .
```
- **Run** the Image
- By default, the application port is not exposed to the host machine. So, we need to expose the port.
- The application is running on port 5000. So, we need to map the port 5000 of the container to the port 5000 of the host machine.
- The application is running in the background. So, we need to run the container in the detached mode.
```bash
docker run -d -p 5000:5000 python-app0
```