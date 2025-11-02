# 🤖 AI Chatbox - Multi-Theme Intelligent Assistant

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=streamlit)](https://ai-chatbox-Chace-codecub.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/CodeCubCA/ai-chatbox-Chace-codecub)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

An intelligent AI-powered chatbot built with Streamlit and Groq API, featuring 4 unique themes (Gaming, Study, Music, Sports) and 3 customizable personality modes for each theme. Perfect for students seeking instant help with homework, gamers looking for strategies, music enthusiasts exploring theory, and fitness seekers wanting workout guidance.

![AI Chatbox Preview](img/AI-Chatbot.png)

---

## ✨ Features

### 🎭 Four Unique Chatbot Themes

#### 1. 🎮 Gaming Helper
Your ultimate gaming companion for dominating the game!
- **Game strategies & tips** - Master tactics and winning strategies
- **Walkthroughs & guides** - Get unstuck and find hidden secrets
- **Character builds & loadouts** - Optimize your setup for victory
- **Competitive advice** - Improve your skills and climb the ranks
- **Game recommendations** - Discover new games you'll love

#### 2. 📚 Study Buddy
Your personal learning companion to ace your studies!
- **Understanding difficult concepts** - Break down complex topics
- **Homework help** - Step-by-step problem guidance
- **Exam preparation** - Study strategies and practice questions
- **Learning tips** - Effective study techniques and memory tricks

#### 3. 🎵 Music Helper
Your ultimate music companion for discovery and learning!
- **Music theory & techniques** - Learn chords, scales, and fundamentals
- **Song recommendations** - Discover new music based on your taste
- **Instrument guidance** - Tips for guitar, piano, drums, and more
- **Artist & genre exploration** - Deep dives into music history
- **Production tips** - Music production, mixing, and recording advice

#### 4. ⚽ Sports Coach
Your personal fitness and sports companion!
- **Training programs & workouts** - Customized fitness routines
- **Sports techniques & strategies** - Master skills in your favorite sports
- **Nutrition & recovery** - Fuel your body and recover like a pro
- **Performance tips** - Improve speed, strength, and endurance
- **Goal setting & motivation** - Stay focused and achieve your dreams

---

### 🎨 Three Personality Modes (Per Theme)

Each theme supports three distinct personalities to match your preference:

#### 😊 Friendly Mode
- Warm and supportive conversations
- Encouraging words and positive reinforcement
- Casual, relatable language
- Celebrates your progress and victories
- Like chatting with a supportive friend

#### 🎯 Professional Mode
- Expert-level guidance and advice
- Precise terminology and technical accuracy
- Well-structured explanations
- Comprehensive and reliable information
- Maintains scholarly yet accessible tone

#### 😄 Humorous Mode
- Fun and entertaining interactions
- Light humor and witty commentary
- Playful banter and jokes
- Creative analogies and examples
- Makes learning and conversations enjoyable

---

### 💬 Advanced Chat Features

- **Real-time Streaming Responses** - See AI responses appear word-by-word
- **Context Awareness** - AI remembers your conversation history
- **Chat History Management** - Review previous messages and clear when needed
- **Dynamic Theme Switching** - Change themes without losing conversation flow
- **Personality Customization** - Switch between personalities mid-conversation
- **Message Counter** - Track conversation length
- **Keyboard Shortcuts** - Quick access to common functions
- **Mobile Responsive** - Works seamlessly on all devices

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Groq API key ([Get one here](https://console.groq.com/keys))

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/CodeCubCA/ai-chatbox-Chace-codecub.git
cd ai-chatbox-Chace-codecub
```

#### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure API Key

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Get your API key from [Groq Console](https://console.groq.com/keys)

3. Edit `.env` file and add your key:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

#### 5. Run the Application
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
ai-chatbox/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your API key (create this, not in git)
├── .gitignore           # Git ignore rules
├── img/                 # Screenshots and images
│   └── AI-Chatbot.png  # App preview image
├── .github/             # GitHub configuration
│   └── workflows/       # CI/CD workflows
└── README.md            # This documentation
```

---

## 🛠️ Technologies Used

### Backend & Framework
- **Python 3.8+** - Core programming language
- **Streamlit 1.31.0** - Web application framework for rapid development
- **python-dotenv 1.0.0** - Environment variable management

### AI & API
- **Groq API 0.33.0** - Fast AI inference with llama-3.3-70b-versatile model
- **llama-3.3-70b-versatile** - Advanced language model for natural conversations
- **Streaming Support** - Real-time response generation

### Deployment
- **Streamlit Cloud** - Serverless deployment platform
- **GitHub Integration** - Continuous deployment from repository
- **Automatic HTTPS** - Secure connections by default

---

## 💡 How It Works

### Architecture Overview

```
User Input → Streamlit Interface → Groq API → llama-3.3 Model → Streaming Response → Display
                                      ↓
                                System Prompt (Theme + Personality)
                                      ↓
                                Context from Chat History
```

### System Prompt Engineering

Each theme has three carefully crafted system prompts (one per personality mode). These prompts define:

1. **Role Definition** - Who the AI assistant is
2. **Tone & Style** - How it communicates
3. **Expertise Areas** - What it specializes in
4. **Response Format** - How it structures answers

Example for Gaming Helper (Friendly Mode):
```python
"You are Gaming Helper, a warm and friendly gaming companion! Chat with gamers
like a supportive friend who shares their passion for games. Use encouraging words,
celebrate their victories, and relate to their gaming challenges..."
```

### Chat Flow

1. **User sends message** → Added to chat history
2. **System prompt selected** → Based on current theme + personality
3. **API request sent** → Includes system prompt + full chat history
4. **Response streamed** → Displayed word-by-word for better UX
5. **History updated** → Response added to conversation

---

## 🎯 Usage Examples

### Example Conversations

#### �� Gaming Helper - Friendly Mode
```
User: "I keep dying to Malenia in Elden Ring!"
AI: "Oh man, I feel you! Malenia is TOUGH! 😅 But don't worry, let me share
some strategies that helped me beat her. First, patience is key - she's all
about reading her patterns..."
```

#### 📚 Study Buddy - Professional Mode
```
User: "Explain how photosynthesis works"
AI: "Photosynthesis is the biochemical process by which plants convert light
energy into chemical energy. The process occurs in two main stages:
1. Light-dependent reactions (in thylakoid membranes)
2. Light-independent reactions (Calvin cycle in stroma)..."
```

#### 🎵 Music Helper - Humorous Mode
```
User: "How do I get better at guitar?"
AI: "Ah, the age-old question! 🎸 Well, step 1: practice. Step 2: practice more.
Step 3: wonder why your fingers hurt. Step 4: realize you're getting better!
😄 But seriously, here's what actually works..."
```

#### ⚽ Sports Coach - Friendly Mode
```
User: "I want to start running but don't know where to begin"
AI: "That's awesome that you want to start running! 🏃 It's such a great way
to stay fit and clear your mind. Let's start you off easy with a beginner-
friendly plan that won't overwhelm you..."
```

---

## 🔧 Configuration & Customization

### Adding New Themes

To add a new chatbot theme, edit `app.py` and add to `chatbot_configs`:

```python
chatbot_configs = {
    # ... existing themes ...
    "YourTheme": {
        "title": "🎭 Your Theme Title",
        "subtitle": "Your subtitle here",
        "icon": "🎭",
        "welcome": "Your welcome message...",
        "prompts": {
            "Friendly": "Your friendly system prompt...",
            "Professional": "Your professional system prompt...",
            "Humorous": "Your humorous system prompt..."
        },
        "tips": """Your usage tips..."""
    }
}
```

### Modifying AI Behavior

Edit the system prompts in `chatbot_configs` to change how the AI responds:

```python
"prompts": {
    "Friendly": "Modify this to change friendly mode behavior",
    "Professional": "Modify this to change professional mode behavior",
    "Humorous": "Modify this to change humorous mode behavior"
}
```

### Changing AI Model

To use a different Groq model, modify the API call in `app.py`:

```python
stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Change this to another model
    messages=api_messages,
    temperature=0.7,  # Adjust creativity (0.0-1.0)
    max_tokens=2048,  # Adjust response length
    stream=True
)
```

Available Groq models:
- `llama-3.3-70b-versatile` (Current) - Fast and versatile
- `llama-3.1-8b-instant` - Very fast, good for simple queries
- `mixtral-8x7b-32768` - Large context window
- `gemma2-9b-it` - Google's efficient model

---

## 📊 Performance & Limitations

### Performance Metrics
- **Response Time:** 1-3 seconds (depending on response length)
- **Token Limit:** 2048 tokens per response
- **Context Memory:** Full conversation history
- **Concurrent Users:** Unlimited (Streamlit Cloud handles scaling)
- **API Rate Limits:** Based on Groq account tier

### Known Limitations
1. **No Image Support** - Text-only conversations
2. **No File Uploads** - Cannot analyze documents or images
3. **Memory Persistence** - Chat history lost on page refresh
4. **Internet Knowledge** - Model trained on data up to 2023
5. **API Dependency** - Requires active Groq API key

### Future Improvements
- [ ] Add chat history persistence (database)
- [ ] Implement user authentication
- [ ] Add conversation export (PDF/TXT)
- [ ] Support file uploads for analysis
- [ ] Add voice input/output
- [ ] Implement multi-language support
- [ ] Add conversation branching
- [ ] Create mobile app version

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] All 4 themes load correctly
- [ ] All 3 personalities work for each theme
- [ ] Theme switching preserves settings
- [ ] Chat history displays properly
- [ ] Clear chat button works
- [ ] Streaming responses appear smoothly
- [ ] Mobile responsive design works
- [ ] Error handling for API failures

### Test Different Scenarios
```bash
# Test with invalid API key
GROQ_API_KEY=invalid_key streamlit run app.py

# Test with no API key
# Remove GROQ_API_KEY from .env and run

# Test on different devices
# Use browser dev tools to test mobile views
```

---

## 🚀 Deployment

### Deploying to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repository
   - Choose `main` branch and `app.py`

3. **Configure Secrets**
   - Click "Advanced settings"
   - Add your secrets in TOML format:
     ```toml
     GROQ_API_KEY = "your_api_key_here"
     ```

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment (usually 2-3 minutes)
   - Your app is live!

### Custom Domain Setup
1. Purchase domain from registrar (Namecheap, GoDaddy, etc.)
2. In Streamlit Cloud settings, add custom domain
3. Add CNAME record in DNS settings pointing to Streamlit
4. Wait for SSL certificate (automatic)

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "Error: Could not read API key"
**Solution:**
1. Check `.env` file exists
2. Verify `GROQ_API_KEY` is set correctly
3. No quotes around the API key
4. Restart the application

#### Issue: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

#### Issue: "API Rate Limit Exceeded"
**Solution:**
- Wait for rate limit to reset
- Upgrade your Groq account tier
- Reduce message frequency

#### Issue: "Streamlit Won't Start"
**Solution:**
```bash
# Kill existing Streamlit processes
pkill -f streamlit

# Clear Streamlit cache
streamlit cache clear

# Try running again
streamlit run app.py
```

#### Issue: "Slow Response Times"
**Solution:**
- Check internet connection
- Try a faster model (llama-3.1-8b-instant)
- Reduce max_tokens in API call
- Check Groq API status

---

## 📝 API Documentation

### Groq API Basics

#### Authentication
```python
from groq import Groq
client = Groq(api_key="your_api_key")
```

#### Making Requests
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7,
    max_tokens=1024,
    stream=True  # Enable streaming
)
```

#### Handling Streaming Responses
```python
for chunk in response:
    if chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        print(content, end="")
```

---

## 🔒 Security Best Practices

### API Key Security
- ✅ **Never commit `.env` to Git** - Already in `.gitignore`
- ✅ **Use environment variables** - Implemented with python-dotenv
- ✅ **Rotate keys regularly** - Change API key every 3-6 months
- ✅ **Use separate keys** - Different keys for dev/prod
- ❌ **Don't hardcode keys** - Never put keys directly in code

### User Data Privacy
- No user data is stored permanently
- Chat history exists only in current session
- No analytics or tracking implemented
- No personal information collected
- All communication over HTTPS

---

## 📈 Project Statistics

### Code Metrics
- **Total Lines of Code:** ~310 lines
- **Python Files:** 1 (app.py)
- **Configuration Files:** 4 (.env, .gitignore, requirements.txt, README)
- **Dependencies:** 3 (streamlit, groq, python-dotenv)

### Development Timeline
- **Planning:** 2 days
- **Initial Development:** 1 week
- **Theme Development:** 3 days
- **Testing & Debugging:** 2 days
- **Documentation:** 1 day
- **Total:** ~2 weeks

### Features Count
- **Chatbot Themes:** 4
- **Personality Modes:** 3 per theme (12 total)
- **System Prompts:** 12 unique prompts
- **Welcome Messages:** 4
- **Usage Tips:** 4 sets

---

## 🎓 Learning Resources

### Technologies to Learn
1. **Python Basics**
   - Variables, functions, classes
   - File I/O and environment variables
   - Error handling and exceptions

2. **Streamlit Framework**
   - Session state management
   - Widget interactions
   - Layout and styling
   - Caching and performance

3. **API Integration**
   - REST API concepts
   - Authentication methods
   - Error handling
   - Rate limiting

4. **Prompt Engineering**
   - System prompt design
   - Context management
   - Temperature and token settings
   - Personality crafting

### Recommended Tutorials
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs)
- [Python dotenv Guide](https://pypi.org/project/python-dotenv/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
1. **Report Bugs** - Open an issue with details
2. **Suggest Features** - Propose new themes or personalities
3. **Improve Documentation** - Fix typos or add examples
4. **Submit Code** - Fix bugs or add features via PR

### Contribution Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style Guidelines
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning and personal projects!

```
MIT License

Copyright (c) 2024 Chace Liu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👨‍💻 About the Developer

Hi! I'm **Chace Liu**, an 11-year-old coding enthusiast passionate about AI and web development. This project showcases my skills in:

- 🐍 Python programming
- 🎨 UI/UX design with Streamlit
- 🤖 AI integration and prompt engineering
- 📝 Technical documentation
- 🚀 Cloud deployment

### My Other Projects
- **Personal Portfolio Website** - [Live Demo](https://Chace.codecub.org)
  - Interactive portfolio with advanced CSS animations
  - Particle playground with 5 effect modes
  - Glassmorphism design and responsive layout

### Connect With Me
- **Portfolio:** [Chace.codecub.org](https://Chace.codecub.org)
- **GitHub:** [@CodeCubCA](https://github.com/CodeCubCA)
- **Projects:** [View All Projects](https://Chace.codecub.org/projects.html)

---

## 🙏 Acknowledgments

- **Groq** - For providing fast and affordable AI API
- **Streamlit** - For the amazing web framework
- **Meta AI** - For the llama-3.3 model
- **CodeCub Community** - For learning support and inspiration
- **Open Source Community** - For countless tutorials and examples

---

## 📝 Changelog

### Version 2.0 (Current)
- ✨ Updated title to "My AI Assistant v2.0"
- 🔧 Upgraded Groq library to v0.33.0
- 🐛 Fixed compatibility issues with httpx
- 📸 Added project screenshots

### Version 1.0 (Initial Release)
- ✨ 4 chatbot themes (Gaming, Study, Music, Sports)
- 🎭 3 personality modes per theme
- 💬 Real-time streaming responses
- 🔄 Dynamic theme switching
- 📱 Mobile responsive design
- 🚀 Deployed to Streamlit Cloud

### Future Versions
- **v2.1:** Chat history persistence
- **v2.2:** User authentication system
- **v2.3:** Conversation export feature
- **v3.0:** Voice input/output support

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ by Chace Liu**

[🤖 Try Live Demo](https://ai-chatbox-Chace-codecub.streamlit.app) • [🏠 Portfolio](https://Chace.codecub.org) • [📧 GitHub](https://github.com/CodeCubCA)

---

### 📊 Project Stats

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red.svg)
![Groq API](https://img.shields.io/badge/groq-0.33.0-purple.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

</div>
