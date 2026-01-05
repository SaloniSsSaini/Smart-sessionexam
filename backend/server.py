from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import cv2
import base64
import numpy as np

from websocket.connection_manager import ConnectionManager
from vision_engine.face_detection import FaceDetector
from vision_engine.micro_expressions import MicroExpressionAnalyzer
from vision_engine.confusion_logic import ConfusionDetector
from vision_engine.state_manager import StateManager

# ---------------- APP & MANAGERS ----------------
app = FastAPI()
manager = ConnectionManager()

face_detector = FaceDetector()
micro_expr = MicroExpressionAnalyzer()
confusion_detector = ConfusionDetector()
state_manager = StateManager()

# ---------------- STUDENT WEBSOCKET ----------------
@app.websocket("/ws/student")
async def student_ws(websocket: WebSocket):
    await manager.connect_student(websocket)
    print("🟢 Student connected")

    try:
        while True:
            data = await websocket.receive_json()

            # -------- Safety Check --------
            if "image" not in data:
                continue

            # -------- Decode Frame --------
            img_bytes = base64.b64decode(data["image"])
            np_arr = np.frombuffer(img_bytes, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if frame is None:
                continue

            # -------- Face Detection --------
            face_count = face_detector.detect_faces(frame)

            if face_count != 1:
                await manager.broadcast_to_teachers({
                    "status": "PROCTOR_ALERT",
                    "reason": "FACE_COUNT"
                })
                continue

            # -------- Micro Expressions --------
            h, w, _ = frame.shape
            face_box = (0, 0, w, h)  # simplified face region

            signals = micro_expr.analyze(face_box)

            score = confusion_detector.compute_score(signals)
            state = confusion_detector.classify(score)

            # -------- Temporal State --------
            stable_state = state_manager.update(state)

            # -------- 🔥 HEARTBEAT FIX (MOST IMPORTANT) --------
            # Always send live update so teacher dashboard updates
            await manager.broadcast_to_teachers({
                "status": state,
                "score": score
            })

            print(f"📡 Broadcast → {state} | Score: {score}")

    except WebSocketDisconnect:
        manager.disconnect_student(websocket)
        print("🔴 Student disconnected")


# ---------------- TEACHER WEBSOCKET ----------------
@app.websocket("/ws/teacher")
async def teacher_ws(websocket: WebSocket):
    print("🟢 Teacher trying to connect")
    await manager.connect_teacher(websocket)
    print("🟢 Teacher connected")

    try:
        while True:
            await websocket.receive_text()  # keep connection alive
    except WebSocketDisconnect:
        print("🔴 Teacher disconnected")
        manager.disconnect_teacher(websocket)
