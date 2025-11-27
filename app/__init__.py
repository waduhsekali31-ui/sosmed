from flask import Flask, jsonify
from config.config import config
from app.models import db
from app.views import user_bp, post_bp, comment_bp, category_bp, tag_bp, like_bp
import os

def create_app(config_name='development'):
    """Application factory"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(tag_bp)
    app.register_blueprint(like_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({'status': 'API is running'}), 200
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run(debug=True, host='0.0.0.0', port=5000)
