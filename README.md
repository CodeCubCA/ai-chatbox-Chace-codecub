[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/a2pucUEo)

# 🤖 Multi-Theme AI Chatbot

An intelligent AI assistant built with Streamlit and Groq API, featuring 4 unique themes and 3 personality modes for each theme.

## ✨ Features

- 🎭 **4 Chatbot Themes:**
  - 🎮 Gaming Helper - Gaming strategies, tips, and recommendations
  - 📚 Study Buddy - Learning assistance and homework help
  - 🎵 Music Helper - Music theory, recommendations, and production tips
  - ⚽ Sports Coach - Fitness training and sports techniques

- 🎨 **3 Personality Modes** (per theme):
  - 😊 Friendly - Warm and friendly conversations
  - 🎯/🎓/🎼/🏅 Professional - Expert advice and guidance
  - 😄 Humorous - Fun and entertaining interactions

- 💬 Real-time chat interface with streaming responses
- 🤖 Powered by Groq's llama-3.3-70b-versatile model
- 💾 Chat history support
- 🔄 Dynamic theme and personality switching

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Get your API key from [Groq Console](https://console.groq.com/keys)

3. Edit `.env` file and add your API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
ai-chatbox/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env.example       # Environment variables example
├── .env               # Your environment variables (create this)
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## 💡 Example Questions by Theme

### 🎮 Gaming Helper
- "Best strategy for Elden Ring bosses?"
- "How to improve aim in Valorant?"
- "What's the meta build for League of Legends?"

### 📚 Study Buddy
- "Explain photosynthesis"
- "Help me understand the Pythagorean theorem"
- "What's the difference between lists and tuples in Python?"

### 🎵 Music Helper
- "Recommend albums similar to Pink Floyd"
- "How do I play C major scale on guitar?"
- "Explain the difference between major and minor keys"

### ⚽ Sports Coach
- "Create a beginner running program"
- "How do I improve my basketball shooting?"
- "Best exercises for building core strength"

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq API (llama-3.3-70b-versatile)
- **Environment Management**: python-dotenv

## 📝 Notes

- Make sure your Groq API key is valid and has sufficient quota
- The `.env` file contains sensitive information - never commit it to Git
- It's recommended to run this project in a virtual environment

## 🤝 Contributing

Feel free to submit issues and pull requests!

## 📄 License

MIT License
