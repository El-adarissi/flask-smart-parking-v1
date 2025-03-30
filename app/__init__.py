from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, supports_credentials=True, origins=["*"])
    
    # Import and register routes
    from app.routes import init_routes
    init_routes(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
