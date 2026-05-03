# Inventory Management System – Backend

## Overview

This project is the backend for the Inventory Management System, built using Django and Django REST Framework.

It provides a RESTful API responsible for authentication, business logic, validation, and data persistence. The system is designed using enterprise software engineering principles such as separation of concerns, secure authentication, and scalable architecture.

The backend supports:

- User registration and authentication
- Inventory item management (CRUD operations)
- Category management
- Stock tracking with audit logs
- User profile management with image upload

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

## Architecture

The system follows a three-layer architecture:

### Frontend (React)
- Handles UI, routing, and user interaction  
- Communicates with backend via API  

### Backend (Django REST API)
- Handles authentication, validation, and business logic  
- Exposes RESTful endpoints  

### Database (PostgreSQL)
- Stores users, items, categories, stock logs, and profiles  

The frontend communicates with the backend exclusively through API endpoints.

---

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Python Decouple (environment variables)
- Pillow (image handling)

---

## Authentication

Authentication is implemented using JSON Web Tokens (JWT).

### Endpoints

Register:
```
POST /api/register/
```

Login:
```
POST /api/token/
```

Refresh Token:
```
POST /api/token/refresh/
```

### Features

- Secure password hashing using Django authentication
- Token-based authentication for stateless sessions
- Protected API endpoints using `IsAuthenticated`
- User-specific data access control

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

Fields:
- name

---

### StockLog
Tracks stock changes over time.

Fields include:
- item
- change amount (+ / -)
- user
- timestamp

This provides an audit trail for inventory changes.

---

### Profile
Extends the default Django user model.

Fields include:
- user (OneToOne relationship)
- display name
- profile image

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

### Profile
```
GET    /api/profile/
PUT    /api/profile/
```

---

## Business Logic

The backend includes key validation and domain logic:

- Prevents negative stock values
- Tracks stock updates automatically using StockLog
- Ensures users can only access their own items
- Validates input data at the API level
- Records audit history for inventory changes

Example validation:

```python
def validate_quantity(self, value):
    if value < 0:
        raise serializers.ValidationError("Stock cannot be negative.")
    return value
```

---

## Filtering and Search

The API supports:

- Search by item name
- Filter by category
- Low-stock filtering

Examples:

```
/api/items/?search=laptop
/api/items/?category=1
/api/items/?low_stock=true
```

---

## Testing

Backend tests include:

- Unit tests for models
- API endpoint testing
- Validation testing (e.g. negative stock prevention)
- Authentication and permission testing

Run tests with:

```bash
python manage.py test
```

Testing focuses on verifying business logic and ensuring correct behaviour under different scenarios.

---

## Security

The system includes:

- Secure password hashing via Django auth
- JWT-based authentication
- Protected endpoints requiring authentication
- User-specific data access control
- Environment variables for sensitive data

---

## Environment Variables

Configuration is handled using environment variables.

Example:

```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
```

This approach separates configuration from code and improves security.

---

## Deployment

The backend is deployed using Render.

### Key Deployment Features

- PostgreSQL database configured via `DATABASE_URL`
- Environment variables used for configuration
- Gunicorn used as the production server
- Static files handled using WhiteNoise

### Production Considerations

- Separate frontend and backend services
- Secure handling of credentials
- Scalable API design using stateless JWT authentication

---

## Technical Decisions

- **Django REST Framework** used for structured API development
- **JWT authentication** chosen for stateless and scalable sessions
- **PostgreSQL** used for production-ready relational database
- **Separation of concerns** between models, serializers, and views
- **Audit logging (StockLog)** implemented for traceability
- **Environment-based configuration** for flexibility across environments

These decisions align with enterprise application design principles.

---

## AI Usage Disclaimer

Generative AI tools (such as ChatGPT) were used during the development of this project to:

- Assist with debugging errors and resolving issues
- Explain technical concepts related to Django, React, and API design
- Suggest improvements to code structure and testing strategies
- Help draft and refine documentation

All AI-generated content was critically reviewed, tested, and adapted before being integrated into the final implementation. I maintain full understanding and ownership of all submitted code and design decisions.

---

## Summary

This backend demonstrates:

- Secure authentication using JWT
- Full CRUD functionality for inventory management
- Implementation of business logic and validation
- Audit logging for traceability
- Modular and maintainable architecture
- Automated testing practices
- Production deployment with environment configuration

The system reflects enterprise-level design and provides a scalable foundation for future development.
