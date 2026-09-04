# 🍽️ Restaurant Management System

A full-stack **Restaurant Management System** built with **Django** and **Django REST Framework** that provides a centralized platform for managing restaurant food items, menus, customer carts, orders, and restaurant-related data.

The application combines a dynamic web interface with a powerful Django backend, database integration, and RESTful APIs to provide a practical solution for digitizing restaurant operations.

---

## ✨ Overview

Managing restaurant operations manually can make it difficult to maintain food items, prices, customer selections, carts, and orders efficiently.

The **Restaurant Management System** provides a centralized platform where restaurant data and customer interactions can be managed digitally.

The application allows users to:

- Browse restaurant food items
- View food item details and images
- Add food items to a shopping cart
- Manage cart items and quantities
- Place and manage orders
- Retrieve restaurant data through REST APIs
- Manage restaurant information through Django Admin
- Store application data in a relational database

The project was developed to demonstrate practical experience in **full-stack web development, Django, REST API development, database management, and deployment**.

---

## 🎯 Key Features

### 🍴 Restaurant Menu

- Display available food items
- Display food item names
- Display food item prices
- Display food item images
- Dynamically retrieve menu information from the database
- Organize restaurant food information efficiently

### 🛒 Shopping Cart

- Add food items to the cart
- View selected food items
- Display item quantities
- Update cart items
- Remove items from the cart
- Calculate cart-related information
- Maintain selected food items during the ordering process

### 📦 Order Management

- Create customer orders
- Store order information in the database
- Manage ordered food items
- Retrieve order information
- Connect customer selections with order processing

### 🔌 REST API

The project uses **Django REST Framework (DRF)** to provide RESTful API functionality.

The API layer supports:

- Data retrieval
- Data creation
- Data updating
- Data deletion
- Serialization
- Data validation
- JSON-based API responses

### 🗄️ Database Management

- Django models for application data
- Django ORM for database interaction
- Database migrations
- CRUD operations
- Structured relational data management

### 👨‍💼 Django Admin

The built-in Django administration interface provides a convenient way to manage restaurant-related data.

Administrators can manage registered application models directly through the Django Admin panel.

### 🖥️ Dynamic Web Application

- Django template-based frontend
- Dynamic database-driven content
- HTML5
- CSS3
- JavaScript
- Responsive web interface

---

## 🛠️ Technology Stack

### Backend

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Django** | Web framework |
| **Django REST Framework** | REST API development |
| **Django ORM** | Database interaction |

### Frontend

| Technology | Purpose |
|---|---|
| **HTML5** | Page structure |
| **CSS3** | Styling and layout |
| **JavaScript** | Client-side functionality |
| **Django Templates** | Dynamic page rendering |

### Database

| Technology | Purpose |
|---|---|
| **SQLite** | Development database |
| **Django ORM** | Database abstraction and queries |

### Development Tools

| Tool | Purpose |
|---|---|
| **Git** | Version control |
| **GitHub** | Source code management |
| **VS Code** | Development environment |
| **pip** | Python package management |
| **Virtual Environment** | Dependency isolation |

### Deployment

| Technology | Purpose |
|---|---|
| **Render** | Cloud deployment |
| **Gunicorn / WSGI** | Production application serving |
| **build.sh** | Deployment build configuration |
| **render.yaml** | Render deployment configuration |

---


## ⚙️ Installation & Setup

🔧 Quick Start

git clone https://github.com/YOUR-USERNAME/CodeAlpha_Restaurant-Management-System.git

cd CodeAlpha_Restaurant-Management-System

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Then open:

http://127.0.0.1:8000/

##📋 Requirements

Before running the project, make sure the following are installed:

Python
pip
Git
A modern web browser
Internet connection for installing dependencies


##👩‍💻 Author
Rani Arji

B.Tech Computer Science & Engineering

Full-Stack Django Developer

Connect with me
💻 GitHub: Your GitHub Profile
💼 LinkedIn: Your LinkedIn Profile
⭐ Support

If you found this project interesting or useful, consider giving the repository a ⭐ on GitHub.
