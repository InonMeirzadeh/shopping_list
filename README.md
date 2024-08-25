Inventory Management System
A Flask-based app to manage products and shopping lists.
Features:

Add, update, delete products
Search and sort products
Automatic shopping list updates

Setup:

Clone repo
Install dependencies: pip install -r requirements.txt
Initialize DB:
from app.models import Database
Database.init_db()
Run: python run.py
Access at http://localhost:5000

Usage:

Add products via form
Update/delete products on main page
Search using top bar
Sort using dropdown menu

Structure:

Backend: init.py, controllers.py, models.py, views.py, run.py
Frontend: index.html, search_results.html, styles.css, script.js
