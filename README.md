# Shopping List Management System

A Flask-based application for managing product inventory and shopping lists.

## Features
- Add, update, and delete products
- Search functionality
- Automatic shopping list generation
- Sort products by name or quantity

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize database: 
   ```python
   from app.models import Database
   Database.init_db()

Run the app: python run.py
Access at http://localhost:5000

Project Structure

Backend: __init__.py, controllers.py, models.py, views.py, run.py
Frontend: index.html, search_results.html, styles.css, script.js

Usage

Add products via the form
Update/delete products using buttons
Search using the search bar
Sort using the dropdown menu

Development
Run in debug mode:
Copyexport FLASK_ENV=development
python run.py
Notes

Uses SQLite database (inventory.db)
Supports Hebrew text and RTL layout

Contributing
Contributions welcome via Pull Requests.
