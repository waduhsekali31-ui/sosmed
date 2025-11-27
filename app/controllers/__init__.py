from app.models import db, User, Post, Comment, Category, Tag, Like
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from datetime import datetime

class UserController:
    """Handle user-related operations"""
    
    @staticmethod
    def create_user(data):
        """Create a new user"""
        try:
            if User.query.filter_by(username=data.get('username')).first():
                return {'error': 'Username already exists'}, 400
            
            if User.query.filter_by(email=data.get('email')).first():
                return {'error': 'Email already exists'}, 400
            
            user = User(
                username=data.get('username'),
                email=data.get('email'),
                password=generate_password_hash(data.get('password')),
                full_name=data.get('full_name')
            )
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_user(user_id):
        """Get user by ID"""
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200
    
    @staticmethod
    def get_all_users(page=1, per_page=10):
        """Get all users with pagination"""
        pagination = User.query.paginate(page=page, per_page=per_page)
        return {
            'users': [u.to_dict() for u in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }, 200
    
    @staticmethod
    def update_user(user_id, data):
        """Update user information"""
        try:
            user = User.query.get(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            
            if 'username' in data and data['username'] != user.username:
                if User.query.filter_by(username=data['username']).first():
                    return {'error': 'Username already exists'}, 400
                user.username = data['username']
            
            if 'email' in data and data['email'] != user.email:
                if User.query.filter_by(email=data['email']).first():
                    return {'error': 'Email already exists'}, 400
                user.email = data['email']
            
            if 'full_name' in data:
                user.full_name = data['full_name']
            
            if 'password' in data:
                user.password = generate_password_hash(data['password'])
            
            user.updated_at = datetime.utcnow()
            db.session.commit()
            return user.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def delete_user(user_id):
        """Delete a user"""
        try:
            user = User.query.get(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def login(username, password):
        """Verify user credentials"""
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {'error': 'Invalid username or password'}, 401
        return user.to_dict(), 200


class PostController:
    """Handle post-related operations"""
    
    @staticmethod
    def create_post(data, user_id):
        """Create a new post"""
        try:
            post = Post(
                title=data.get('title'),
                content=data.get('content'),
                user_id=user_id,
                category_id=data.get('category_id'),
                status=data.get('status', 'draft')
            )
            db.session.add(post)
            db.session.commit()
            return post.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_post(post_id):
        """Get post by ID"""
        post = Post.query.get(post_id)
        if not post:
            return {'error': 'Post not found'}, 404
        post.views_count += 1
        db.session.commit()
        return post.to_dict(include_comments=True), 200
    
    @staticmethod
    def get_all_posts(page=1, per_page=10, status='published'):
        """Get all posts with pagination"""
        query = Post.query.filter_by(status=status)
        pagination = query.paginate(page=page, per_page=per_page)
        return {
            'posts': [p.to_dict() for p in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }, 200
    
    @staticmethod
    def update_post(post_id, data, user_id):
        """Update a post"""
        try:
            post = Post.query.get(post_id)
            if not post:
                return {'error': 'Post not found'}, 404
            
            if post.user_id != user_id:
                return {'error': 'Unauthorized'}, 403
            
            if 'title' in data:
                post.title = data['title']
            if 'content' in data:
                post.content = data['content']
            if 'category_id' in data:
                post.category_id = data['category_id']
            if 'status' in data:
                post.status = data['status']
            
            post.updated_at = datetime.utcnow()
            db.session.commit()
            return post.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def delete_post(post_id, user_id):
        """Delete a post"""
        try:
            post = Post.query.get(post_id)
            if not post:
                return {'error': 'Post not found'}, 404
            
            if post.user_id != user_id:
                return {'error': 'Unauthorized'}, 403
            
            db.session.delete(post)
            db.session.commit()
            return {'message': 'Post deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500


class CommentController:
    """Handle comment-related operations"""
    
    @staticmethod
    def create_comment(data, user_id):
        """Create a new comment"""
        try:
            comment = Comment(
                content=data.get('content'),
                user_id=user_id,
                post_id=data.get('post_id')
            )
            db.session.add(comment)
            db.session.commit()
            return comment.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_comment(comment_id):
        """Get comment by ID"""
        comment = Comment.query.get(comment_id)
        if not comment:
            return {'error': 'Comment not found'}, 404
        return comment.to_dict(), 200
    
    @staticmethod
    def get_post_comments(post_id, page=1, per_page=10):
        """Get all comments for a post"""
        pagination = Comment.query.filter_by(post_id=post_id, is_approved=True).paginate(page=page, per_page=per_page)
        return {
            'comments': [c.to_dict() for c in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }, 200
    
    @staticmethod
    def update_comment(comment_id, data, user_id):
        """Update a comment"""
        try:
            comment = Comment.query.get(comment_id)
            if not comment:
                return {'error': 'Comment not found'}, 404
            
            if comment.user_id != user_id:
                return {'error': 'Unauthorized'}, 403
            
            if 'content' in data:
                comment.content = data['content']
            
            comment.updated_at = datetime.utcnow()
            db.session.commit()
            return comment.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def delete_comment(comment_id, user_id):
        """Delete a comment"""
        try:
            comment = Comment.query.get(comment_id)
            if not comment:
                return {'error': 'Comment not found'}, 404
            
            if comment.user_id != user_id:
                return {'error': 'Unauthorized'}, 403
            
            db.session.delete(comment)
            db.session.commit()
            return {'message': 'Comment deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500


class CategoryController:
    """Handle category-related operations"""
    
    @staticmethod
    def create_category(data):
        """Create a new category"""
        try:
            if Category.query.filter_by(slug=data.get('slug')).first():
                return {'error': 'Category slug already exists'}, 400
            
            category = Category(
                name=data.get('name'),
                description=data.get('description'),
                slug=data.get('slug')
            )
            db.session.add(category)
            db.session.commit()
            return category.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_category(category_id):
        """Get category by ID"""
        category = Category.query.get(category_id)
        if not category:
            return {'error': 'Category not found'}, 404
        return category.to_dict(), 200
    
    @staticmethod
    def get_all_categories():
        """Get all categories"""
        categories = Category.query.all()
        return [c.to_dict() for c in categories], 200
    
    @staticmethod
    def update_category(category_id, data):
        """Update a category"""
        try:
            category = Category.query.get(category_id)
            if not category:
                return {'error': 'Category not found'}, 404
            
            if 'name' in data:
                category.name = data['name']
            if 'description' in data:
                category.description = data['description']
            if 'slug' in data:
                if Category.query.filter_by(slug=data['slug']).first():
                    return {'error': 'Category slug already exists'}, 400
                category.slug = data['slug']
            
            category.updated_at = datetime.utcnow()
            db.session.commit()
            return category.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def delete_category(category_id):
        """Delete a category"""
        try:
            category = Category.query.get(category_id)
            if not category:
                return {'error': 'Category not found'}, 404
            
            db.session.delete(category)
            db.session.commit()
            return {'message': 'Category deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500


class TagController:
    """Handle tag-related operations"""
    
    @staticmethod
    def create_tag(data):
        """Create a new tag"""
        try:
            if Tag.query.filter_by(slug=data.get('slug')).first():
                return {'error': 'Tag slug already exists'}, 400
            
            tag = Tag(
                name=data.get('name'),
                slug=data.get('slug')
            )
            db.session.add(tag)
            db.session.commit()
            return tag.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_tag(tag_id):
        """Get tag by ID"""
        tag = Tag.query.get(tag_id)
        if not tag:
            return {'error': 'Tag not found'}, 404
        return tag.to_dict(), 200
    
    @staticmethod
    def get_all_tags():
        """Get all tags"""
        tags = Tag.query.all()
        return [t.to_dict() for t in tags], 200
    
    @staticmethod
    def delete_tag(tag_id):
        """Delete a tag"""
        try:
            tag = Tag.query.get(tag_id)
            if not tag:
                return {'error': 'Tag not found'}, 404
            
            db.session.delete(tag)
            db.session.commit()
            return {'message': 'Tag deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500


class LikeController:
    """Handle like-related operations"""
    
    @staticmethod
    def like_post(user_id, post_id):
        """Like a post"""
        try:
            post = Post.query.get(post_id)
            if not post:
                return {'error': 'Post not found'}, 404
            
            existing_like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
            if existing_like:
                return {'error': 'You already liked this post'}, 400
            
            like = Like(user_id=user_id, post_id=post_id)
            db.session.add(like)
            db.session.commit()
            return like.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def unlike_post(user_id, post_id):
        """Unlike a post"""
        try:
            like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
            if not like:
                return {'error': 'Like not found'}, 404
            
            db.session.delete(like)
            db.session.commit()
            return {'message': 'Post unliked successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
    
    @staticmethod
    def get_post_likes(post_id, page=1, per_page=10):
        """Get all likes for a post"""
        pagination = Like.query.filter_by(post_id=post_id).paginate(page=page, per_page=per_page)
        return {
            'likes': [l.to_dict() for l in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }, 200
