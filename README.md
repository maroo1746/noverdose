# noverdose

## Project Overview

Our project consists of two main functionalities:

### User Side:
- Users are able to search for contraindicated drugs.

### Admin Side:
- Verified administrators have the ability to add drug information into the database (we named this table `med`, which is part of the `med_db`).


## Setup Process

Follow these steps to set up the project using Docker:


### 1. Clone the Repository
Before building the project with Docker, create an empty folder and clone the repository:

```
git clone https://github.com/maroo1746/noverdose.git
```


### 2. Pull Docker Images
Navigate to the noverdose folder within the cloned directory and pull the two required Docker images:

*Web Image*
```
docker pull seoyeong4700/mediforbidden_web:latest
```
*DB Image*
```
docker pull seoyeong4700/mysql:8.0
```


### 3. Docker Compose
Execute the following command in the directory containing the Dockerfile and docker-compose.yml :
```
docker-compose up
```
* Note : You will encounter some errors at this step. Please follow the rest of our step. 



### 4. Go into the Container
When you perform docker-compose up, two images will run creating two containers that are linked. Leave the two containers running and open a new command line to enter the bash shell inside the container. We have two containers - 'web container and db container. 

Follow the command to enter the bash shell of the web container. (Check the name of the web container before running it using the command ‘docker ps’. The name of the container of the image named 'mediforbidden-web' with the image tag 'latest' is the name of the web container.)

```
docker exec -it [container ID or name] /bin/bash
```
After entering the bash shell inside the web container, follow these two steps:

### 4-1. Create a superuser
Please create an admin account that you will use on the ‘http://127.0.0.1:8000/login/’ page.
```
python manage.py createsuperuser
```

### 4-2. Compile the med_db.c file
Compile the med_db.c file to create a shared object file named med_db.so in the /app/libs/ directory.
```
gcc -shared -o /app/libs/med_db.so -fPIC /app/libs/med_db.c -lmysqlclient
```

After completing all the steps, press CTRL + C to stop the containers and then use the command docker-compose down to remove the containers.
```
docker-compose down
```


### 5. Execute 'docker-compose up' again
Afterwards, if you run docker-compose up, you can view our webpage by going to http://127.0.0.1:8000.

If you encounter additional errors, refer to 6. Appendix to check if that covers your case.


## 6. Appendix : additional errors


### 6-1. mysql-client not available
If you face error message like :
`````
7.910 Package libmysqlclient-dev is not available, but is referred to by another package.
7.910 This may mean that the package is missing, has been obsoleted, or
7.910 is only available from another source
7.910 However the following packages replace it:
7.910   libmariadb-dev-compat libmariadb-dev
7.910
7.910 Package mysql-client is not available, but is referred to by another package.
7.910 This may mean that the package is missing, has been obsoleted, or
7.910 is only available from another source
7.910
7.912 E: Package 'libmysqlclient-dev' has no installation candidate
7.912 E: Package 'mysql-client' has no installation candidate
------
failed to solve: process "/bin/sh -c apt-get update && apt-get install -y     python3-pip     gcc     libmysqlclient-dev     mysql-client && apt-get clean" did not complete successfully: exit code: 100
`````

Please follow the additional steps : 
1. change the Dockerfile's line 8 to line 12 with
   `````
    RUN apt-get update && apt-get install -y \
      gcc \
      libmariadb-dev-compat \
      libmariadb-dev && \
      apt-get clean && rm -rf /var/lib/apt/lists/*
   `````
2. Run the docker images again
   ```
   docker-compose up
   ```
3. Go into the web container and compile the med_db.c to create a shared object file named med_db.so
   ```
   docker exec -it [web container's ID or name] /bin/bash
   ```

   ```
   gcc -shared -o /app/libs/med_db.so -fPIC /app/libs/med_db.c -lmariadb
   ```

### 6-2. wait-for-it.sh
If the Docker log shows that there is no permission for wait-for-it.sh, grant permission to wait-for-it.sh with the following command:

1. Go into the web container
   ```
   docker exec -it [web container's ID or name] /bin/bash
   ```
2. grant permission of wait-for-it.sh
   ```
   chomd +x wait-for-it.sh
   ```

   
