from app import app, db, User, Recipe
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    with app.app_context():
        # Create tables
        db.drop_all()
        db.create_all()

        # Create admin user
        admin = User(
            username=os.getenv('ADMIN_USERNAME', 'admin'),
            is_admin=True,
            can_add_recipes=True
        )
        admin.set_password(os.getenv('ADMIN_PASSWORD', 'admin'))
        db.session.add(admin)

        # Create a recipe manager user
        manager = User(
            username='recipe_manager',
            can_add_recipes=True
        )
        manager.set_password('manager123')
        db.session.add(manager)

        # Add some sample recipes
        recipes = [
            {
                'title': 'Chocolate Chip Cookies',
                'ingredients': '2 1/4 cups all-purpose flour\n1 cup butter\n3/4 cup sugar\n2 eggs\n2 cups chocolate chips',
                'instructions': '1. Preheat oven to 375°F\n2. Mix ingredients\n3. Drop spoonfuls onto baking sheet\n4. Bake for 10 minutes'
            },
            {
                'title': 'Classic Pancakes',
                'ingredients': '1 1/2 cups all-purpose flour\n3 1/2 teaspoons baking powder\n1 teaspoon salt\n1 tablespoon sugar',
                'instructions': '1. Mix dry ingredients\n2. Add wet ingredients\n3. Cook on griddle'
            }
        ]

        for recipe_data in recipes:
            recipe = Recipe(**recipe_data)
            db.session.add(recipe)

        db.session.commit()

if __name__ == '__main__':
    init_db()
