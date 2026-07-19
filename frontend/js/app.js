const BACKEND_URL = "http://127.0.0.1:5000/api"; // Render link deploy hone par yahan change hoga
let currentDocId = null;

const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const mainDashboard = document.getElementById('main-dashboard');
const fileStatus = document.getElementById('file-status');

// Click setup to upload
dropZone.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', async (e) => {
    if (e.target.files.length === 0) return;
    const file = e.target.files[0];
    fileStatus.textContent = `Uploading ${file.name}... Please wait.`;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const res = await fetch(`${BACKEND_URL}/upload`, { method: 'POST', body: formData });
        const data = await res.json();
        
        if (res.ok) {
            currentDocId = data.documentId;
            fileStatus.textContent = "Upload successful! Analyzing content...";
            mainDashboard.style.display = "grid"; // Grid visible karein
            
            // UI dynamically data fill up karegi
            renderInsights(data.insights);
            renderQuestions(data.questions);
        } else {
            fileStatus.textContent = `Error: ${data.message}`;
        }
    } catch (err) {
        fileStatus.textContent = "Server connection failed.";
    }
});

function renderInsights(insights) {
    const list = document.getElementById('insights-list');
    list.innerHTML = insights.map(item => `<li>${item}</li>`).join('');
}

function renderQuestions(questions) {
    const box = document.getElementById('questions-box');
    box.innerHTML = questions.map((q, idx) => `<p style='margin-bottom:10px;'><strong>Q${idx+1}:</strong> ${q}</p>`).join('');
}

// Chat Functionality
document.getElementById('btn-send').addEventListener('click', async () => {
    const input = document.getElementById('chat-input');
    const query = input.value.trim();
    if (!query || !currentDocId) return;

    appendMessage(query, 'user-msg');
    input.value = '';

    try {
        const res = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ documentId: currentDocId, message: query })
        });
        const data = await res.json();
        appendMessage(data.reply, 'bot-msg');
    } catch {
        appendMessage("Failed to get response from agent.", 'bot-msg');
    }
});

function appendMessage(text, className) {
    const box = document.getElementById('chat-box');
    const msg = document.getElementById('chat-box');
    const div = document.createElement('div');
    div.className = className;
    div.textContent = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
