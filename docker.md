# Import docker commands
- Run an ubuntu container
```bash
docker run ubuntu
```
- List all the running containers
```bash
docker ps
```
- List all the containers including the stopped ones
```bash
docker ps -a
```
- Run a sleep command inside ubuntu container
```bash
docker run ubuntu sleep 5
```
- Create a customer docker container called ubuntu-sleeper that sleeps for 5 seconds
```dockerfile
FROM ubuntu
CMD ["sleep", "5"]
```
- Build the above docker file to create a docker image with the name ubuntu-sleeper
```bash
docker build -t ubuntu-sleeper .
```
- Run the above docker container
```bash
docker run ubuntu-sleeper
```
- By default, ubuntu docker container will run bash command, let replace it with sleep command
```bash
docker run ubuntu sleep 10
```
- In the customer dokcer container, we can override the sleep command to 10 seconds
```bash
docker run ubuntu-sleeper sleep 10
```
- Instead of overriding the command, we can pass arguments to the command with entrypoint
```dockerfile
FROM ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```
- Build the above docker file to create a docker image with the name ubuntu-sleeper
```bash
docker build -t ubuntu-sleeper -f DockerfileWithEntryPoint .
```
- Run the above docker container which will sleep for 5 seconds default
```bash
docker run ubuntu-sleeper
```
- Run the container with 20 seconds sleep
```bash
docker run ubuntu-sleeper 20
```
- Override the entrypoint command with echo command
```bash
docker run --entrypoint echo "Hello world" ubuntu-sleeper 10
```