# QR Menu Backend for Restaurant

This project provides a complete Django backend for a QR menu website for restaurants. Customers can view the menu by scanning a QR code, and administrators can manage products (add, edit, delete) through a user-friendly admin panel.

## Features

- **Menu Display**: Categorized menu for customers to browse
- **Admin Panel**: User-friendly interface for managing menu items
- **Product Management**: Add, edit, delete, and toggle visibility of products
- **Category Organization**: Organize products by categories
- **Image Support**: Add images to products for better visual representation

## Technologies Used

- Django 4.x
- SQLite (default database)
- Bootstrap 5.3
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd qr-menu-django
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations menu
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at: http://127.0.0.1:8000/

## Usage

### Setting Up Categories and Products

1. Access the Django admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created.

2. Add categories first:
   - Navigate to "Categories" and click "Add Category"
   - Create categories such as "Starters", "Main Dishes", "Desserts", "Beverages", etc.

3. Add products to categories:
   - Navigate to "Products" and click "Add Product"
   - Fill in product details including name, description, price, category, and image (optional)
   - Set availability status

### Admin Panel

Access the custom admin panel at http://127.0.0.1:8000/admin/panel/ for a more user-friendly product management interface with:

- Product listing with filtering by category
- Toggle product visibility with a simple switch
- Quick access to edit and delete functions
- Form for adding/editing products with image upload

### Menu Display for Customers

The menu is available at the root URL (http://127.0.0.1:8000/) and can be filtered by category. Generate a QR code for this URL using any QR code generator service and place it on restaurant tables for customers to scan and view the menu.

## Customization

### Frontend Integration

The existing HTML files can be integrated by:

1. Copying static assets (CSS, JS, images) to the `menu/static/menu/` directory
2. Using the Django template system to merge frontend design with backend functionality
3. Updating the URL patterns in `menu/urls.py` to match the existing structure

### Additional Features

To extend this project, you might consider adding:
- Multi-language support
- Online ordering functionality
- Customer reviews and ratings
- Special offers and discounts
- Allergen information

## License

This project is licensed under the MIT License - see the LICENSE file for details.