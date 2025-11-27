# Flask REST API - Project Documentation

## Overview
This is a complete REST API application built with Flask, using SQLAlchemy ORM and MySQL/MariaDB database. The project follows the MVC (Model-View-Controller) architecture pattern.

## Project Structure
```
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models/
│   │   └── __init__.py       # Database models (ORM)
│   ├── controllers/
│   │   └── __init__.py       # Business logic controllers
│   └── views/
│       └── __init__.py       # API routes and blueprints
├── config/
│   └── config.py             # Configuration settings
├── venv/                      # Virtual environment
├── .env                       # Environment variables
├── run.py                     # Application entry point
├── init_db.py                # Database initialization script
└── requirements.txt          # Python dependencies
```

## Features

### Architecture
- **MVC Pattern**: Separation of concerns with Models, Controllers, and Views
- **ORM (SQLAlchemy)**: Database abstraction layer for MySQL/MariaDB
- **RESTful API**: Standard REST conventions for all endpoints
- **Blueprints**: Organized routing with Flask blueprints

### Database Tables (6 tables)
1. **Users** - User accounts and authentication
2. **Posts** - Blog posts/articles
3. **Comments** - Comments on posts
4. **Categories** - Post categories
5. **Tags** - Post tags
6. **Likes** - Post likes (association table)

### API Endpoints

#### Users
- `POST /api/users` - Create new user
- `GET /api/users` - Get all users (paginated)
- `GET /api/users/<id>` - Get user by ID
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user
- `POST /api/users/login` - User login

#### Posts
- `POST /api/posts` - Create new post
- `GET /api/posts` - Get all posts (paginated, filtered by status)
- `GET /api/posts/<id>` - Get post by ID
- `PUT /api/posts/<id>` - Update post
- `DELETE /api/posts/<id>` - Delete post

#### Comments
- `POST /api/comments` - Create new comment
- `GET /api/comments/<id>` - Get comment by ID
- `GET /api/comments/post/<post_id>` - Get post comments
- `PUT /api/comments/<id>` - Update comment
- `DELETE /api/comments/<id>` - Delete comment

#### Categories
- `POST /api/categories` - Create new category
- `GET /api/categories` - Get all categories
- `GET /api/categories/<id>` - Get category by ID
- `PUT /api/categories/<id>` - Update category
- `DELETE /api/categories/<id>` - Delete category

#### Tags
- `POST /api/tags` - Create new tag
- `GET /api/tags` - Get all tags
- `GET /api/tags/<id>` - Get tag by ID
- `DELETE /api/tags/<id>` - Delete tag

#### Likes
- `POST /api/likes` - Like a post
- `DELETE /api/likes` - Unlike a post
- `GET /api/likes/post/<post_id>` - Get post likes

#### Health Check
- `GET /api/health` - API health status

## Installation & Setup

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database
Edit `.env` file with your MySQL/MariaDB credentials:
```
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/database_name
```

### 4. Initialize Database
```bash
python init_db.py
```

This script will:
- Create all database tables
- Add sample users, categories, tags, posts, comments, and likes

### 5. Run the Application
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## Usage Examples

### Create a User
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "user@example.com",
    "password": "secure_password",
    "full_name": "New User"
  }'
```

### Get All Users
```bash
curl http://localhost:5000/api/users?page=1&per_page=10
```

### Create a Post
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my post",
    "user_id": 1,
    "category_id": 1,
    "status": "published"
  }'
```

### Like a Post
```bash
curl -X POST http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

### Create a Comment
```bash
curl -X POST http://localhost:5000/api/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Great post!",
    "user_id": 2,
    "post_id": 1
  }'
```

## Database Models

### User Model
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `password` (String, Hashed)
- `full_name` (String)
- `profile_picture` (String)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Post Model
- `id` (Integer, Primary Key)
- `title` (String)
- `content` (Text)
- `user_id` (Foreign Key)
- `category_id` (Foreign Key)
- `status` (String: draft, published, archived)
- `views_count` (Integer)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- `published_at` (DateTime)

### Comment Model
- `id` (Integer, Primary Key)
- `content` (Text)
- `user_id` (Foreign Key)
- `post_id` (Foreign Key)
- `is_approved` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Category Model
- `id` (Integer, Primary Key)
- `name` (String, Unique)
- `description` (Text)
- `slug` (String, Unique)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Tag Model
- `id` (Integer, Primary Key)
- `name` (String, Unique)
- `slug` (String, Unique)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Like Model
- `id` (Integer, Primary Key)
- `user_id` (Foreign Key)
- `post_id` (Foreign Key)
- `created_at` (DateTime)
- Unique constraint on (user_id, post_id)

## Environment Variables
Configure these in `.env`:
- `FLASK_ENV` - Environment (development/production)
- `FLASK_DEBUG` - Debug mode (True/False)
- `DATABASE_URL` - MySQL connection string
- `SECRET_KEY` - Secret key for sessions

## Requirements
- Python 3.8+
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5
- PyMySQL 1.1.0
- python-dotenv 1.0.0
- cryptography 41.0.3
- PyJWT 2.8.1

## Key Features

### 1. **MVC Architecture**
   - **Models**: Database models with relationships
   - **Controllers**: Business logic and data processing
   - **Views**: API endpoints and routing

### 2. **ORM (SQLAlchemy)**
   - Automatic SQL generation
   - Type safety and validation
   - Relationship management
   - Query optimization

### 3. **Database**
   - MySQL/MariaDB support
   - 6 interconnected tables
   - Foreign keys and constraints
   - Indexed fields for performance

### 4. **Security**
   - Password hashing with werkzeug
   - User authentication
   - Data validation

### 5. **API Features**
   - Pagination support
   - JSON responses
   - Error handling
   - Health check endpoint

## Error Handling
The API returns appropriate HTTP status codes:
- `200` - OK
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

## Development Commands

### Create Database
```bash
python init_db.py
```

### Flask Shell
```bash
export FLASK_APP=run.py
flask shell
```

### Run Tests (if added)
```bash
pytest
```

## Future Enhancements
- User authentication with JWT tokens
- Request validation with marshmallow
- API documentation with Swagger/OpenAPI
- Unit tests with pytest
- Rate limiting
- Caching
- Full-text search
- Admin panel

## License
This project is open source and available under the MIT License.

## Author
Created as a REST API project demonstration with Flask, SQLAlchemy ORM, and MySQL.
