# 🧁 Butter Garden

A delightful recipe management application built with Flask, featuring a cozy, warm-toned interface and modern web technologies.

🌟 **[Try the Demo](https://garden.hex.lgbt)** 🌟

## ✨ Features

- 🔍 Browse and search recipes
- 📝 View detailed recipe ingredients and instructions
- 👥 Multi-user support with role-based permissions:
  - 👑 Admin users can manage all recipes and users
  - 👩‍🍳 Recipe managers can create and manage their own recipes
  - 👀 Regular users can browse recipes
- 🎨 Beautiful, responsive design with custom styling
- 🚀 Modern interactions using HTMX
- 🌙 Dark mode support with smooth transitions
- 🎯 System theme detection and persistence
- 🌟 Warm, inviting color scheme
- 🐳 Docker support for easy deployment

## 🛠️ Technology Stack

- **Backend**: Flask + SQLAlchemy
- **Frontend**: HTMX + Custom CSS
- **Database**: SQLite
- **Authentication**: Flask-Login with Role-Based Access
- **Styling**: 
  - CSS Variables for theming
  - Dark/Light mode with system preference detection
  - Smooth theme transitions
  - Modern CSS Features
- **Deployment**: Docker + Gunicorn

## 🚀 Quick Start with Docker

The easiest way to run Butter Garden is using Docker:

1. Clone the repository:
   ```bash
   git clone https://github.com/HardwarePunk/ButterGarden.git
   cd ButterGarden
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

3. Start with Docker Compose:
   ```bash
   docker-compose up -d
   ```

That's it! Visit `http://localhost:5000` to start using Butter Garden.

## 🐳 Docker Details

### Container Features
- Production-grade Gunicorn server
- Automatic health checks
- Persistent SQLite database volume
- Non-root user for security
- Automatic restarts on failure

### Container Management

**Start the container:**
```bash
docker-compose up -d
```

**View logs:**
```bash
docker-compose logs -f
```

**Stop the container:**
```bash
docker-compose down
```

**Rebuild after changes:**
```bash
docker-compose up -d --build
```

### Docker Configuration
- Port: 5000 (configurable in docker-compose.yml)
- Database location: /app/instance (mounted as volume)
- Environment variables: loaded from .env file
- Health check interval: 30 seconds

## 📝 Manual Installation (Without Docker)

If you prefer to run without Docker:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

4. Initialize the database:
   ```bash
   python init_db.py
   ```

5. Run the development server:
   ```bash
   flask run
   ```

## 🔒 Environment Variables

Required variables in `.env`:
```bash
FLASK_SECRET_KEY=your-secret-key-here
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD=your-secure-password
FLASK_ENV=production  # or development
```

## 👥 User Management

Butter Garden supports three types of users:

1. **Admin Users**
   - Can manage all recipes
   - Can add, edit, and delete users
   - Can assign user roles
   - Full access to all features

2. **Recipe Managers**
   - Can create new recipes
   - Can edit and delete their own recipes
   - Cannot manage other users
   - Access to "My Recipes" dashboard

3. **Regular Users**
   - Can browse and view recipes
   - Cannot create or edit recipes
   - No access to management features

### Default Users

The application comes with two default users after initialization:

1. **Admin User**
   - Username: from ADMIN_USERNAME in .env
   - Password: from ADMIN_PASSWORD in .env
   - Full administrative access

2. **Recipe Manager**
   - Username: recipe_manager
   - Password: manager123
   - Can create and manage their own recipes

To create additional users:
1. Log in as an admin user
2. Click "Manage Users" in the admin panel
3. Click "Add New User"
4. Fill in the username, password, and permissions

## 👩‍💻 Development

The application uses modern CSS features and HTMX for enhanced interactivity:
- CSS Variables for easy theme customization
- Responsive design, mobile friendly
- HTMX for dynamic content updates
- Custom scrollbar styling
- Sticky navigation elements

## 🎨 Customization

The app's appearance can be easily customized by modifying the CSS variables in `static/css/main.css`:

```css
:root {
  --primary-color: #9B4819;     /* Warm terracotta */
  --secondary-color: #D68C45;   /* Muted orange */
  --background-color: #FDF6EC;  /* Warm off-white */
  /* ... other variables ... */
}
```

## 📱 Responsive Design

- Desktop: Left sidebar navigation
- Mobile: Top navigation bar
- Adaptive recipe content display
- Optimized spacing and typography

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the Unlicense License - see the LICENSE file for details.
