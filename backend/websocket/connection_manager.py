from typing import List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.students: List[WebSocket] = []
        self.teachers: List[WebSocket] = []

    # ---------- Student ----------
    async def connect_student(self, websocket: WebSocket):
        await websocket.accept()
        self.students.append(websocket)

    def disconnect_student(self, websocket: WebSocket):
        if websocket in self.students:
            self.students.remove(websocket)

    # ---------- Teacher ----------
    async def connect_teacher(self, websocket: WebSocket):
        await websocket.accept()
        self.teachers.append(websocket)

    def disconnect_teacher(self, websocket: WebSocket):
        if websocket in self.teachers:
            self.teachers.remove(websocket)

    # ---------- Broadcast ----------
    async def broadcast_to_teachers(self, message: dict):
        for teacher in self.teachers:
            await teacher.send_json(message)
