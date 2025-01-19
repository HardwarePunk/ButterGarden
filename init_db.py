from app import app, db, User
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def init_db():
    with app.app_context():
        db.create_all()
        
        # Check if admin user already exists
        admin_username = os.getenv('ADMIN_USERNAME', 'admin')
        admin = User.query.filter_by(username=admin_username).first()
        if not admin:
            admin = User(
                username=admin_username,
                password_hash=generate_password_hash(os.getenv('ADMIN_PASSWORD', 'change-this-password')),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully!")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    init_db()
