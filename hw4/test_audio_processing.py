#!/usr/bin/env python3
"""
Test script for audio processing functionality
"""

import os
import tempfile
from dotenv import load_dotenv
from voice_ai_app import VoiceAI

def test_audio_processing():
    """Test the audio processing pipeline"""
    
    # Load environment variables
    load_dotenv()
    
    print("🧪 Testing Voice AI Audio Processing...")
    
    try:
        # Initialize Voice AI
        voice_ai = VoiceAI(
            tts_language="en",
            whisper_model="base"
        )
        
        # Create a test audio file using gTTS
        from gtts import gTTS
        test_text = "Hello, this is a test of the voice AI system."
        
        print("🎤 Creating test audio...")
        tts = gTTS(text=test_text, lang='en', slow=False)
        test_audio_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        tts.save(test_audio_file.name)
        
        print(f"✅ Test audio created: {test_audio_file.name}")
        
        # Test the complete pipeline
        print("🔄 Testing complete pipeline...")
        voice_ai.process_voice_input(test_audio_file.name)
        
        # Get conversation history
        messages = voice_ai.memory.chat_memory.messages
        if len(messages) >= 2:
            user_msg = messages[-2].content if hasattr(messages[-2], 'content') else str(messages[-2])
            ai_msg = messages[-1].content if hasattr(messages[-1], 'content') else str(messages[-1])
            
            print("\n📝 Results:")
            print(f"Original text: {test_text}")
            print(f"Transcribed: {user_msg}")
            print(f"AI Response: {ai_msg}")
        
        # Cleanup
        os.unlink(test_audio_file.name)
        print("\n✅ Test completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_audio_processing()
