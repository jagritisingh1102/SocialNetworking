# Social Networking Application API

This repository contains the backend API for a social networking application built using Django Rest Framework (DRF). The API provides various functionalities for user management and social interactions.

## Table of Contents

- [Installation](#installation)
  - [Without Docker](#without-docker)
  - [With Docker](#with-docker)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Postman Collection](#postman-collection)

## Installation

Choose one of the following methods to set up and run the project:

### Without Docker

#### Prerequisites

- Python 3.x and pip
- Django and Django Rest Framework

#### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd social_network

2. **Set up a virtual environment:** 
   1. On macOs/Linux
       ```bash
      python -m venv venv
      source venv/bin/activate

   2. On Windows
      ```bash
      python -m venv venv
      venv\Scripts\activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create Superuser (for admin access):**
    ```bash
    python manage.py createsuperuser

6. **Run the development Server:**
    ```bash
    python manage.py runserver

7. **Access the API:**
    Navigate to http://localhost:8000/api/ to view the API root.
    

### With Docker

#### Prerequisites

- Docker and Docker Compose


#### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd social_network

2. **Build and run Docker containers:**
    ```bash
    docker compose up --build
This command will build your Docker images based on the Dockerfile and start the containers defined in docker-compose.yml. The Django development server will be accessible at http://localhost:8000.

3. **Access the Docker Container (optional):**
    ```bash
    docker compose exec web bash
This command opens a bash session in your web service container, where you can run Django management commands (python manage.py migrate, python manage.py createsuperuser, etc.) and interact with your Django project.


## Usage

### API Endpoints

1. **User Authentication**
   1. POST /api/login/: User login endpoint.
   2. POST /api/signup/: User signup endpoint.

2. **User Management**
   1. GET /api/users/search/?search=<query>: Search users by username or email.
   2. POST /api/send-friend-request/: Send a friend request. 
   3. POST /api/accept-friend-request/<request_id>/: Accept a friend request. 
   4. POST /api/reject-friend-request/<request_id>/: Reject a friend request. 
   5. GET /api/friends/: List of accepted friends. 
   6. GET /api/pending-requests/: List of pending friend requests.


### Authentication

1. Authentication credentials are required for most API endpoints.
2. Use the Authorization header with a token obtained from the login endpoint.


### Postman Collection

For easy testing and reference, download the Postman collection containing API endpoints:

https://drive.google.com/file/d/10nmz55rkk7qrrpVFaG1bqfHYLrzALsFH/view?usp=drive_link

Import this collection into Postman to start testing the API endpoints immediately.