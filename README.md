# My Inventory Management System – Backend

---

## Quick Start

### Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the server
```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## Overview

This project is the backend for My Inventory Management System built using Django and Django REST Framework.

It provides a RESTful API that handles authentication, business logic, and data storage for inventory management.

The system allows users to:
- Register and log in securely
- Manage inventory items (CRUD operations)
- Categorise items
- Track stock changes
- View stock history (audit logs)

---

## Architecture

The system follows a three-layer architecture based on what was provided in the assigment brief:

### Frontend (React)
Handles UI and user interaction.

### Backend (Django REST API)
Handles:
- Authentication
- Business logic
- Validation
- API endpoints

### Database (PostgreSQL)
Stores:
- Users
- Items
- Categories
- Stock logs

The frontend communicates with the backend via API endpoints only.

---

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Python Decouple (environment variables)

---

## Authentication

Authentication is implemented using JWT (JSON Web Tokens).

### Endpoints

Register:
```
POST /api/register/
```

Login:
```
POST /api/token/
```

Refresh token:
```
POST /api/token/refresh/
```

### Features

- Secure password hashing
- Token-based authentication
- Protected API endpoints
- User-specific data access

---

## Database Models

### Item
Represents an inventory item.

Fields include:
- name
- description
- quantity
- category
- owner (user)
- timestamps

---

### Category
Used to group inventory items.

---

### StockLog
Tracks stock changes over time.

Fields include:
- item
- change amount (+ / -)
- user
- timestamp

This supports audit history and traceability.

---

## API Endpoints

### Items

```
GET    /api/items/
POST   /api/items/
GET    /api/items/<id>/
PUT    /api/items/<id>/
DELETE /api/items/<id>/
```

---

### Categories

```
GET    /api/categories/
POST   /api/categories/
```

---

### Stock Logs

```
GET /api/stock-logs/
```

---

## Business Logic

The backend includes key validation and logic:

- Prevents negative stock values
- Automatically tracks stock changes using StockLog
- Ensures users can only access their own items
- Validates input data on the server side

---

## Filtering and Search

The API supports:

- Search by item name
- Filter by category
- Low-stock filtering

Example:

```
/api/items/?search=laptop
/api/items/?category=1
/api/items/?low_stock=true
```

---

## Testing

Backend tests include:

- Unit tests for models
- API tests for endpoints
- Validation testing (e.g. negative stock prevention)
- Authentication testing

Run tests with:

```bash
python manage.py test
```

---

## Security

The system includes:

- Hashed passwords (Django auth)
- JWT authentication
- Protected endpoints
- Environment variable configuration for sensitive data

---

## Environment Variables

Configuration is handled using `.env`:

Example:

```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=inventory_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

## Deployment

The backend can be deployed using platforms such as Render.
