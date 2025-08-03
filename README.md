# 🏛️ Court-Data Fetcher & Mini-Dashboard

This is a Flask-based web app that allows users to enter details of a case (Case Type, Number, and Filing Year) and fetch the latest metadata and judgment/order information from the **Delhi High Court website**.

> 🔥 Built as part of my first internship test challenge — goal: full-stack automation and real-time data display from a public legal source.

---

## 📌 Features

- ✅ Clean HTML form for user input
- ✅ Beautiful law-themed UI with background image
- ✅ Backend logic in Python using Flask
- ✅ Ready to integrate web scraping for Delhi HC data
- ✅ Secure structure with database and future PDF download support

---

## 🚀 Tech Stack

| Layer        | Tech Used          |
|--------------|--------------------|
| Frontend     | HTML + CSS         |
| Backend      | Python + Flask     |
| Styling      | Custom CSS (with background image) |
| Deployment   | Localhost / GitHub |
| Versioning   | Git + GitHub       |

---

## 🧰 Setup Instructions

🔹 Step 1: Clone the Repo
git clone https://github.com/Loki22-glich/court-dashboard.git
cd court-dashboard

🔹 Step 2: Install Flask
pip install flask
🔹 Step 3: Run the App
python app.py
Visit in browser: http://127.0.0.1:5000

🖼️ Preview

Background image from a legal theme for aesthetics and professional appeal.

📦 Folder Structure
court-dashboard/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Form UI
├── static/
│   ├── law-image.jpg       # Background image
│   └── style.css           # CSS styling

🚧 To-Do (Next Steps)
 Add web scraping logic using Selenium or Playwright

 Parse party names, dates, and latest PDF link

 Store user queries in SQLite DB

 Handle CAPTCHA bypass legally

 Add user-friendly error messages

🙋 About Me
👨‍💻 Name: Banoth Lokesh
🎓 Institute: IIT Madras
💡 Role: Python Developer Intern (Applicant)

I’m passionate about real-world tools, automation, and software that solves problems.

📝 License
MIT License — Feel free to use and improve!
