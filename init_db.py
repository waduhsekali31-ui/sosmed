#!/usr/bin/env python
"""
Database initialization script
Create and populate initial data
"""
import os
import sys
from app import create_app
from app.models import db, User, Post, Comment, Category, Tag, Like
from datetime import datetime
from werkzeug.security import generate_password_hash

def init_db():
    """Initialize database with sample data"""
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    
    with app.app_context():
        # Create tables
        print("Creating database tables...")
        db.create_all()
        print("✓ Tables created successfully!")
        
        # Check if data already exists
        if User.query.first() is not None:
            print("⚠ Database already contains data. Skipping sample data insertion.")
            return
        
        # Create sample users
        print("\nAdding sample users...")
        users = [
            User(username='john', email='john@example.com', password=generate_password_hash('password123'), full_name='John Doe'),
            User(username='jane', email='jane@example.com', password=generate_password_hash('password123'), full_name='Jane Smith'),
            User(username='bob', email='bob@example.com', password=generate_password_hash('password123'), full_name='Bob Johnson'),
        ]
        db.session.add_all(users)
        db.session.commit()
        print(f"✓ Added {len(users)} users")
        
        # Create sample categories
        print("\nAdding sample categories...")
        categories = [
            Category(name='Technology', slug='technology', description='Tech related posts'),
            Category(name='Travel', slug='travel', description='Travel experiences'),
            Category(name='Food', slug='food', description='Food and recipes'),
        ]
        db.session.add_all(categories)
        db.session.commit()
        print(f"✓ Added {len(categories)} categories")
        
        # Create sample tags
        print("\nAdding sample tags...")
        tags = [
            Tag(name='Python', slug='python'),
            Tag(name='Flask', slug='flask'),
            Tag(name='API', slug='api'),
            Tag(name='Database', slug='database'),
        ]
        db.session.add_all(tags)
        db.session.commit()
        print(f"✓ Added {len(tags)} tags")
        
        # Create sample posts
        print("\nAdding sample posts...")
        posts = [
            Post(
                title='Getting Started with Flask',
                content='Flask is a lightweight web framework for Python. Learn how to build REST APIs with Flask.',
                user_id=1,
                category_id=1,
                status='published',
                published_at=datetime.utcnow()
            ),
            Post(
                title='Best Travel Destinations 2024',
                content='Discover the most beautiful places to visit this year. From beaches to mountains, there is something for everyone.',
                user_id=2,
                category_id=2,
                status='published',
                published_at=datetime.utcnow()
            ),
            Post(
                title='Homemade Pizza Recipe',
                content='Learn how to make delicious homemade pizza with simple ingredients. Perfect for family gatherings.',
                user_id=3,
                category_id=3,
                status='published',
                published_at=datetime.utcnow()
            ),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print(f"✓ Added {len(posts)} posts")
        
        # Create sample comments
        print("\nAdding sample comments...")
        comments = [
            Comment(content='Great tutorial! Very helpful.', user_id=2, post_id=1),
            Comment(content='I visited all these places. Highly recommended!', user_id=1, post_id=2),
            Comment(content='Perfect! I will try this recipe.', user_id=3, post_id=3),
        ]
        db.session.add_all(comments)
        db.session.commit()
        print(f"✓ Added {len(comments)} comments")
        
        # Create sample likes
        print("\nAdding sample likes...")
        likes = [
            Like(user_id=1, post_id=2),
            Like(user_id=2, post_id=3),
            Like(user_id=3, post_id=1),
        ]
        db.session.add_all(likes)
        db.session.commit()
        print(f"✓ Added {len(likes)} likes")
        
        print("\n✓ Database initialization completed successfully!")

if __name__ == '__main__':
    init_db()
