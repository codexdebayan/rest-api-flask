# **Rest-Api-Flask**

This project is a REST API built with Flask and MySQL, containerized using Docker, and automated with GitHub Actions.

## **Features**

- CRUD operations for managing customers
- MySQL database integration
- Containerized with Docker
- CI/CD with GitHub Actions

## **Prerequisites**

- Docker & Docker Compose
- Python 3.8+
- Git

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/codexdebayan/Rest-Api-Flask.git
   cd Rest-Api-Flask
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```
3. Access the application at http://localhost:5000.

## Project Structure
* app/: Flask application files
* Dockerfile: Docker configuration for Flask app
* docker-compose.yml: Docker Compose setup for Flask and MySQL
* tests/: Unit tests for the application
* .github/workflows/: GitHub Actions CI/CD pipeline

## Usage

* List customers: GET /customers
* Get details of a particular customer : GET /customer/{id}
* Add a customer: POST /customers
* Update a customer: PUT /customers/{id}
* Delete a customer: DELETE /customers/{id}

## CI/CD
This project uses GitHub Actions for continuous integration and deployment. Each push triggers automated testing and deployment.

## Database Setup
To ensure compatibility with MySQL, the root user is configured with mysql_native_password. To set this up manually:

```sql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
```
## Environment Variables
Ensure to set the following environment variables:

* SQLALCHEMY_DATABASE_URI: Set to connect Flask with MySQL.

### Example:
```bash
export SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@customer_db:3306/customer_db'
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
