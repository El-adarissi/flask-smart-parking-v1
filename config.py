import os

class Config:
    # MySQL configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/smartparking')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    CORS_SUPPORTS_CREDENTIALS = True
