# College Lost and Found Forum

A web-based platform built with Django for college students and staff to report, track, and claim lost and found items within the campus community.

## 🚀 Features

- **User Authentication**: Secure Sign Up, Log In, and Log Out functionality.
- **Report Items**: Easily register lost or found items with a title, description, location, category, and image upload.
- **Categorization**: Items are organized into distinct categories:
  - Devices (Phones, Laptops, Tablets, etc.)
  - Documents (Student IDs, Passports, Notebooks, etc.)
  - Accessories (Keys, Wallets, Bags, etc.)
  - Clothing (Jackets, Hats, Footwear, etc.)
  - Stationery (Art supplies, Calculators, etc.)
  - Miscellaneous/Other
- **Dashboard**: A personalized user dashboard to manage, edit, or delete reported items.
- **Claiming System**: Users can claim found items directly through the portal, which links the claim to their account.
- **Mobile-Responsive UI**: Clean interface built using Bootstrap.

---

## 🛠️ Tech Stack

- **Backend**: Python & Django 6.0
- **Database**: SQLite (Development)
- **Frontend**: Bootstrap 4, HTML5, CSS3
- **Media Storage**: Pillow (Python Imaging Library)
- **Deployment Ready**: Vercel configuration (`vercel.json`) included.

---

## ⚙️ Installation & Local Setup

### Prerequisites
- Python 3.10+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Athility/college-lost-and-found-forum.git
cd college-lost-and-found-forum
```

### 2. Set Up a Virtual Environment
**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
Generate and apply database migrations to set up the SQLite database:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django Admin Portal (`/admin`):
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📂 Project Structure

```text
├── lost_found/           # Django Application containing core logic
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates (Home, Login, Register, Dashboard, etc.)
│   ├── admin.py          # Django Admin configuration
│   ├── models.py         # Item and status database models
│   ├── urls.py           # App routing patterns
│   └── views.py          # Controller functions for pages and actions
├── mysite/               # Django Project configuration folder
│   ├── settings.py       # Global settings
│   ├── urls.py           # Main routing configuration
│   └── wsgi.py/asgi.py   # Web server gateway interfaces
├── manage.py             # Django command-line utility
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies list
└── README.md             # Project documentation
```

---

## ☁️ Deployment

This project includes a `vercel.json` configuration and is ready to deploy directly to [Vercel](https://vercel.com).
Ensure you configure environment variables and Django static settings properly for production environments.
