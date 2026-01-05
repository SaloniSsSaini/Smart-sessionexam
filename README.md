# SmartSession – AI-Powered Student Engagement & Proctoring System

SmartSession is a real-time, privacy-first web application designed to help teachers
understand student engagement and integrity during online sessions.

Instead of invasive surveillance, the system focuses on **explainable cognitive signals**
to detect confusion and basic proctoring risks, providing teachers with actionable insights
in real time.

---

## 🔍 Problem Statement

In online education, teachers often lack visibility into:
- When students are confused
- Whether students are attentive
- Basic integrity issues such as no face or multiple faces

SmartSession addresses this gap by offering **live, non-invasive insights**
without recording or storing any student video.

---

## 🧠 Key Features

### 🎓 Student Portal
- Live webcam capture
- Secure WebSocket streaming
- No video or image storage
- No decision-making on the client side

### 🧠 AI Engine (Backend)
- Face count detection (0 / 1 / multiple)
- Gaze direction estimation (LEFT / RIGHT / UP / DOWN / CENTER)
- Custom confusion detection using facial effort signals
- Temporal intelligence to avoid flickering states

### 👩‍🏫 Teacher Dashboard
- Live color-coded student status
- Real-time engagement timeline
- Proctor alerts
- No access to raw video (privacy-by-design)

---

## 🏗️ Architecture Overview



Student Browser
└── Webcam Frames (Base64)
└── FastAPI WebSocket Server
├── Vision Engine (CV + Logic)
├── Temporal State Manager
└── WebSocket Broadcast
└── Teacher Dashboard



---


---

## 🧩 Confusion Detection Logic (Explainable AI)

This system does **not** rely on black-box emotion classification models.

Instead, confusion is treated as a **cognitive state** derived from multiple
facial effort signals inspired by human observation.

### Signals Used

| Signal        | Meaning            | Weight |
|---------------|--------------------|--------|
| Brow Furrow   | Mental effort      | 40     |
| No Smile      | Neutral / tension  | 20     |
| Head Tilt     | Thinking posture   | 10     |
| Lip Press     | Stress indicator   | 15     |
| Eye Squint    | Cognitive load     | 15     |
| **Total**     |                    | **100** |

### Classification Rule
- Confusion Score > **60**
- State must remain stable for **≥ 2.5 seconds**

➡ Student is classified as **CONFUSED**

---

## 🧠 Temporal Intelligence

To avoid rapid state flickering:
- A state must remain consistent for a minimum duration
- Only stable states are broadcast to the teacher dashboard

This ensures clean, reliable, and actionable insights for instructors.

---

## 🔐 Privacy by Design

- All video frames are processed **in memory only**
- No images or videos are stored
- Teachers receive **only derived states**, never raw video feeds

Privacy is enforced by system architecture, not by policy alone.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **Real-time Communication:** WebSockets
- **Computer Vision:** OpenCV (Python 3.11 compatible)
- **Visualization:** Chart.js

---

## ▶️ How to Run the Project

### 1️⃣ Backend
```bash
cd backend
uvicorn server:app --reload



Frontend

Run a simple HTTP server:
cd frontend
python -m http.server 5500


Open in Browser

Student Portal:
http://127.0.0.1:5500/student/index.html

Teacher Dashboard:
http://127.0.0.1:5500/teacher/index.html

🎥 Demo / Integrity Video

A short screen-recorded demo explaining:

End-to-end working of the system

Live confusion detection

Teacher dashboard updates

Privacy guarantees

📹 Video Link:
https://drive.google.com/file/d/1s7fwrmSElJ4vWUsPS73PYQLN3bi3wbSR/view


🚀 Future Improvements

Multi-student session support

Landmark-based gaze tracking

Adaptive confusion thresholds

Teacher feedback loop

🎯 Final Note

SmartSession prioritizes teacher empowerment, student privacy, and
explainable intelligence over surveillance-heavy proctoring systems.
