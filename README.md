# WeSocial-socialmedia-application
🚀 Features 

    👤 User Authentication  
        Register/Login with email and password  
        Profile setup with bio, profile picture, cover photo  
        
    🧑‍🤝‍🧑 Friend System  
        Send and accept friend requests  
        View mutual friends  
        
    📝 Post System  
        Create text/image posts  
        Like and comment on posts  
        Edit/Delete own posts  
        
🛠️ Tech Stack
    Layer	                        Technology
    Backend	                      Django
    Frontend	                    HTML, CSS, JavaScript, Bootstrap
    Database	                    SQLite
    Auth	                        Django Auth
    Media Storage	                Local

📂 Folder Structure (Sample)
    bash

    /we_social
    /profiles         # User auth and profile
    /posts            # Post creation, like, comment
    /static_project   # CSS, JS, Images
    /templates        # HTML Templates
    manage.py
    settings.py

🧑‍💻 Getting Started
    Prerequisites
    Python 3.x
    
    pip
    
    virtualenv
Setup
  bash

  git clone https://github.com/your-username/socialmedia-app.git
  cd socialmedia-app
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

Admin Login
  Go to /admin/ to access the admin panel.

  Create a superuser:
    
