# REST API Testing Guide

## API Testing with curl

### 1. Health Check
```bash
curl http://localhost:5000/api/health
```

### 2. User Management

#### Create User
```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "full_name": "Test User"
  }'
```

#### Login
```bash
curl -X POST http://localhost:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "password123"
  }'
```

#### Get All Users
```bash
curl http://localhost:5000/api/users?page=1&per_page=10
```

#### Get User by ID
```bash
curl http://localhost:5000/api/users/1
```

#### Update User
```bash
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Updated Name",
    "email": "newemail@example.com"
  }'
```

#### Delete User
```bash
curl -X DELETE http://localhost:5000/api/users/1
```

### 3. Posts Management

#### Create Post
```bash
curl -X POST http://localhost:5000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is amazing content",
    "user_id": 1,
    "category_id": 1,
    "status": "published"
  }'
```

#### Get All Posts
```bash
curl http://localhost:5000/api/posts?page=1&per_page=10&status=published
```

#### Get Post by ID
```bash
curl http://localhost:5000/api/posts/1
```

#### Update Post
```bash
curl -X PUT http://localhost:5000/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content",
    "user_id": 1
  }'
```

#### Delete Post
```bash
curl -X DELETE http://localhost:5000/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1
  }'
```

### 4. Comments Management

#### Create Comment
```bash
curl -X POST http://localhost:5000/api/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Great post!",
    "user_id": 2,
    "post_id": 1
  }'
```

#### Get Post Comments
```bash
curl http://localhost:5000/api/comments/post/1?page=1&per_page=10
```

#### Get Comment by ID
```bash
curl http://localhost:5000/api/comments/1
```

#### Update Comment
```bash
curl -X PUT http://localhost:5000/api/comments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Updated comment",
    "user_id": 2
  }'
```

#### Delete Comment
```bash
curl -X DELETE http://localhost:5000/api/comments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 2
  }'
```

### 5. Categories Management

#### Create Category
```bash
curl -X POST http://localhost:5000/api/categories \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Programming",
    "slug": "programming",
    "description": "Programming related posts"
  }'
```

#### Get All Categories
```bash
curl http://localhost:5000/api/categories
```

#### Get Category by ID
```bash
curl http://localhost:5000/api/categories/1
```

#### Update Category
```bash
curl -X PUT http://localhost:5000/api/categories/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Web Development",
    "description": "Web development posts"
  }'
```

#### Delete Category
```bash
curl -X DELETE http://localhost:5000/api/categories/1
```

### 6. Tags Management

#### Create Tag
```bash
curl -X POST http://localhost:5000/api/tags \
  -H "Content-Type: application/json" \
  -d '{
    "name": "JavaScript",
    "slug": "javascript"
  }'
```

#### Get All Tags
```bash
curl http://localhost:5000/api/tags
```

#### Get Tag by ID
```bash
curl http://localhost:5000/api/tags/1
```

#### Delete Tag
```bash
curl -X DELETE http://localhost:5000/api/tags/1
```

### 7. Likes Management

#### Like a Post
```bash
curl -X POST http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

#### Unlike a Post
```bash
curl -X DELETE http://localhost:5000/api/likes \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "post_id": 1
  }'
```

#### Get Post Likes
```bash
curl http://localhost:5000/api/likes/post/1?page=1&per_page=10
```

## API Response Examples

### Success Response (200/201)
```json
{
  "id": 1,
  "username": "john",
  "email": "john@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "created_at": "2024-11-27T10:00:00",
  "updated_at": "2024-11-27T10:00:00"
}
```

### Error Response (400/404/500)
```json
{
  "error": "Missing required fields"
}
```

## Testing Checklist

- [ ] Health check endpoint
- [ ] Create user
- [ ] User login
- [ ] Get all users (with pagination)
- [ ] Get user by ID
- [ ] Update user
- [ ] Delete user
- [ ] Create post
- [ ] Get all posts
- [ ] Get post by ID
- [ ] Update post
- [ ] Delete post
- [ ] Create category
- [ ] Get all categories
- [ ] Create tag
- [ ] Get all tags
- [ ] Create comment
- [ ] Get post comments
- [ ] Update comment
- [ ] Delete comment
- [ ] Like post
- [ ] Unlike post
- [ ] Get post likes

## Database Verification

### MySQL/MariaDB Commands
```bash
# Connect to database
mysql -u username -p database_name

# Show tables
SHOW TABLES;

# Show table structure
DESCRIBE users;
DESCRIBE posts;
DESCRIBE comments;
DESCRIBE categories;
DESCRIBE tags;
DESCRIBE likes;
DESCRIBE post_tags;

# View data
SELECT * FROM users;
SELECT * FROM posts;
SELECT * FROM comments;
```
