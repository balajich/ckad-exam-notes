# Application Environment Configuration and Security
- Discover and use resources that extended Kubernetes (CRD, Operators)
# Create & consume Secrets
- 6-pod-definition.yml—create a database details secret and use it in pod that has python app and mysql db containers are running
- 7-pod-definition.yml—create a database details secret and mount it as volume in python app container
# Security
- Run a docker container in host pid namespace so that it can interact with host processes
```bash
docker run -it --pid=host --cap-add=SYS_ADMIN ubuntu /bin/sh
```