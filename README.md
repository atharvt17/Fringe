# Fringe: Ditch the DMs, Fringe it out!

![Fringe Logo](vdzcall/fringe/static/images/logo.png)

Welcome to **Fringe** - the ultimate solution for seamless video conferencing! Say goodbye to traditional direct messages and embrace the power of **Fringe** for your communication needs.

## Features

- **User Authentication**: Sign up and log in securely to access all the features.
- **Create Rooms**: Hosts can create rooms for video conferences with customizable settings.
- **Real-Time Communication**: Enjoy uninterrupted audio and video communication with WebRTC technology.
- **Screen Sharing**: Share your screen during calls for presentations or collaborative work.
- **Chat Functionality**: Exchange messages in real-time during video conferences.
- **Customizable Settings**: Adjust audio, video, and other settings to suit your preferences.
- **Responsive Design**: Access Fringe seamlessly across various devices.

## How to Use

1. **Sign Up/Login**: Visit the Fringe website and sign up for an account. If you already have an account, simply log in.
2. **Create or Join a Room**: After logging in, create a new room for a video conference or join an existing one using the provided room code.
3. **Start Your Meeting**: Once inside the room, start your video conference by enabling your camera and microphone.
4. **Invite Participants**: Share the room code with participants to join your meeting.
5. **Collaborate**: Enjoy uninterrupted video conferencing with real-time communication, screen sharing, and chat functionality.

## Directory Structure
vdzcall
│   db.sqlite3
│   manage.py
│   requirements.txt
│
├───fringe
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───static
│   │   └───images
│   │           logo.png
│   │           Vectorfavicon.png
│   │
│   └───templates
│           dashboard.html
│           index.html
│           login.html
│           meetingdash.html
│           meetingscreen.html
│           signup.html
│
└───vdzcall
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py


## Installation

To install and run Fringe locally on your machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/atharvt17/Fringe.git
   ```
2. **Navigate to the Directory**:
   ```bash
   cd vdzcall
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Development Server**:
   ```bash
   http://localhost:8000/
   ```

## Technologies Used

- **Frontend**: HTML, TailWind CSS, and JavaScript for creating a dynamic and responsive user interface.
- **Backend**: Django for managing data and user authentication.


Ready to ditch the DMs and Fringe it out? Join us now!
