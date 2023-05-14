"""Web development configuration."""
import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
# FIX THIS
SECRET_KEY = b'7\xff\xb5M[\xfc\xc3\xc6\xc8\x13zq\xb0x4\x17Z\x00BE'
SECRET_KEY += b'\xa1\x7f\x97\xfb'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
WEB_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = WEB_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/web.sqlite3
DATABASE_FILENAME = WEB_ROOT/'var'/'insta485.sqlite3'
