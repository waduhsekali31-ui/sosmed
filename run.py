import os
import sys
from app import create_app
from app.models import db, User, Post, Comment, Category, Tag, Like

app = create_app(os.getenv('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Add objects to the shell context"""
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Comment': Comment,
        'Category': Category,
        'Tag': Tag,
        'Like': Like
    }

if __name__ == '__main__':
    app.run(debug=True)
