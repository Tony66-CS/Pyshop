
---

# 🛒 PyShop – E-Commerce System

PyShop is a full-featured e-commerce web application built using **Django** and **Python**.
The system provides essential online shopping functionalities including product browsing, cart management, user authentication, and order processing.

---

## 🚀 Features

* 👤 User Registration & Authentication (Login / Logout)
* 🛍️ Product Listing & Categories
* 🔎 Product Detail View
* 🛒 Shopping Cart Functionality
* 💳 Order Checkout System
* 🗂️ Admin Dashboard for Product Management
* 📦 Order Management
* 📱 Responsive Design

---

## 🛠️ Built With

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default Django DB)
* **Authentication:** Django Built-in Auth System

---

## 📂 Project Structure

```
pyshop/
│── manage.py
│── pyshop/            # Main project settings
│── shop/              # Core e-commerce app
│── templates/         # HTML templates
│── static/            # CSS, JS, Images
│── db.sqlite3
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/pyshop.git
cd pyshop
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

Open your browser at:
`http://127.0.0.1:8000/`

---

## 🔐 Admin Panel

Access the admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials to manage:

* Products
* Categories
* Orders
* Users

---

## 📸 Screenshots

*(Add screenshots of your homepage, product page, cart, and admin dashboard here)*

---

## 📈 Future Improvements

* Online payment integration (Stripe / PayPal)
* Product search & filtering
* Wishlist feature
* REST API integration
* Deployment (Heroku / Render / AWS)

---

## 👨‍💻 Author

**Antwan Fares**
Computer Science Student | Backend Developer
GitHub: [https://github.com/yourusername](https://github.com/yourusername)

---


