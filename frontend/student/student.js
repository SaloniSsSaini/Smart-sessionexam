const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const statusText = document.getElementById("status");
const ctx = canvas.getContext("2d");

let socket = null;
let stream = null;

// -------------------- WEBSOCKET --------------------
function connectWebSocket() {
  socket = new WebSocket("ws://127.0.0.1:8000/ws/student");

  socket.onopen = () => {
    statusText.innerText = "🟢 Session Connected";
    startFrameCapture();
  };

  socket.onclose = () => {
    statusText.innerText = "🔴 Session Disconnected";
  };

  socket.onerror = () => {
    statusText.innerText = "❌ WebSocket Error";
  };
}

// -------------------- CAMERA --------------------
async function startCamera() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: false
    });

    video.srcObject = stream;
    statusText.innerText = "🟢 Camera Active";
  } catch (err) {
    statusText.innerText = "❌ Camera Permission Denied";
  }
}

// -------------------- FRAME CAPTURE --------------------
function startFrameCapture() {
  setInterval(() => {
    if (!video.videoWidth || socket.readyState !== WebSocket.OPEN) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const base64Image = canvas
      .toDataURL("image/jpeg", 0.5)
      .split(",")[1];

    socket.send(
      JSON.stringify({
        image: base64Image,
        timestamp: Date.now()
      })
    );
  }, 300); // ~3 FPS (low bandwidth, real-time)
}

// -------------------- CAMERA OFF / TAB CLOSE --------------------
window.addEventListener("beforeunload", () => {
  if (socket && socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({ event: "CAMERA_OFF" }));
  }
});

// -------------------- INIT --------------------
startCamera();
connectWebSocket();
