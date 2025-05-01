# Interview Project

This project is a simple REST API built using Python. The API connects to a PostgreSQL database, and asynchronous functionality is optional. You can use any open-source PostgreSQL provider, such as NeonDB.

## Features
- REST API using Python
- PostgreSQL database integration or any database.
- Optional asynchronous functionality
- Optional poetry if you are comfortable
- ORM tools would be nice.
- RUN_README for setup and running would be nice.

## Getting Started
1. Clone the repository.
2. Set up a PostgreSQL database (e.g., NeonDB).
3. Install the required dependencies.
4. Run the API server.

## Requirements
- Python >= 3.9+
- PostgreSQL database or any RDBMS or NoSQL (e.g., NeonDB)
- At least one POST method to create a record in the DB.
- Simple unit test.
- Create a PR from this repo.

## Running the FastAPI App Locally

1. Make sure you have installed all dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server using Uvicorn or Hypercorn:
   ```bash
   # Using Uvicorn (recommended for FastAPI)
   uvicorn main:app --reload
   # Or using Hypercorn
   hypercorn main:app --reload
   ```
   - The `--reload` flag enables auto-reload on code changes (useful for development).
   - By default, the app will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. Access the Swagger (OpenAPI) documentation:
   - Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the interactive Swagger UI.
   - You can use this interface to test API endpoints and view request/response schemas.
   - For the raw OpenAPI JSON schema, visit [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json).

## Running Tests Locally

This project uses [pytest](https://pytest.org/) for testing.

1. Make sure you have installed all dependencies (including pytest):
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests from the project root directory:
   ```bash
   pytest
   ```
   - If you encounter import errors, set the PYTHONPATH environment variable:
     ```bash
     PYTHONPATH=. pytest
     ```

- All test files are located in the `interview/tests/` directory.
- Test results will be shown in the terminal.

