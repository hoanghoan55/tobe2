import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cấu hình Cloudinary   
cloudinary.config( 
    cloud_name = "dwkkugzxr", 
    api_key = "668853365344795", 
    api_secret = "668853365344795", # Click 'View API Keys' above to copy your API secret
    secure=True
)
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
