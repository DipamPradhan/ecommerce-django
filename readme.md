# 🛒 Mini E-Commerce Inventory (Django)

A simple e-commerce Inventory web application built using **Django** to practice real-world backend concepts like **Custom User Authentication**, **Authorization**, **Product CRUD**, **Image Uploads**, and a **Review & Rating System**.

This project is beginner-friendly and suitable for learning Django fundamentals and CRUD-based web development.

---

## 🚀 Features

### 👤 Accounts & Authentication
- Custom user model (`CustomUser`)
- User signup and login
- Password change and password reset
- Edit profile (including profile image upload)

### 📦 Product Management (CRUD)
- Add, update, delete, and view products
- Product image upload support
- Product listing and product detail pages

### 🔐 Authorization & Security
- Login required to access protected pages (even if the user knows the URL)
- Only the user who created the product can update or delete it

### ⭐ Reviews & Ratings
- Users can add reviews for products
- Ratings from **1 to 5**
- Average rating displayed on product listing

---

## 🧰 Tech Stack

- **Python 3.12**
- **Django 5.0.14**
- **Bootstrap 5**
- **SQLite (default database)**
- **django-crispy-forms**
- **crispy-bootstrap5**
- **Pillow** (for image uploads)

---

## 📂 Project Structure (Apps)

- `accounts` → CustomUser, authentication, profile editing
- `products` → Product CRUD, images, reviews & ratings
- `pages` → Homepage and static pages

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/DipamPradhan/ecommerce-django
cd ecommerce

**Windows:**
python -m venv .venv
.venv\Scripts\activate

**Mac/Linux:**
python3 -m venv .venv
source .venv/bin/activate


### Install Dependecies
pip install -r requirements.txt

### Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Create a superuser
python manage.py createsuperuser

### Run server
python manage.py runserver
**Click:** http://127.0.0.1:8000/

### Admin url
http://127.0.0.1:8000/admin/

## © Copyright
Copyright (c) 2026 DIPAM PRADHAN  
All rights reserved.
