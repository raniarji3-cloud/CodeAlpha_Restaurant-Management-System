# Restaurant Management System 🍽️

A backend-based Restaurant Management System built using Django and Django REST Framework.

This project helps manage restaurant operations such as:
- Menu management
- Order processing
- Table reservations
- Inventory tracking
- Daily sales reporting
- Low stock alerts

---

# Features 🚀

## Menu Management
- Add and manage food items
- View available menu items

## Order Management
- Create customer orders
- Automatic total amount calculation
- Order status tracking:
  - Pending
  - Preparing
  - Ready
  - Delivered

## Inventory Management
- Track inventory quantity
- Automatic inventory updates
- Low stock alerts

## Table Reservation System
- Reserve tables
- Prevent booking unavailable tables
- Prevent duplicate reservations for same time

## Reporting System
- Daily sales reports
- Total orders count
- Total sales calculation

## Admin Panel
- Django admin dashboard
- Manage all restaurant operations easily

---

# Tech Stack 🛠️

- Python
- Django
- Django REST Framework
- SQLite

---

# API Endpoints 📌

| Endpoint | Method | Description |
|---|---|---|
| `/menu/` | GET | View menu items |
| `/orders/` | GET, POST | Create and manage orders |
| `/reservations/` | GET, POST | Reserve tables |
| `/reports/daily-sales/` | GET | View daily sales report |
| `/reports/low-stock/` | GET | View low stock alerts |

---

# Installation ⚙️

## Clone Repository

```bash
git clone https://github.com/raniarji3-cloud/CodeAlpha_Restaurant-Management-System.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

---

# Future Improvements 🔥

- Frontend integration using React
- Authentication system
- Online payment integration
- Email notifications

---

# Author 👨‍💻

Developed by Rani Arji