# Social Media API

This project is a RESTful API for a social media platform designed to handle essential features such as user registration, login, posts, comments, and likes. It provides a secure and scalable backend using token-based authentication.

## 📌 Features

- **User Management**
   - Register a new user
   - Login with token authentication
- **Posts Management**
   - Create a new post
   - Retrieve all posts
- **Comments Management**
   - Add a comment to a post
- **Likes Management**
   - Like a post
   - Unlike a post
   - List users who liked a post

---

## 📦 API Endpoints

### **User Endpoints**
- **Register a User:**  
  `POST /api/users/register/`  
- **Login User:**  
  `POST /api/users/login/`

### **Post Endpoints**
- **Create a Post:**  
  `POST /api/posts/`  
- **Retrieve All Posts:**  
  `GET /api/posts/`

### **Comments Endpoints**
- **Add a Comment:**  
  `POST /api/comments/`

### **Likes Endpoints**
- **Like a Post:**  
  `POST /api/posts/{id}/like/`  
- **Unlike a Post:**  
  `POST /api/posts/{id}/unlike/`  
- **List Likes on a Post:**  
  `GET /api/posts/{id}/likes/`

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <project_directory>

✅ Technologies Used
Python
Django
Django REST Framework
Token-based Authentication
MySQL
PythonWhere for hosting
LINK: https://socialmediaapi.pythonanywhere.com
