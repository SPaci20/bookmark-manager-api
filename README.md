# 📑 Bookmark Manager API

A professional REST API for managing bookmarks with collections and tag-based filtering.  
Built with **Django REST Framework** and **JWT authentication**.

---

## 🚀 Features

- **JWT Authentication** – Secure user registration/login with token-based auth  
- **Collection Management** – Organize bookmarks into customizable collections  
- **Smart Tag Filtering** – Advanced search by tags with partial matching  
- **RESTful Design** – Clean, predictable API endpoints following best practices  
- **Swagger Documentation** – Interactive API documentation with live testing  
- **User Isolation** – Secure data separation between users  
- **CRUD Operations** – Full Create, Read, Update, Delete functionality  

---

## 📚 API Documentation

- **Interactive Swagger UI:** `/swagger/`  
- **ReDoc Documentation:** `/redoc/`  
- **API Root:** `/api/`  

---

## 🔑 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.  
Include the token in your request headers:

```http
Authorization: Bearer your-access-token-here
🛠️ Installation & Setup
Prerequisites
Python 3.8+

pip package manager

Local Development
bash
Copy code
# Clone the repository
git clone <your-repo-url>
cd bookmark-manager-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
The API will be available at: http://localhost:8000

📋 API Endpoints
Authentication
Method	  Endpoint	                  Description
POST	/api/auth/register/	         Register new user
POST	/api/auth/login/	         Login user
GET	    /api/auth/profile/	         Get user profile
POST	/api/auth/token/refresh/	 Refresh access token

Collections
Method	    Endpoint	               Description
GET	       /api/collections/	     List all user collections
POST	   /api/collections/	     Create new collection
GET	     /api/collections/{id}/	     Get collection details
PUT       /api/collections/{id}/	 Update collection
DELETE	  /api/collections/{id}/	 Delete collection

Bookmarks
Method	   Endpoint	                 Description
GET	      /api/bookmarks/	         List all bookmarks
POST	  /api/bookmarks/	         Create new bookmark
GET	     /api/bookmarks/{id}/	     Get bookmark details
PUT      /api/bookmarks/{id}/	     Update bookmark
DELETE	 /api/bookmarks/{id}/	     Delete bookmark
GET	     /api/bookmarks/tag/{tag}/	 Filter by tag

💡 Usage Examples
User Registration
http
Copy code
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
Create Bookmark
http
Copy code
POST /api/bookmarks/
Authorization: Bearer your-token-here
Content-Type: application/json

{
  "title": "Django Documentation",
  "url": "https://docs.djangoproject.com",
  "description": "Official Django documentation",
  "tags": "django, python, backend",
  "collection": 1
}
Filter by Tag
http
Copy code
GET /api/bookmarks/tag/django/
Authorization: Bearer your-token-here
🗃️ Data Models
User – Authentication and ownership

Collection – Groups of related bookmarks

Bookmark – Individual saved links with metadata

🛡️ Security Features
Password hashing with Django’s built-in auth

JWT token expiration & refresh

User-level data isolation

SQL injection protection via Django ORM

🚀 Deployment
This API can be deployed to various platforms:

Heroku: git push heroku main

Railway: Connect GitHub repository

PythonAnywhere: Upload via Git or ZIP

👨‍💻 Development
Running Tests
bash
Copy code
python manage.py test
Code Style
Follows PEP 8 standards

Implements Django best practices

📦 requirements.txt
txt
Copy code
# Example dependencies
Django>=4.0
djangorestframework
djangorestframework-simplejwt
drf-yasg
gunicorn
psycopg2-binary
whitenoise
