# DOCKER Commands

---

docker version 			<---- check intalled docker version

---

docker login			<---- login to docker hub 

---

docker pull <image_name>		<----- pulling image from docker hub

---

docker run --name app1 -p 80:8080 -d <image_name> 		<---- running container from the pulled image.

---

docker ps 				<---- to check the running container

---

docker ps -a			<---- to check all the containers including the stopped ones.

---

docker exec -it <container-name> /bin/bash 		<--- logging into the container with a specific shell.

---

docker start <container-name>		<--- Start a stopped container.

---

docker stop <container-name>		<--- stop a container.

---

docker rm <container-name>			<--- remove a container(stop first).

---

docker images				<--- to check the list of images.

---

docker rmi					<--- to remove the pulled images.

---

docker build -t <<your-docker-hub-id>>/<image_name>:v1   <--- build a dockerfile to create a docker image.

---

#Sample docker file. Dockerfile

FROM openjdk:8-jdk-alpine

VOLUME /tmp

EXPOSE 8080

ADD target/*.jar app.jar

ENTRYPOINT [ "sh", "-c", "java -jar /app.jar" ]

---

docker tag <your-docker-hub-id>/mynginx_image1:v1 <your-docker-hub-id>/mynginx_image1:v1-release

---

docker push <your-docker-hub-id>/mynginx_image1:v1-release

---
