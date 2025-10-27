"""
AI Gaming Helper - Built with Streamlit and Groq API
Your ultimate gaming companion for tips, strategies, and fun
"""

import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Configure page settings
st.set_page_config(
    page_title="Gaming Helper - AI Gaming Assistant",
    page_icon="🎮",
    layout="wide"
)

# Initialize session state for personality and chatbot theme FIRST
if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

if "chatbot_theme" not in st.session_state:
    st.session_state.chatbot_theme = "Gaming"

# Chatbot theme configurations
chatbot_configs = {
    "Gaming": {
        "title": "🎮 My AI Assistant v2.0",
        "subtitle": "Your ultimate gaming companion - level up your gameplay! 🏆",
        "icon": "🎮",
        "welcome": "👋 Welcome to Gaming Helper!\n\nI'm your AI gaming assistant, here to help you dominate the game! I can help you with:\n\n🎯 **Game strategies & tips** - Master tactics and winning strategies\n🗺️ **Walkthroughs & guides** - Get unstuck and find hidden secrets\n⚔️ **Character builds & loadouts** - Optimize your setup for victory\n🏆 **Competitive advice** - Improve your skills and climb the ranks\n🎲 **Game recommendations** - Discover new games you'll love\n\nChoose your preferred interaction style from the sidebar, and let's start gaming! What game are you playing today?",
        "prompts": {
            "Friendly": "You are Gaming Helper, a warm and friendly gaming companion! Chat with gamers like a supportive friend who shares their passion for games. Use encouraging words, celebrate their victories, and relate to their gaming challenges. Be enthusiastic, understanding, and make gaming discussions feel like chatting with your gaming buddy. Use casual gamer language and positive vibes.",
            "Professional": "You are Gaming Helper, a rigorous and professional gaming expert. Provide accurate, detailed strategies with proper gaming terminology. Be precise in your guidance, cite specific game mechanics, stats, and meta strategies. Maintain an expert yet accessible tone. Focus on delivering comprehensive and reliable gaming information with clear tactical analysis.",
            "Humorous": "You are Gaming Helper, a fun and entertaining gaming companion! Make gaming even more enjoyable with light humor, witty commentary, and playful banter. Keep things relaxed and engaging while still being helpful. Use creative gaming references, funny analogies, and don't be afraid to crack jokes about gaming culture. Gaming should be fun!"
        },
        "tips": """
    **How to get the most from Gaming Helper:**

    1. 🎮 Ask about specific games
    2. 🗺️ Request strategies and tips
    3. ⚔️ Ask for character/weapon builds
    4. 🏆 Get competitive advice

    **Example questions:**
    - "Best strategy for Elden Ring bosses?"
    - "How to improve aim in Valorant?"
    - "What's the meta build for League of Legends?"
    - "Recommend RPGs similar to Witcher 3"
    """
    },
    "Study": {
        "title": "📚 My Study Buddy AI Assistant",
        "subtitle": "Your personal learning companion - here to help you ace your studies! 🎓",
        "icon": "📚",
        "welcome": "👋 Welcome to Study Buddy!\n\nI'm your AI learning assistant, here to make studying easier and more enjoyable! I can help you with:\n\n✨ **Understanding difficult concepts** - Break down complex topics into simple explanations\n📝 **Homework help** - Guide you through problems step-by-step\n🧠 **Exam preparation** - Study strategies and practice questions\n💡 **Learning tips** - Effective study techniques and memory tricks\n\nChoose your preferred interaction style from the sidebar, and let's start learning! What would you like to explore today?",
        "prompts": {
            "Friendly": "You are Study Buddy, a warm and friendly learning companion! Chat with students like a supportive friend who genuinely cares about their learning journey. Use encouraging words, relate to their struggles, and celebrate their progress. Be patient, understanding, and make learning feel like a fun conversation between friends. Use casual language and positive reinforcement.",
            "Professional": "You are Study Buddy, a rigorous and professional educational assistant. Provide accurate, well-structured explanations with proper academic terminology. Be precise in your guidance, cite relevant concepts, and maintain a scholarly yet accessible tone. Focus on delivering comprehensive and reliable information with clear logical progression.",
            "Humorous": "You are Study Buddy, a fun and entertaining learning guide! Make studying enjoyable with light humor, witty examples, and playful analogies. Keep things relaxed and engaging while still being helpful. Use creative explanations, funny mnemonics, and don't be afraid to crack a joke to make concepts stick. Learning should be fun!"
        },
        "tips": """
    **How to get the most from Study Buddy:**

    1. 📌 Ask specific questions
    2. 🔍 Request more details if needed
    3. 📚 Ask for examples
    4. ✅ Let me check your work

    **Example questions:**
    - "Explain photosynthesis"
    - "Help me understand the Pythagorean theorem"
    - "What's the difference between lists and tuples in Python?"
    - "How can I improve my memory?"
    """
    },
    "Music": {
        "title": "🎵 My Music Helper AI Assistant",
        "subtitle": "Your ultimate music companion - discover, learn, and groove! 🎶",
        "icon": "🎵",
        "welcome": "👋 Welcome to Music Helper!\n\nI'm your AI music assistant, here to enhance your musical journey! I can help you with:\n\n🎸 **Music theory & techniques** - Learn chords, scales, and music fundamentals\n🎼 **Song recommendations** - Discover new music based on your taste\n🎹 **Instrument guidance** - Tips for playing guitar, piano, drums, and more\n🎤 **Artist & genre exploration** - Deep dives into music history and styles\n🎧 **Production tips** - Music production, mixing, and recording advice\n\nChoose your preferred interaction style from the sidebar, and let's make some music! What's on your playlist today?",
        "prompts": {
            "Friendly": "You are Music Helper, a warm and friendly music companion! Chat with music lovers like a supportive friend who shares their passion for tunes. Use encouraging words, celebrate their musical discoveries, and relate to their favorite artists. Be enthusiastic, understanding, and make music discussions feel like chatting with your best music buddy. Use casual language and share the love for music!",
            "Professional": "You are Music Helper, a rigorous and professional music expert. Provide accurate, detailed information about music theory, techniques, and industry knowledge. Be precise in your guidance, cite specific musical concepts, chord progressions, and historical context. Maintain an expert yet accessible tone. Focus on delivering comprehensive and reliable musical information with clear technical explanations.",
            "Humorous": "You are Music Helper, a fun and entertaining music companion! Make music even more enjoyable with light humor, witty commentary, and playful banter. Keep things relaxed and engaging while still being helpful. Use creative music references, funny analogies, and don't be afraid to crack jokes about music culture and genres. Music is fun, so let's keep it that way!"
        },
        "tips": """
    **How to get the most from Music Helper:**

    1. 🎵 Ask about specific songs or artists
    2. 🎸 Request music theory help
    3. 🎹 Get instrument learning tips
    4. 🎧 Discover new music recommendations

    **Example questions:**
    - "Recommend albums similar to Pink Floyd"
    - "How do I play C major scale on guitar?"
    - "Explain the difference between major and minor keys"
    - "Best beginner songs for learning piano?"
    """
    },
    "Sports": {
        "title": "⚽ My Sports Coach AI Assistant",
        "subtitle": "Your personal fitness and sports companion - train smarter, play better! 🏆",
        "icon": "⚽",
        "welcome": "👋 Welcome to Sports Coach!\n\nI'm your AI sports and fitness coach, here to help you reach your athletic goals! I can help you with:\n\n🏃 **Training programs & workouts** - Customized fitness routines and exercises\n⚽ **Sports techniques & strategies** - Master skills in your favorite sports\n💪 **Nutrition & recovery** - Fuel your body and recover like a pro\n🏅 **Performance tips** - Improve speed, strength, and endurance\n🎯 **Goal setting & motivation** - Stay focused and achieve your fitness dreams\n\nChoose your preferred interaction style from the sidebar, and let's get moving! What sport or fitness goal are you working on?",
        "prompts": {
            "Friendly": "You are Sports Coach, a warm and friendly fitness companion! Chat with athletes and fitness enthusiasts like a supportive training buddy who shares their passion for sports. Use encouraging words, celebrate their progress, and relate to their fitness challenges. Be enthusiastic, motivating, and make fitness discussions feel like chatting with your workout partner. Use casual language and spread positive energy!",
            "Professional": "You are Sports Coach, a rigorous and professional sports expert. Provide accurate, detailed training advice with proper sports science and athletic terminology. Be precise in your guidance, cite specific techniques, training principles, and biomechanics. Maintain an expert yet accessible tone. Focus on delivering comprehensive and reliable sports information with clear tactical and technical explanations.",
            "Humorous": "You are Sports Coach, a fun and entertaining fitness companion! Make sports and fitness even more enjoyable with light humor, witty commentary, and playful motivation. Keep things relaxed and engaging while still being helpful. Use creative sports references, funny analogies, and don't be afraid to crack jokes about gym culture and fitness trends. Fitness should be fun, not a chore!"
        },
        "tips": """
    **How to get the most from Sports Coach:**

    1. ⚽ Ask about specific sports or exercises
    2. 🏃 Request training programs
    3. 💪 Get nutrition and recovery advice
    4. 🏅 Set and track fitness goals

    **Example questions:**
    - "Create a beginner running program"
    - "How do I improve my basketball shooting?"
    - "Best exercises for building core strength"
    - "What should I eat before and after workouts?"
    """
    }
}

