# 🌍 Raw Unwind Safaris

A modern tourism and travel booking platform built with **Django**, designed to showcase safari packages, destinations, accommodations, and provide an easy way for travelers to explore and book unforgettable experiences.

## ✨ Features

- Safari package listings
- Destination showcase
- Accommodation listings
- Contact and inquiry forms
- Responsive design
- Django Admin Dashboard
- PostgreSQL/SQLite support
- Media & static file handling

---

## 🛠 Tech Stack

- Python 3.x
- Django
- HTML5
- CSS3
- JavaScript
- Bootstrap/Tailwind CSS
- PostgreSQL / SQLite

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Kim-Onesmus/raw-unwind.git
cd raw-unwind
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Upgrade pip

```bash
pip install --upgrade pip
```

Install project requirements

```bash
pip install -r requirements.txt
```

---

## 4. Create the Environment File

Create a file named

```
.env
```

in the project's root directory.

Example:

```env
AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 
AWS_STORAGE_BUCKET_NAME = 
# AWS_S3_SIGNATURE_NAME = 
AWS_S3_REGION_NAME = 



DATABASE_URL=

```

## 5. Apply Database Migrations

```bash
python manage.py migrate
```

---

## 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

---

## 7. Collect Static Files

```bash
python manage.py collectstatic
```

---

## 8. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## Access the Admin Panel

Visit

```
http://127.0.0.1:8000/admin/
```

and log in using your superuser credentials.

---




# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Onesmus Kimanzi Muimi**

- 🌐 Portfolio: https://onesmus-kimanzi.vercel.app
- 💼 LinkedIn: https://www.linkedin.com/in/onesmus-muimi-67192026b/
- 📧 Email: kimonesmuske@gmail.com

---

⭐ If you found this project helpful, consider giving it a **star** on GitHub!
