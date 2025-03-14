# Docker_117

This project is a Django application that allows the management of museum data, including details such as name, city, country, address, contact information, and description. The application is containerized using Docker and includes a PostgreSQL database for storing museum records.

## Features

- **Django Framework**: Built with Django 5.1.7.
- **Django REST Framework**: Provides RESTful APIs for CRUD operations on museums.
- **Dockerized**: The app and database are containerized using Docker for easy setup and deployment.
- **PostgreSQL Database**: Data is stored in a PostgreSQL database running in a Docker container.
- **Environment Variables**: Configuration values such as database credentials are managed via `.env` files.

## API Endpoints

1. **List, Create, Retrieve, Update, Delete Museums**
   - **GET** `/museums/` - List all museums.
   - **POST** `/museums/` - Create a new museum.
   - **GET** `/museums/{id}/` - Retrieve a museum by ID.
   - **PUT** `/museums/{id}/` - Update a museum by ID.
   - **DELETE** `/museums/{id}/` - Delete a museum by ID.

## Requirements

- Docker and Docker Compose installed on your system.
- Python 3.8+ (if you wish to run outside Docker).

## Installation

1. Clone the repository:
   git clone https://github.com/anageguchadze/Docker_117.git
   cd Docker_117
   
Build and start the Docker containers:
docker-compose up --build

Once the containers are up and running, the application should be available at:
Web: http://127.0.0.1:8000/
API Endpoint: http://127.0.0.1:8000/museums/

To create a superuser for Django admin (optional):
docker-compose exec web python manage.py createsuperuser
Configuration

Environment variables are loaded from the .env file located in the project root. You can configure your database settings in the .env file.

Example .env file:
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgresadmin22
Running the Application Without Docker

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt
Set up environment variables in a .env file as shown above.

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Usage
You can interact with the API using tools like curl, Postman, or any HTTP client.

Example: Get a list of all museums
curl -X GET http://127.0.0.1:8000/museums/
Docker Setup
The project is set up with Docker Compose, which simplifies the management of both the Django app and the PostgreSQL database in separate containers.

Web Container: This container runs the Django application.
DB Container: This container runs PostgreSQL for data storage.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to your branch (git push origin feature-branch).
Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
