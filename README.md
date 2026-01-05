# SmartSession – AI-Powered Student Engagement & Proctoring System

SmartSession is a real-time, privacy-first education platform that provides teachers
with live insights into student engagement and integrity during online sessions.
Instead of invasive surveillance, the system focuses on explainable cognitive signals
to detect confusion and proctoring risks.

---

## 🔍 Problem Statement

Online education lacks real-time feedback on:
- When students are confused
- Whether attention is maintained
- Basic integrity issues (no face / multiple faces)

SmartSession solves this by offering teachers “Super Vision” through
non-invasive, explainable AI signals.

---

## 🧠 Key Features

### Student Portal
- Live webcam capture
- Secure WebSocket streaming
- No video storage
- No on-device decision making

### AI Engine (Backend)
- Face count detection (0 / 1 / multiple)
- Gaze direction estimation (LEFT / RIGHT / UP / DOWN / CENTER)
- Custom confusion detection using facial effort signals
- Temporal intelligence to prevent flickering

### Teacher Dashboard
- Live color-coded status
- Real-time engagement timeline
- Proctor alerts
- No raw video access (privacy-first)

---

## 🏗️ Architecture Overview

Student Browser
└── Webcam Frames (Base64)
└── FastAPI WebSocket Server
├── Vision Engine (CV + Logic)
├── Temporal State Manager
└── WebSocket Broadcast
└── Teacher Dashboard

yaml
Copy code

---

## 🧩 Confusion Detection Logic (Explainable AI)

Unlike black-box emotion models, confusion is defined as a **cognitive state**
derived from multiple facial effort signals.

### Signals Used

| Signal | Meaning | Weight |
|------|--------|--------|
| Brow Furrow | Mental effort | 40 |
| No Smile | Neutral / tension | 20 |
| Head Tilt | Thinking posture | 10 |
| Lip Press | Stress | 15 |
| Eye Squint | Cognitive load | 15 |
| **Total** | | **100** |

### Rule

- Confusion Score > 60
- Stable for ≥ 2.5 seconds

➡ Student classified as **CONFUSED**

---

## 🧠 Temporal Intelligence

To avoid flickering:
- A state must remain stable for a minimum duration
- Only stable states are broadcast to teachers

This ensures clean, actionable insights.

---

## 🔐 Privacy by Design

- Video frames are processed **in-memory only**
- No images or videos are stored
- Teachers receive **only derived states**, never raw feeds

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- Communication: WebSockets
- Computer Vision: OpenCV (Python 3.11 compatible)
- Charts: Chart.js

---

## ▶️ How to Run

### Backend
```bash
cd backend
uvicorn server:app --reload
Student Portal
Open:

bash
Copy code
frontend/student/index.html
Teacher Dashboard
Open:

bash
Copy code
frontend/teacher/index.html
🚀 Future Improvements
Multi-student sessions

Landmark-based gaze tracking

Adaptive confusion thresholds

Teacher feedback loop

🎯 Final Note
This system prioritizes teacher empowerment, student privacy, and
explainable intelligence over surveillance.

yaml
Copy code

---

