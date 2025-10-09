# 🎙️ Voice AI Application

A lightweight application that allows you to talk to an AI agent and hear responses. This application uses OpenAI Whisper for speech-to-text, Google Gemini (via LangChain) for AI responses, and Google Text-to-Speech for voice responses.

## ✨ Features

- **Voice Input**: Record audio or upload audio files
- **Speech-to-Text**: Powered by OpenAI Whisper
- **AI Responses**: Powered by Google Gemini via LangChain
- **Text-to-Speech**: Powered by Google's gTTS
- **Multiple Interfaces**: Command-line and web-based interfaces
- **Configurable Language**: Support for multiple TTS languages
- **Conversation Memory**: Maintains context across interactions
- **Extensible**: Built with LangChain for easy addition of tools and capabilities

## 🚀 Quick Start

### 1. Setup

```bash
# Clone or download the project
cd hw4

# Run the setup script
python setup.py
```

### 2. Configure API Key

Edit the `.env` file and add your Google Gemini API key:

```bash
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Application

Choose one of these interfaces:

#### Command Line Interface
```bash
python voice_ai_app.py
```

#### Web Interface (Recommended)
```bash
python gradio_voice_app.py
```
Then open your browser to `http://localhost:7860`

## 📋 Requirements

- Python 3.8+
- Google Gemini API key
- Microphone (for voice recording)
- Speakers/headphones (for audio output)

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
DEFAULT_TTS_LANGUAGE=en          # Language for text-to-speech
WHISPER_MODEL=base              # Whisper model size
GEMINI_MODEL=gemini-1.5-flash   # Gemini model (free tier compatible)
```

### Google Gemini Free Tier

The application is configured to work with Google Gemini's free tier:
- **Free tier models**: `gemini-1.5-flash` (recommended), `gemini-pro`
- **Rate limits**: 15 requests per minute, 1 million tokens per day
- **Features**: Full conversation capabilities, no cost

### Supported Languages

The TTS supports many languages. Common language codes:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `ko` - Korean
- `zh` - Chinese

### Whisper Models

Choose based on your needs:
- `tiny` - Fastest, least accurate
- `base` - Good balance (default)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy, slowest

## 🎯 Usage

### Web Interface (Gradio)

1. **Audio Upload Tab**: Upload audio files and get voice responses
2. **Text Chat Tab**: Type messages and get voice responses
3. **Settings Tab**: Change TTS language
4. **History Tab**: View conversation history

### Command Line Interface

The CLI provides a menu-driven interface:
1. Record audio (press Enter to stop)
2. Upload audio file
3. Text chat
4. Change TTS language
5. Exit

## 🏗️ Architecture

### Core Components

- **VoiceAI Class**: Main application logic
- **Whisper Integration**: Speech-to-text transcription
- **LangChain + Gemini**: AI response generation
- **gTTS Integration**: Text-to-speech conversion
- **Audio Processing**: Recording, playback, and file handling

### Extensibility

The application is built with LangChain, making it easy to add:

- **Tool Calling**: Add custom functions the AI can use
- **Memory Types**: Different conversation memory strategies
- **Chains**: More complex AI workflows
- **Agents**: Specialized AI agents for different tasks
- **Retrieval**: Add document or knowledge base integration

### Example: Adding Tool Calling

```python
from langchain.tools import Tool

def get_weather(city: str) -> str:
    """Get current weather for a city"""
    # Your weather API logic here
    return f"Weather in {city}: Sunny, 72°F"

# Add tool to the agent
tools = [
    Tool(
        name="get_weather",
        description="Get current weather for a city",
        func=get_weather
    )
]

# Initialize agent with tools
agent = initialize_agent(
    tools=tools,
    llm=self.llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=self.memory
)
```

## 🐛 Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY not found"**
   - Make sure you have a `.env` file with your API key
   - Check that the key is valid and has proper permissions

2. **Audio recording issues**
   - Ensure microphone permissions are granted
   - Check that PyAudio is properly installed
   - Try a different audio device

3. **TTS not working**
   - Check your internet connection (gTTS requires internet)
   - Verify the language code is supported
   - Ensure pygame is properly installed

4. **Whisper model download issues**
   - Check internet connection
   - Ensure sufficient disk space
   - Try a smaller model first

### Installation Issues

If you encounter installation issues:

```bash
# Update pip
pip install --upgrade pip

# Install PyAudio separately (often causes issues)
# On macOS:
brew install portaudio
pip install pyaudio

# On Ubuntu/Debian:
sudo apt-get install portaudio19-dev
pip install pyaudio

# On Windows:
# Download and install Microsoft Visual C++ Build Tools
pip install pyaudio
```

## 📁 Project Structure

```
hw4/
├── voice_ai_app.py          # Main command-line application
├── gradio_voice_app.py      # Web interface using Gradio
├── setup.py                 # Setup script
├── requirements.txt         # Python dependencies
├── env_example.txt          # Environment variables example
├── README.md               # This file
└── speech_tts_demo.ipynb   # Jupyter notebook demo
```

## 🤝 Contributing

This application is designed to be easily extensible. Some ideas for enhancements:

- Add more TTS providers (Azure, AWS, etc.)
- Implement real-time voice recognition
- Add voice cloning capabilities
- Integrate with external APIs (weather, news, etc.)
- Add conversation export/import
- Implement user authentication
- Add multi-user support

## 📄 License

This project is for educational purposes. Please ensure you comply with the terms of service for all APIs used (Google Gemini, OpenAI Whisper, Google TTS).

## 🙏 Acknowledgments

- OpenAI for the Whisper speech recognition model
- Google for Gemini AI and Text-to-Speech services
- LangChain for the AI framework
- Gradio for the web interface framework
