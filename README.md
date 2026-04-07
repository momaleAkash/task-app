# 🚀 Task Manager App (Full Stack)

A **production-ready full-stack application** built using modern technologies with clean architecture, authentication, caching, and deployment.

---

## 🧱 Architecture

* **Frontend:** React (Vite + TailwindCSS + React Query)
* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
* **Cache:** Redis
* **Deployment:** Railway (Backend) + Vercel (Frontend)

---

## ✨ Features

* 🔐 JWT Authentication (Login/Register)
* 📋 Task Management (CRUD operations)
* ⚡ Redis Caching for performance
* 🧱 Clean Architecture (Controller → Service → Repository)
* 📦 REST APIs with FastAPI
* 🎯 React Query for efficient data fetching
* 🌍 Fully deployed & accessible online
* 🐳 Dockerized backend (optional)

---

## 📁 Project Structure

```
task-app/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repository/
│   │   ├── services/
│   │   └── main.py
│   ├── alembic/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── hooks/
│   │   ├── pages/
│   │   └── components/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

👉 API Docs:
http://localhost:8000/docs

---

## 🎨 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

👉 App runs on:
http://localhost:5173

---

## 🔑 Environment Variables

### Backend (`.env`)

```
DATABASE_URL=your_postgres_url
REDIS_URL=your_redis_url
SECRET_KEY=your_secret
```

---

### Frontend (`.env`)

```
VITE_API_URL=http://localhost:8000/api
```

---

## 🚀 Deployment

### Backend → Railway

* Deploy via GitHub
* Add environment variables
* Connect PostgreSQL & Redis services

---

### Frontend → Vercel

* Import GitHub repo
* Set `VITE_API_URL`
* Deploy

---

## 🔗 Live URLs (Add after deployment)

* 🌍 Frontend: https://your-app.vercel.app
* ⚙️ Backend: https://your-app.up.railway.app
* 📘 API Docs: https://your-app.up.railway.app/docs

---

## 🧠 Key Concepts Used

* Dependency Injection (FastAPI Depends)
* Repository Pattern
* Service Layer Architecture
* JWT Authentication
* Caching with Redis
* API Integration with Axios
* State Management with React Query

---

## 📸 Screenshots (Optional)

*Add screenshots of UI here*

---

## 🧑‍💻 Author

**Akash Momale**

---

## ⭐ Acknowledgements

This project demonstrates a **real-world industry-ready full-stack architecture** suitable for production deployment.

---
