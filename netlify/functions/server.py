import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'production'))

def handler(event, context):
    """Netlify serverless function handler"""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": '{"message": "API is running"}'
    }
