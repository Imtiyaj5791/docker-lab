# Docker Compose Flask + MySQL Project

## 📌 Project Overview

This project demonstrates a simple **2-tier application** using Docker Compose.

- Flask Application (Python)
- MySQL Database
- Docker Compose
- Custom Docker Network
- Named Volume for MySQL data persistence
- Environment Variables for configuration

---

## 🏗️ Architecture

```
                Browser
                    |
                    v
           Flask Application
                    |
           DB_HOST = db
                    |
                    v
           MySQL Container
                    |
                    v
            Named Docker Volume
```

---

## 📂 Project Structure

```
docker-compose-flask-mysql/
│── Dockerfile
│── docker-compose.yml
│── app.py
└── requirements.txt
```

---

## 🚀 Technologies Used

- Docker
- Docker Compose
- Python Flask
- MySQL 8
- Docker Network
- Docker Volume

---

## ⚙️ Build & Run

Build and start containers

```bash
docker compose up -d --build
```

Check running containers

```bash
docker compose ps
```

View logs

```bash
docker compose logs
```

Stop containers

```bash
docker compose down
```

---

## 🌐 Application

Open in browser

```
http://<EC2-Public-IP>:5000
```

Example Output

```
Flask connected successfully with MySQL
```

---

## 📌 Docker Compose Features Used

- Multi-container application
- Dockerfile build
- Environment Variables
- Custom Network
- Named Volume
- depends_on
- Port Mapping

---

## 📚 Learning Outcome

After completing this project I learned:

- Creating custom Docker images
- Building multi-container applications
- Container communication using Docker Compose Network
- Using Environment Variables
- Persisting MySQL data using Docker Volumes
- Connecting Flask application with MySQL

---

## 👨‍💻 Author

**Imtiyaj Ansari**
