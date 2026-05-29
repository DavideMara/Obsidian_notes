# Docker & Docker Compose

---

## 1. What is Docker?

Docker is a containerization platform that allows developers to package applications and all their dependencies (libraries, system tools, and code) into a single, standardized unit called a **Container**.

### Key Concepts

*   **Image**: A read-only template containing the instructions to build a container. Think of it as a blueprint or class in OOP.
*   **Container**: A runnable instance of an image. It is isolated from the host machine and other containers. Think of it as an object/instance in OOP.
*   **Dockerfile**: A text document containing all the commands a user could call on the command line to assemble an image.
*   **Docker Compose**: A tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services.

---

## 2. Project Dockerfile Breakdown

Here is the code inside your [Dockerfile](file:///home/davide/Coding/repos/ingsw_25-26_group-13/Dockerfile):

```dockerfile
FROM maven:3.8.8-eclipse-temurin-17 AS dev
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
CMD ["mvn", "clean", "test"]
```

### Explanation of Each Instruction

1.  **`FROM maven:3.8.8-eclipse-temurin-17 AS dev`**
    *   **Base Image**: This tells Docker to start building your image using an official Maven image preloaded with Eclipse Temurin JDK 17.
    *   **Multi-Stage Build (`AS dev`)**: It labels this compilation stage as `dev` so it can be targeted by Docker Compose.
2.  **`WORKDIR /app`**
    *   Sets the working directory inside the container to `/app`. All subsequent commands (`COPY`, `RUN`, `CMD`) will execute relative to this directory.
3.  **`COPY pom.xml .`**
    *   Copies the `pom.xml` from your local machine (the build context) into the container's `/app` folder. We copy the dependencies description first to leverage Docker's layer caching.
4.  **`RUN mvn dependency:go-offline -B`**
    *   Downloads all the required Maven plugins and dependencies inside the container before copying the actual source code. If `pom.xml` does not change, Docker caches this layer, saving time on subsequent builds. The `-B` flag runs Maven in non-interactive batch mode.
5.  **`COPY src ./src`**
    *   Copies your actual application source code from your local machine's `./src` folder to `/app/src` inside the container.
6.  **`CMD ["mvn", "clean", "test"]`**
    *   Defines the default command that runs automatically when the container starts up. In this case, it executes the unit tests using Maven.

---

## 3. Project docker-compose.yml Breakdown

Here is the code inside your [docker-compose.yml](file:///home/davide/Coding/repos/ingsw_25-26_group-13/docker-compose.yml):

```yaml
services:
  db:
    image: mysql:8.0
    container_name: transport-db-container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "Admin123."
      MYSQL_DATABASE: "transport_db"
      MYSQL_USER: "user_app"
      MYSQL_PASSWORD: "useruser123"
    ports:
      - "3306:3306"
    volumes:
      - ./sql:/docker-entrypoint-initdb.d

  app:
    build:
      context: .
      target: dev
    container_name: transport-app-container
    volumes:
      - .:/app
      - maven_target:/app/target
      - ~/.m2:/root/.m2
    depends_on:
      - db
    command: mvn clean test

volumes:
  maven_target:
```

### Explanation of Each Service

### `db` Service (MySQL Database)
*   **`image: mysql:8.0`**: Runs an official MySQL version 8 container.
*   **`container_name: transport-db-container`**: Gives the container a specific name instead of a randomly generated one.
*   **`restart: always`**: Automatically restarts the container if it stops or crashes.
*   **`environment`**: Sets environment variables that configure MySQL, defining the credentials and the database named `transport_db`.
*   **`ports: - "3306:3306"`**: Maps port `3306` from your host machine to port `3306` inside the container, allowing you to connect to the database from external database managers (like DBeaver or IntelliJ).
*   **`volumes: - ./sql:/docker-entrypoint-initdb.d`**: Mounts your local `./sql` directory to a special initialization directory inside the MySQL container. MySQL runs any `.sql` scripts found here upon container creation to initialize tables and schemas.

### `app` Service (Java Maven Application)
*   **`build`**: Instructs Docker Compose to build the image using the local `Dockerfile` in the current directory (`context: .`) using the target stage `dev`.
*   **`volumes`**:
    *   `.:/app`: Mounts the project root folder on the host to `/app` inside the container. This enables live code updates (changes in the host immediately reflect inside the container).
    *   `maven_target:/app/target`: Mounts a named volume (`maven_target`) to `/app/target`. This prevents Maven compiled class files from being written back to your host machine, avoiding permission issues and file locks.
    *   `~/.m2:/root/.m2`: Mounts your local `~/.m2` folder into the container to reuse dependencies already cached on your host machine, speeding up Maven builds.
*   **`depends_on: - db`**: Tells Docker to start the `db` container before launching the `app` container.
*   **`command: mvn clean test`**: Overrides the Dockerfile `CMD` to execute unit tests.

---

## 4. Useful Commands for Your Exam

*   `docker compose up`: Starts the services in the foreground.
*   `docker compose up -d`: Starts the services in detached (background) mode.
*   `docker compose down`: Stops the running containers and removes networks created by compose.
*   `docker compose down -v`: Stops containers and also deletes the named volumes (resetting database state).
*   `docker compose logs -f <service_name>`: Tails logs of a specific container (e.g., `docker compose logs -f db`).