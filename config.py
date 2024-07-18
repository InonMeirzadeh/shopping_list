import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_secret_key_for_development'
    DATABASE = 'inventory.db'