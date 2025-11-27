from flask import Blueprint, request, jsonify
from app.controllers import (
    UserController, PostController, CommentController,
    CategoryController, TagController, LikeController
)

# Define blueprints
user_bp = Blueprint('users', __name__, url_prefix='/api/users')
post_bp = Blueprint('posts', __name__, url_prefix='/api/posts')
comment_bp = Blueprint('comments', __name__, url_prefix='/api/comments')
category_bp = Blueprint('categories', __name__, url_prefix='/api/categories')
tag_bp = Blueprint('tags', __name__, url_prefix='/api/tags')
like_bp = Blueprint('likes', __name__, url_prefix='/api/likes')

# ============== User Routes ==============
@user_bp.route('', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing required fields'}), 400
    result, status_code = UserController.create_user(data)
    return jsonify(result), status_code

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    result, status_code = UserController.get_user(user_id)
    return jsonify(result), status_code

@user_bp.route('', methods=['GET'])
def get_all_users():
    """Get all users"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    result, status_code = UserController.get_all_users(page, per_page)
    return jsonify(result), status_code

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user"""
    data = request.get_json()
    result, status_code = UserController.update_user(user_id, data)
    return jsonify(result), status_code

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user"""
    result, status_code = UserController.delete_user(user_id)
    return jsonify(result), status_code

@user_bp.route('/login', methods=['POST'])
def login():
    """User login"""
    data = request.get_json()
    if not data or not all(k in data for k in ('username', 'password')):
        return jsonify({'error': 'Missing username or password'}), 400
    result, status_code = UserController.login(data['username'], data['password'])
    return jsonify(result), status_code

# ============== Post Routes ==============
@post_bp.route('', methods=['POST'])
def create_post():
    """Create a new post"""
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'content', 'user_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    user_id = data.pop('user_id')
    result, status_code = PostController.create_post(data, user_id)
    return jsonify(result), status_code

@post_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get post by ID"""
    result, status_code = PostController.get_post(post_id)
    return jsonify(result), status_code

@post_bp.route('', methods=['GET'])
def get_all_posts():
    """Get all posts"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status', 'published')
    result, status_code = PostController.get_all_posts(page, per_page, status)
    return jsonify(result), status_code

@post_bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update post"""
    data = request.get_json()
    user_id = data.pop('user_id', None)
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    result, status_code = PostController.update_post(post_id, data, user_id)
    return jsonify(result), status_code

@post_bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete post"""
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    result, status_code = PostController.delete_post(post_id, user_id)
    return jsonify(result), status_code

# ============== Comment Routes ==============
@comment_bp.route('', methods=['POST'])
def create_comment():
    """Create a new comment"""
    data = request.get_json()
    if not data or not all(k in data for k in ('content', 'post_id', 'user_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    user_id = data.pop('user_id')
    result, status_code = CommentController.create_comment(data, user_id)
    return jsonify(result), status_code

@comment_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    """Get comment by ID"""
    result, status_code = CommentController.get_comment(comment_id)
    return jsonify(result), status_code

@comment_bp.route('/post/<int:post_id>', methods=['GET'])
def get_post_comments(post_id):
    """Get all comments for a post"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    result, status_code = CommentController.get_post_comments(post_id, page, per_page)
    return jsonify(result), status_code

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    """Update comment"""
    data = request.get_json()
    user_id = data.pop('user_id', None)
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    result, status_code = CommentController.update_comment(comment_id, data, user_id)
    return jsonify(result), status_code

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """Delete comment"""
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    result, status_code = CommentController.delete_comment(comment_id, user_id)
    return jsonify(result), status_code

# ============== Category Routes ==============
@category_bp.route('', methods=['POST'])
def create_category():
    """Create a new category"""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'slug')):
        return jsonify({'error': 'Missing required fields'}), 400
    result, status_code = CategoryController.create_category(data)
    return jsonify(result), status_code

@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Get category by ID"""
    result, status_code = CategoryController.get_category(category_id)
    return jsonify(result), status_code

@category_bp.route('', methods=['GET'])
def get_all_categories():
    """Get all categories"""
    result, status_code = CategoryController.get_all_categories()
    return jsonify(result), status_code

@category_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Update category"""
    data = request.get_json()
    result, status_code = CategoryController.update_category(category_id, data)
    return jsonify(result), status_code

@category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete category"""
    result, status_code = CategoryController.delete_category(category_id)
    return jsonify(result), status_code

# ============== Tag Routes ==============
@tag_bp.route('', methods=['POST'])
def create_tag():
    """Create a new tag"""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'slug')):
        return jsonify({'error': 'Missing required fields'}), 400
    result, status_code = TagController.create_tag(data)
    return jsonify(result), status_code

@tag_bp.route('/<int:tag_id>', methods=['GET'])
def get_tag(tag_id):
    """Get tag by ID"""
    result, status_code = TagController.get_tag(tag_id)
    return jsonify(result), status_code

@tag_bp.route('', methods=['GET'])
def get_all_tags():
    """Get all tags"""
    result, status_code = TagController.get_all_tags()
    return jsonify(result), status_code

@tag_bp.route('/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    """Delete tag"""
    result, status_code = TagController.delete_tag(tag_id)
    return jsonify(result), status_code

# ============== Like Routes ==============
@like_bp.route('', methods=['POST'])
def like_post():
    """Like a post"""
    data = request.get_json()
    if not data or not all(k in data for k in ('user_id', 'post_id')):
        return jsonify({'error': 'Missing user_id or post_id'}), 400
    result, status_code = LikeController.like_post(data['user_id'], data['post_id'])
    return jsonify(result), status_code

@like_bp.route('', methods=['DELETE'])
def unlike_post():
    """Unlike a post"""
    data = request.get_json()
    if not data or not all(k in data for k in ('user_id', 'post_id')):
        return jsonify({'error': 'Missing user_id or post_id'}), 400
    result, status_code = LikeController.unlike_post(data['user_id'], data['post_id'])
    return jsonify(result), status_code

@like_bp.route('/post/<int:post_id>', methods=['GET'])
def get_post_likes(post_id):
    """Get all likes for a post"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    result, status_code = LikeController.get_post_likes(post_id, page, per_page)
    return jsonify(result), status_code
