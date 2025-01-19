from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'fallback-secret-key-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    recipes = Recipe.query.filter(
        (Recipe.title.ilike(f'%{query}%')) |
        (Recipe.ingredients.ilike(f'%{query}%'))
    ).all()
    return render_template('index.html', recipes=recipes, search_query=query)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe_detail.html', recipe=recipe)

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    if not current_user.is_admin:
        flash('Access denied.')
        return redirect(url_for('index'))
    recipes = Recipe.query.all()
    return render_template('admin.html', recipes=recipes)

@app.route('/admin/recipe/add', methods=['GET', 'POST'])
@login_required
def add_recipe():
    if not current_user.is_admin:
        flash('Access denied.')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        recipe = Recipe(
            title=request.form['title'],
            ingredients=request.form['ingredients'],
            instructions=request.form['instructions']
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!')
        return redirect(url_for('admin'))
    
    return render_template('recipe_form.html')

@app.route('/admin/recipe/edit/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    if not current_user.is_admin:
        flash('Access denied.')
        return redirect(url_for('index'))
    
    recipe = Recipe.query.get_or_404(recipe_id)
    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        db.session.commit()
        flash('Recipe updated successfully!')
        return redirect(url_for('admin'))
    
    return render_template('recipe_form.html', recipe=recipe)

@app.route('/admin/recipe/delete/<int:recipe_id>')
@login_required
def delete_recipe(recipe_id):
    if not current_user.is_admin:
        flash('Access denied.')
        return redirect(url_for('index'))
    
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully!')
    return redirect(url_for('admin'))

# HTMX Endpoints
@app.route('/recipes/search')
def search_recipes():
    query = request.args.get('query', '')
    recipes = Recipe.query.filter(
        (Recipe.title.ilike(f'%{query}%')) |
        (Recipe.ingredients.ilike(f'%{query}%'))
    ).all()
    return render_template('partials/recipe_list.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>/delete', methods=['DELETE'])
@login_required
def delete_recipe_htmx(recipe_id):
    if not current_user.is_admin:
        return 'Unauthorized', 403
    
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return '', 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect(url_for('admin'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
