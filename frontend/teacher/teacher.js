const statusText = document.getElementById("statusText");
const statusReason = document.getElementById("statusReason");
const statusCard = document.getElementById("statusCard");

// -------------------- CHART SETUP --------------------
const ctx = document.getElementById("timelineChart").getContext("2d");

const timelineData = {
  labels: [],
  datasets: [{
    label: "Engagement Level",
    data: [],
    borderWidth: 2,
    fill: false
  }]
};

const chart = new Chart(ctx, {
  type: "line",
  data: timelineData,
  options: {
    responsive: true,
    scales: {
      y: {
        min: 0,
        max: 2,
        ticks: {
          callback: (value) => {
            if (value === 0) return "Confused";
            if (value === 1) return "Focused";
            if (value === 2) return "Alert";
          }
        }
      }
    }
  }
});

// -------------------- WEBSOCKET --------------------
const socket = new WebSocket("ws://127.0.0.1:8000/ws/teacher");

socket.onopen = () => {
  statusText.innerText = "🟢 Connected";
};

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateStatus(data);
  updateChart(data);
};

socket.onclose = () => {
  statusText.innerText = "🔴 Disconnected";
};

// -------------------- STATUS UPDATE --------------------
function updateStatus(data) {
  statusCard.className = "status-card";

  if (data.status === "PROCTOR_ALERT") {
    statusCard.classList.add("red");
    statusText.innerText = "🔴 Proctor Alert";
    statusReason.innerText = data.reason || "Integrity issue detected";
    return;
  }

  if (data.status === "CONFUSED") {
    statusCard.classList.add("yellow");
    statusText.innerText = "🟡 Student Confused";
    statusReason.innerText = `Confusion Score: ${Math.round(data.score)}`;
    return;
  }

  if (data.status === "FOCUSED") {
    statusCard.classList.add("green");
    statusText.innerText = "🟢 Student Focused";
    statusReason.innerText = "";
  }
}

// -------------------- TIMELINE UPDATE --------------------
function updateChart(data) {
  const time = new Date().toLocaleTimeString();

  let value = 1; // Focused
  if (data.status === "CONFUSED") value = 0;
  if (data.status === "PROCTOR_ALERT") value = 2;

  timelineData.labels.push(time);
  timelineData.datasets[0].data.push(value);

  if (timelineData.labels.length > 20) {
    timelineData.labels.shift();
    timelineData.datasets[0].data.shift();
  }

  chart.update();
}
