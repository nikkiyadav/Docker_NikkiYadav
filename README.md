# Flask and Express Application – Docker Assignment

## 1. Project Overview

This project demonstrates how to containerize a Python Flask backend and a Node.js Express frontend using Docker and deploy both services on a single environment using Docker Compose.

The application allows users to enter student details through a web form. The Express frontend communicates with the Flask backend, which processes the submitted data and stores it in MongoDB Atlas.

## 2. Technologies Used

- **Python** – Backend programming language
- **Flask** – Backend web framework
- **Node.js** – JavaScript runtime
- **Express.js** – Frontend web server
- **Docker** – Application containerization
- **Docker Compose** – Multi-container application management
- **MongoDB Atlas** – Cloud database
- **Git and GitHub** – Source code version control
- **Docker Hub** – Container image hosting

## 3. Project Architecture

The application contains two Docker containers:

1. **Express Frontend**
   - Runs on port `3000`
   - Displays the student registration form
   - Forwards form submissions to the Flask backend

2. **Flask Backend**
   - Runs on port `5000`
   - Processes submitted student details
   - Stores data in MongoDB Atlas

### Application Flow

Browser → Express Frontend → Flask Backend → MongoDB Atlas

Docker Compose manages both application containers and enables communication between them through the service name `backend`.

## 4. Project Structure

```text
Docker_NikkiYadav/
│
├── backend/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   ├── mangodb_app.py
│   └── templates/
│       ├── form.html
│       └── success.html
│
├── frontend/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── package.json
│   ├── package-lock.json
│   ├── server.js
│   └── public/
│       ├── index.html
│       └── style.css
│
├── docker-compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## 5. Prerequisites

Install the following before running the project:

- Docker Desktop
- Git
- MongoDB Atlas account and database connection URI

## 6. Environment Configuration

Create a `.env` file inside the `backend` folder.

Add your MongoDB connection string:

```env
MONGODB_URI=your_mongodb_connection_string
```

Replace the placeholder with your own MongoDB Atlas URI.

**Important:** Never upload the `.env` file or database credentials to GitHub.

## 7. Run the Application Using Docker Compose

Open PowerShell in the project root directory.

### Step 1: Build the Docker images

```powershell
docker compose build
```

### Step 2: Start both containers

```powershell
docker compose up -d
```

### Step 3: Check running containers

```powershell
docker ps
```

Both frontend and backend containers should be running.

### Step 4: Access the application

Open the following URL in your browser:

**http://localhost:3000**

Submit the student form to test the application and database integration.

### Step 5: Stop the containers

```powershell
docker compose down
```

## 8. Docker Hub Images

The following Docker images have been successfully published:

| Service | Docker Hub Image |
|---|---|
| Flask Backend | `nyadav234/flask-backend:latest` |
| Express Frontend | `nyadav234/express-frontend:latest` |

Docker Hub repositories:

- [Flask Backend Image](https://hub.docker.com/r/nyadav234/flask-backend)
- [Express Frontend Image](https://hub.docker.com/r/nyadav234/express-frontend)

## 9. GitHub Repository

Source code is available here:

[Docker_NikkiYadav – GitHub](https://github.com/nikkiyadav/Docker_NikkiYadav)

## 10. Learning Outcomes

Through this assignment, the following concepts were implemented:

- Created Dockerfiles for Flask and Express applications.
- Built Docker images for both services.
- Used Docker Compose to manage multiple containers.
- Configured communication between frontend and backend containers.
- Connected the Flask backend to MongoDB Atlas.
- Tested the application through the browser.
- Published Docker images to Docker Hub.
- Managed and published source code using Git and GitHub.
- Used `.dockerignore` and `.gitignore` to exclude unnecessary files and sensitive configuration.

---

**Assignment:** Docker – Containerization of Flask and Express Applications

**Author:** Nikki Yadav
