# 🚀  PRE_IAM + EmojiEmotion Website

This repository contains two components:

1. **PRE_IAM** – Main project (IP-based Pre-IAM Module)
2. **EmojiEmotion** – A sample Django website to demonstrate PRE_IAM integration

Both applications can run **at the same time on different localhost ports** for demonstration purposes.

---

## 📖 Project Overview
- **PRE_IAM** acts as an IP-based pre-authentication filter before Identity and Access Management (IAM).
- **EmojiEmotion** is a sample Django website used to demonstrate PRE_IAM filtering in action.
- Purpose: Secure requests by validating IPs before allowing authentication or access.

---

## ⚡ Methodology (Summary)
- PRE_IAM uses **IP whitelisting/blacklisting** to intercept incoming requests.
- Requests are checked via Django **middleware** before IAM authentication.
- Admins can manage allowed/blocked IPs from the Django admin panel.
- Useful for **cloud integration (AWS/Azure/GCP)** to provide an additional security layer.
- EmojiEmotion acts as a **testing website** to demonstrate how requests are filtered.

---
## 🔧 Installation & Running on Localhost

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/major-project.git
cd major-project
```

### 2️⃣ Setup PRE_IAM
```bash
cd PRE_IAM

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

👉 **Before running**, create a superuser for login:
```bash
python manage.py createsuperuser
```

Run the server:
```bash
python manage.py runserver 5000
```
- PRE_IAM available at: **http://localhost:5000**

---


### 3️⃣ Setup and Run EmojiMotion Website
```bash
cd ../EmojiMotion

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver 8000
```
👉 Django website will be available at **http://localhost:8000**  

---

## 🔗 Running Both Together
- Start **PRE_IAM** → http://localhost:5000  
- Start **Django Website** → http://localhost:8000  
- You can now demonstrate integration and testing live.  

---

# 🌐 Deployment & Local Setup Notes  

## ☁️ Cloud Deployment (Preferred)
- The project is deployed on **Google Cloud App Engine**  
- Two separate instances:  
  - **PRE_IAM** → Handles authentication & IAM module  
  - **EmojiMotion** → Frontend testing website  
- Recommended way for demonstration since networking/IP resolution is handled by GCP.  

---

## 💻 Running Locally (Advanced)  
Running both modules locally requires **manual tunneling**:  

1. **Run PRE_IAM on localhost** (e.g., port 5000)  
2. **Expose PRE_IAM with ngrok**  
   ```bash
   ngrok http 5000
   ```
   👉 Copy the generated public URL (e.g., `https://abc123.ngrok.io`)  

3. **Update EmojiMotion configuration**  
   - In the code where PRE_IAM server address is used (middleware/action settings), replace the cloud endpoint with the ngrok URL.  

   Example (inside `settings.py` or middleware config):  
   ```python
   PRE_IAM_API = "https://abc123.ngrok.io"
   ```

4. **Run EmojiMotion** (port 8000)  
   ```bash
   python manage.py runserver 8000
   ```
   Now it can talk to PRE_IAM through ngrok.  

---

✅ **Summary for Contributors**  
- If you just want to test the system → Use **GCP deployment** (simpler).  
- If you want to develop locally → Be ready to use **ngrok** + change config values in both apps.  

---

## 📜 License
This project is for educational and demonstration purposes only.  
