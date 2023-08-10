# Simple Book with FastAPI and Alembic

This project provides a simple structure for creating a FastAPI-based web application for managing books, along with Alembic for database migrations. It is designed with beginners in mind and follows a structured folder organization.

## Prerequisites

- Python 3.9
- [Deta](https://deta.space/) account for deployment (optional but recommended)

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/yudhaislamisulistya/book-api-fastapi.git
   cd book-api-fastapi
   ```

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run command for migration database:
   ```bash
   alembic revision --autogenerate
   or
   alembic upgrade head
   ```
4. Run the application locally using the following command:

   ```bash
   uvicorn main:app --reload
   ```

   Or, if you want to use Deta for deployment:

   - Create an account on [Deta](https://deta.space/).
   - Install Deta CLI:

     ```bash
     curl -fsSL https://get.deta.dev/space-cli.sh | sh
     ```

   - Initialize a Deta project and deploy:

     ```bash
     space new
     space push
     ```

   - or Alternative with Space CLI
     ```bash
     space dev
     ```

   - Obtain the token and project ID from Deta and update them in `deploy.yml` for CI/CD setup.

5. Access the application at the following URL (if using Deta):

   ```
   https://bookapi-1-v1905306.deta.app/
   or
   http://localhost:8080/
   ```

6. Access the API documentation at the following URL:

   ```
   https://bookapi-1-v1905306.deta.app/docs
   or
   http://localhost:8080/docs
   ```

## Example Endpoints

Here are some example endpoints that you can use:

### Read Books

**GET** `/api/v1/books/`

Retrieves a list of all books.

### Create Book

**POST** `/api/v1/books/`

Creates a new book.

### Delete Book

**DELETE** `/api/v1/books/{book_id}`

Deletes a book by its ID.

## Schemas

- `BookInput` - Schema for creating a book.
- `BookOutput` - Schema for the book response.

## Project Structure

The project follows this folder structure:

- `.github/workflows` - GitHub Actions workflows
- `alembic` - Alembic database migration scripts
- `app` - Main application code
  - `configs` - Database configuration
  - `controllers` - Controllers for business logic
  - `endpoints` - API endpoints
  - `libs` - Utility libraries (databases and templates)
  - `model` - Database table structures
  - `routes` - API routes
  - `schemas` - Pydantic request and response schemas
  - `tests` - Unit tests
  - `utils` - Additional utility libraries
- `Spacefile` - Deta configuration
- `main.py` - FastAPI application entry point
- `requirements.txt` - Project dependencies

## Contribution

Feel free to contribute to this project by submitting pull requests. Your contributions can help improve and expand this beginner-friendly FastAPI and Alembic structure.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.