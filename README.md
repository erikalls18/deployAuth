# deployAuth

## Description

This web application is built with FastAPI and provides an API for managing users and authentication. It enables querying a PostgreSQL database and retrieves JSON Web Tokens (JWT) for secure access. The application uses Docker Compose to build an image for the API and creates two containers: one for the FastAPI application and another for the PostgreSQL database.

## Features
- **RESTful API**: Interface for interacting with data.
- **PostgreSQL Database**: Persistent data storage.
- **User Authentication**: Secure user management with tokens.
- **Admin Interface**: Adminer for database management.

## Requirements

- Docker
- Docker-compose
- Create a .env file to store secrets and algorithm configurations.


## Installation

- Clone the repository
- Grant execute permission to the wait_for_it.sh file
- buil the aplication with docker compose build 
- Start  the application with docker-compose up

