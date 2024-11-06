# Flask CRUD Application with MongoDB

## Overview

This is a Flask-based REST API application that performs CRUD operations on a MongoDB database for managing a "User" resource.

## Requirements

- **Python 3.9+**
- **MongoDB**

## Setup and Run

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/FlaskCRUDApp.git
   cd FlaskCRUDApp
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application:**
   ```bash
   python run.py
   ```

## API Endpoints

1. `GET /users` - List all users.
2. `GET /users/<id>` - Fetch user by ID.
3. `POST /users` - Create a new user.
4. `PUT /users/<id>` - Update a user.
5. `DELETE /users/<id>` - Delete a user.

## Docker Setup

```bash
docker build -t flask_crud_app .
docker run -p 5000:5000 flask_crud_app
```
