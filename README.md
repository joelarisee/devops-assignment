# DevOps Assignment 2: AWS Compute, Networking & Database Integration

This repository contains a lightweight REST API built with Python (FastAPI). It is containerized using Docker and deployed securely to an AWS EC2 instance, with a connection to an AWS RDS PostgreSQL database.

## Live Deployment
**Public API URL:** `http://3.25.86.170`

## Prerequisites
To run this application, the host system must have the following installed:
- Docker
- Docker Compose
- Git

## How to Run the Application

### 1. Set Environment Variables
The application dynamically reads database credentials from the host system's environment variables to ensure no secrets are hardcoded. Before starting the application, export the following variables in terminal:

```bash
export DB_HOST="<YOUR_RDS_ENDPOINT>"
export DB_PORT="5432"
export DB_NAME="postgres"
export DB_USER="postgres"
export DB_PASSWORD="<YOUR_DB_PASSWORD>"
```

### 2. Run with Docker Compose
Once the environment variables are set, build and start the container in the background using Docker Compose:

```bash
# The -E flag ensures sudo preserves the exported environment variables
sudo -E docker-compose up -d --build
```

## API Endpoints & Testing
The API endpoints are secured and only accept requests containing the header `Authorization: pay3-assignment`.

### Create an Entry (POST)
To create a new entry in the RDS database, run the following cURL command:

```bash
curl -X POST "http://3.25.86.170/items/?name=devops&value=assignment_completed" -H "Authorization: pay3-assignment"
```

### Fetch All Entries (GET)
To retrieve all saved entries from the RDS database, run:

```bash
curl -X GET "http://3.25.86.170/items/" -H "Authorization: pay3-assignment"
```

## Proof of Execution

1. **Screenshot of successful POST (Write) Request:**
    <img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/2e2f47ba-2749-4739-b6bb-59ab97f4f8f8" />

2. **Screenshot of successful GET (Read) Request:**
   ``<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/4f4ee137-6805-401c-9b33-4e67b66880f4" />


