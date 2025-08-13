# 🚦 SafeRoute AI

AI-powered safety assistant that helps users assess whether their surroundings are safe — especially for women — with optional real-time location context.

---

## 📌 Features

- 💬 **AI Chat** — Ask safety-related questions and get short, clear answers.  
- 📍 **Location-Aware Advice** — Include your location to receive safety tips relevant to your area.  
- ⚡ **Fast & Minimal UI** — Built with Tailwind CSS for responsive and clean design.  
- 🧠 **Powered by Google Vertex AI (Gemini 2.5 Pro)** — Generates intelligent, context-aware safety suggestions.  

---

## 🛠 Tech Stack

**Frontend**
- HTML + Tailwind CSS
- Vanilla JavaScript (fetch API for requests)

**Backend**
- Python + Flask
- Google Cloud Vertex AI (GenerativeModel – Gemini 2.5 Pro)

---

## 📂 Project Structure

```
SafeRoute-AI/
│
├── templates/
│   └── index.html        # Main UI
│
├── app.py                # Flask backend
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ritesh-2124/saferoute-ai.git
cd saferoute-ai
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set up Google Vertex AI
Ensure you have a Google Cloud Project with Vertex AI API enabled.

Set your GOOGLE_APPLICATION_CREDENTIALS environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
```

### 4️⃣ Run the server
```bash
python app.py
```

Server will be available at:
➡️ http://localhost:5000/

---

## 💡 How It Works

1. User enters a question in the chat box.
2. (Optional) Click Ask with Location to include GPS coordinates.
3. Backend sends question (and location if available) to Google Vertex AI Gemini 2.5 Pro.
4. AI returns a brief, safety-focused response in under 3 sentences.

---

## 🚀 Future Enhancements

- 📊 **Crime Data Integration** — Pull live safety data from government and open data APIs.
- 📢 **Real-Time Alerts** — Notify users about nearby incidents or safety risks.
- 🗺 **Interactive Safety Maps** — Display heatmaps showing safer and riskier zones in the area.
- 🔒 **User Privacy Mode** — Stronger anonymization for location sharing.
- 📱 **Mobile App Version** — Build native Android/iOS apps for better accessibility.
- 🧠 **AI Chat Memory** — Maintain conversation history for more personalized safety advice.
- 🌐 **Multilingual Support** — Provide safety responses in multiple languages.

---

## 📜 License

MIT License © 2025 — Ritesh Yadav