# 🧑‍💻 Flask REST API - User Management

### 📌 Objective
Build a simple REST API using Python and Flask to manage user data in memory.

### 🛠 Tools Used
- Python 3.x
- Flask
- Postman (for testing)

### 📁 Endpoints

| Method | URL             | Description             |
|--------|------------------|-------------------------|
| GET    | `/users`         | Get all users           |
| GET    | `/users/<id>`    | Get specific user       |
| POST   | `/users`         | Create new user         |
| PUT    | `/users/<id>`    | Update existing user    |
| DELETE | `/users/<id>`    | Delete user             |

### 🔧 Run the App

```bash
pip install flask
python app.py
```
🔍 Sample POST (using curl)
bash
```
curl -X POST http://127.0.0.1:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Deepak", "email": "deepak@example.com"}'
```
