# 📚 Study Buddy - AI Learning Assistant

An intelligent learning companion built with Streamlit and Groq API to help you with your studies, understand concepts, and get homework help.

## ✨ Features

- 💬 Real-time chat interface
- 🤖 Powered by Groq's llama-3.3-70b-versatile model
- 📖 Focused on learning and education
- 🎨 Clean and intuitive Streamlit interface
- 💾 Chat history support
- 🔄 Streaming responses for real-time interaction

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

## 💡 Example Questions

- "Explain photosynthesis"
- "Help me understand the Pythagorean theorem"
- "What's the difference between lists and tuples in Python?"
- "How can I improve my memory?"
- "Explain quantum mechanics in simple terms"

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
