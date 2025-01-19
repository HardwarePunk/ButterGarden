# 🧁 Butter Garden

A delightful recipe management application built with Flask, featuring a cozy, warm-toned interface and modern web technologies.

## ✨ Features

- 🔍 Browse and search recipes
- 📝 View detailed recipe ingredients and instructions
- 👤 Admin interface for managing recipes
- 🎨 Beautiful, responsive design with custom styling
- 🚀 Modern interactions using HTMX
- 🌙 Warm, inviting color scheme

## 🛠️ Technology Stack

- **Backend**: Flask + SQLAlchemy
- **Frontend**: HTMX + Custom CSS
- **Database**: SQLite
- **Authentication**: Flask-Login
- **Styling**: CSS Variables + Modern CSS Features

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/HardwarePunk/ButterGarden.git
   cd ButterGarden
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

5. Initialize the database:
   ```bash
   python init_db.py
   ```

6. Run the application:
   ```bash
   flask run
   ```

Visit `http://localhost:5000` to start using Butter Garden!

## 🔒 Environment Variables

Create a `.env` file with the following variables:
```
FLASK_SECRET_KEY=your-secret-key-here
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD=your-secure-password
FLASK_ENV=development
```

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
