# midterm-exam

## Features

- Retrieve all users
- Retrieve a specific user by ID
- Create a new user
- Update an existing user
- Delete a user

Before you can run or deploy this application, you'll need to have the following components installed on your system:

## Prerequisites

Before you can run or deploy this app, you need to have the following installed:

- Python 3.x
- pip (Python package manager)
- Flask (`pip install Flask`)
- gunicorn (`pip install gunicorn`)
- Azure CLI (optional, for deployment)

## Project Structure

- app.py: Main Flask application 
- requirements.txt: List of Python dependencies 
- test.http: Test the REST API using the REST Client extension in Visual Studio Code
- README.md: Documentation

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/OseenMarcelino/midterm-exam
   
2. Navigate to the project directory:
   ```bash
   cd midterm-exam
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
5. The API will be running at http://127.0.0.1:8000
6. Use **test.http** to test the REST API using the REST Client extension in Visual Studio Code.