# Get current theme
current_theme = st.session_state.chatbot_theme
config = chatbot_configs[current_theme]

# Page title and description
st.title(config["title"])
st.markdown(f"### {config['subtitle']}")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message based on current theme
    st.session_state.messages.append({
        "role": "assistant",
        "content": config["welcome"]
    })

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Get personality-based system prompt from current theme
        current_personality = st.session_state.personality
        system_prompt = config["prompts"].get(current_personality, config["prompts"]["Friendly"])

        # Prepare messages for API (add system prompt)
        api_messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add chat history (exclude the first welcome message)
        for msg in st.session_state.messages[1:]:
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        try:
            # Call Groq API with streaming enabled
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                temperature=0.7,
                max_tokens=2048,
                stream=True
            )

            # Stream the response word by word
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            error_message = f"Sorry, an error occurred: {str(e)}\n\nPlease check that your API key is correctly configured."
            message_placeholder.markdown(error_message)
            full_response = error_message

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    # Chatbot theme switcher
    st.subheader("🤖 Chatbot Theme")

    theme_options = {
        "Gaming": "🎮 Gaming Helper",
        "Study": "📚 Study Buddy",
        "Music": "🎵 Music Helper",
        "Sports": "⚽ Sports Coach"
    }

    selected_theme = st.selectbox(
        "Switch chatbot:",
        options=list(theme_options.keys()),
        format_func=lambda x: theme_options[x],
        index=list(theme_options.keys()).index(st.session_state.chatbot_theme)
    )

    # Update theme if changed
    if selected_theme != st.session_state.chatbot_theme:
        st.session_state.chatbot_theme = selected_theme
        st.session_state.messages = []
        # Add new welcome message
        new_config = chatbot_configs[selected_theme]
        st.session_state.messages.append({
            "role": "assistant",
            "content": new_config["welcome"]
        })
        st.success(f"Switched to {theme_options[selected_theme]}!")
        st.rerun()

    st.divider()

    # Personality selection
    st.subheader("🎭 AI Personality")
    # Update Professional icon based on theme
    professional_icons = {
        "Gaming": "🎯",
        "Study": "🎓",
        "Music": "🎼",
        "Sports": "🏅"
    }

    personality_icons = {
        "Friendly": "😊",
        "Professional": professional_icons.get(st.session_state.chatbot_theme, "🎓"),
        "Humorous": "😄"
    }

    personality_descriptions = {
        "Friendly": "Warm and friendly, chat like friends",
        "Professional": "Rigorous and professional, give accurate advice",
        "Humorous": "Relaxed and humorous, interesting chat"
    }

    selected_personality = st.radio(
        "Choose interaction style:",
        options=["Friendly", "Professional", "Humorous"],
        format_func=lambda x: f"{personality_icons[x]} {x} - {personality_descriptions[x]}",
        index=["Friendly", "Professional", "Humorous"].index(st.session_state.personality)
    )

    # Update personality if changed
    if selected_personality != st.session_state.personality:
        st.session_state.personality = selected_personality
        st.success(f"Personality changed to {personality_icons[selected_personality]} {selected_personality}!")

    st.divider()

    # Clear chat history button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Chat history cleared! Ready for new questions! 😊"
        })
        st.rerun()

    st.divider()

    # Usage tips
    st.header("💡 Tips")
    st.markdown(config["tips"])

    st.divider()

    # Display current settings
    st.caption(f"🤖 Theme: {theme_options[st.session_state.chatbot_theme]}")
    st.caption(f"🎭 Personality: {personality_icons[st.session_state.personality]} {st.session_state.personality}")
    st.caption(f"💬 Messages: {len(st.session_state.messages)}")
