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
    
    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.slot_routes import slot_bp
    from app.routes.user_routes import user_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.feedback_routes import feedback_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(slot_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(feedback_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
