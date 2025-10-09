#!/usr/bin/env python3
"""
Voice AI Application
A lightweight application that allows users to talk to an AI agent and hear responses.
Uses OpenAI Whisper for speech-to-text, LangChain + Gemini for LLM, and gTTS for text-to-speech.
"""

import os
import sys
import tempfile
import threading
import time
from typing import Optional, Dict, Any
from pathlib import Path

import pyaudio
import wave
import whisper
from gtts import gTTS
import pygame
from dotenv import load_dotenv

# LangChain imports
from langchain_community.llms import GooglePalm
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Load environment variables
load_dotenv()

class VoiceAI:
    """Main Voice AI application class"""
    
    def __init__(self, 
                 gemini_api_key: Optional[str] = None,
                 tts_language: str = "en",
                 whisper_model: str = "base",
                 sample_rate: int = 16000,
                 chunk_size: int = 1024,
                 channels: int = 1):
        """
        Initialize the Voice AI application
        
        Args:
            gemini_api_key: Google Gemini API key
            tts_language: Language code for text-to-speech (e.g., 'en', 'fr', 'es')
            whisper_model: Whisper model size ('tiny', 'base', 'small', 'medium', 'large')
            sample_rate: Audio sample rate for recording
            chunk_size: Audio chunk size for recording
            channels: Number of audio channels
        """
        self.tts_language = tts_language
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.channels = channels
        self.is_recording = False
        self.audio_frames = []
        
        # Initialize pygame for audio playback
        pygame.mixer.init()
        
        # Initialize Whisper
        print(f"Loading Whisper model: {whisper_model}")
        self.whisper_model = whisper.load_model(whisper_model)
        
        # Initialize LangChain with Gemini
        self._setup_llm(gemini_api_key)
        
        print("Voice AI initialized successfully!")
    
    def _setup_llm(self, api_key: Optional[str] = None):
        """Setup LangChain with Google Gemini"""
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        # Initialize Gemini LLM (Free tier compatible)
        try:
            # Try the latest free tier model first
            self.llm = ChatGoogleGenerativeAI(
                model="models/gemini-flash-latest",
                google_api_key=api_key,
                temperature=0.7
            )
        except Exception as e:
            print(f"Warning: ChatGoogleGenerativeAI with gemini-flash-latest failed, trying gemini-pro-latest: {e}")
            try:
                self.llm = ChatGoogleGenerativeAI(
                    model="models/gemini-pro-latest",
                    google_api_key=api_key,
                    temperature=0.7
                )
            except Exception as e2:
                print(f"Warning: ChatGoogleGenerativeAI failed, trying gemini-2.0-flash: {e2}")
                try:
                    self.llm = ChatGoogleGenerativeAI(
                        model="models/gemini-2.0-flash",
                        google_api_key=api_key,
                        temperature=0.7
                    )
                except Exception as e3:
                    print(f"Warning: ChatGoogleGenerativeAI failed, trying direct API: {e3}")
                    # Fallback to direct Google Generative AI
                    import google.generativeai as genai
                    genai.configure(api_key=api_key)
                    self.llm = genai.GenerativeModel('models/gemini-flash-latest')
        
        # Setup conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Define system prompt
        self.system_prompt = """You are a helpful AI assistant. 
        Keep your responses concise and conversational, as they will be converted to speech.
        Aim for responses that are 1-2 sentences long for better user experience.
        Be friendly, helpful, and engaging in your responses."""
        
        print("LangChain with Gemini initialized successfully!")
    
    def start_recording(self) -> None:
        """Start recording audio from microphone"""
        if self.is_recording:
            print("Already recording!")
            return
        
        self.is_recording = True
        self.audio_frames = []
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        
        # Open audio stream
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        # Start recording thread
        self.recording_thread = threading.Thread(target=self._record_audio)
        self.recording_thread.start()
        
        print("🎤 Recording started... (Press Enter to stop)")
    
    def stop_recording(self) -> Optional[str]:
        """Stop recording and return the audio file path"""
        if not self.is_recording:
            print("Not currently recording!")
            return None
        
        self.is_recording = False
        
        # Wait for recording thread to finish
        if hasattr(self, 'recording_thread'):
            self.recording_thread.join()
        
        # Stop and close audio stream
        if hasattr(self, 'stream'):
            self.stream.stop_stream()
            self.stream.close()
        
        if hasattr(self, 'audio'):
            self.audio.terminate()
        
        # Save audio to temporary file
        if self.audio_frames:
            audio_file = self._save_audio_to_file()
            print("🎤 Recording stopped!")
            return audio_file
        else:
            print("No audio recorded!")
            return None
    
    def _record_audio(self) -> None:
        """Internal method to record audio in a separate thread"""
        while self.is_recording:
            try:
                data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                self.audio_frames.append(data)
            except Exception as e:
                print(f"Error recording audio: {e}")
                break
    
    def _save_audio_to_file(self) -> str:
        """Save recorded audio frames to a temporary WAV file"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        
        with wave.open(temp_file.name, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.audio_frames))
        
        return temp_file.name
    
    def transcribe_audio(self, audio_file_path: str) -> str:
        """Transcribe audio file to text using Whisper"""
        print("🔄 Transcribing audio...")
        try:
            result = self.whisper_model.transcribe(audio_file_path)
            transcribed_text = result["text"].strip()
            print(f"📝 Transcription: {transcribed_text}")
            return transcribed_text
        except Exception as e:
            print(f"❌ Error transcribing audio: {e}")
            return ""
    
    def get_ai_response(self, user_message: str) -> str:
        """Get AI response using LangChain and Gemini"""
        print("🤖 Getting AI response...")
        try:
            # Check if using LangChain or direct Google AI
            if hasattr(self.llm, 'invoke'):
                # LangChain interface
                messages = [
                    SystemMessage(content=self.system_prompt),
                    HumanMessage(content=user_message)
                ]
                response = self.llm.invoke(messages)
                ai_response = response.content.strip()
                
                # Update memory
                self.memory.save_context(
                    {"input": user_message},
                    {"output": ai_response}
                )
            else:
                # Direct Google AI interface
                prompt = f"{self.system_prompt}\n\nUser: {user_message}"
                response = self.llm.generate_content(prompt)
                ai_response = response.text.strip()
                
                # Update memory (simplified for direct API)
                self.memory.save_context(
                    {"input": user_message},
                    {"output": ai_response}
                )
            
            print(f"💬 AI Response: {ai_response}")
            return ai_response
            
        except Exception as e:
            print(f"❌ Error getting AI response: {e}")
            return "Sorry, I encountered an error while processing your request."
    
    def text_to_speech(self, text: str) -> Optional[str]:
        """Convert text to speech and save as audio file"""
        if not text:
            return None
        
        print("🔊 Converting text to speech...")
        try:
            # Create TTS object
            tts = gTTS(text=text, lang=self.tts_language, slow=False)
            
            # Save to temporary file
            temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            tts.save(temp_file.name)
            
            print(f"🔊 Audio saved: {temp_file.name}")
            return temp_file.name
            
        except Exception as e:
            print(f"❌ Error converting text to speech: {e}")
            return None
    
    def play_audio(self, audio_file_path: str) -> None:
        """Play audio file"""
        try:
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.play()
            
            # Wait for playback to complete
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
                
        except Exception as e:
            print(f"❌ Error playing audio: {e}")
    
    def cleanup_audio_file(self, audio_file_path: str) -> None:
        """Clean up temporary audio file"""
        try:
            if os.path.exists(audio_file_path):
                os.unlink(audio_file_path)
        except Exception as e:
            print(f"Warning: Could not delete audio file {audio_file_path}: {e}")
    
    def process_voice_input(self, audio_file_path: str) -> None:
        """Complete pipeline: audio -> text -> AI response -> speech"""
        tts_file = None
        try:
            # Step 1: Transcribe audio
            transcribed_text = self.transcribe_audio(audio_file_path)
            if not transcribed_text:
                print("❌ No text transcribed from audio")
                return
            
            # Step 2: Get AI response
            ai_response = self.get_ai_response(transcribed_text)
            if not ai_response:
                print("❌ No AI response received")
                return
            
            # Step 3: Convert response to speech
            tts_file = self.text_to_speech(ai_response)
            if not tts_file:
                print("❌ Failed to convert response to speech")
                return
            
            # Step 4: Play the response
            print("🔊 Playing AI response...")
            self.play_audio(tts_file)
            
        except Exception as e:
            print(f"❌ Error in voice processing pipeline: {e}")
        finally:
            # Cleanup audio files
            if tts_file:
                self.cleanup_audio_file(tts_file)
            # Only cleanup input file if it's a temporary file (starts with /tmp or /var/tmp)
            if audio_file_path and (audio_file_path.startswith('/tmp/') or audio_file_path.startswith('/var/tmp/')):
                self.cleanup_audio_file(audio_file_path)


def main():
    """Main application entry point"""
    print("🎙️ Voice AI Application")
    print("=" * 50)
    
    # Get configuration from environment
    tts_language = os.getenv("DEFAULT_TTS_LANGUAGE", "en")
    whisper_model = os.getenv("WHISPER_MODEL", "base")
    
    try:
        # Initialize Voice AI
        voice_ai = VoiceAI(
            tts_language=tts_language,
            whisper_model=whisper_model
        )
        
        print(f"🔧 Configuration:")
        print(f"   TTS Language: {tts_language}")
        print(f"   Whisper Model: {whisper_model}")
        print()
        
        while True:
            print("🎙️ Voice AI Menu:")
            print("1. Record audio (Press Enter to stop)")
            print("2. Upload audio file")
            print("3. Text chat")
            print("4. Change TTS language")
            print("5. Exit")
            
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == "1":
                # Record audio
                voice_ai.start_recording()
                input()  # Wait for Enter to stop
                audio_file = voice_ai.stop_recording()
                if audio_file:
                    voice_ai.process_voice_input(audio_file)
            
            elif choice == "2":
                # Upload audio file
                file_path = input("Enter path to audio file: ").strip()
                if os.path.exists(file_path):
                    voice_ai.process_voice_input(file_path)
                else:
                    print("❌ File not found!")
            
            elif choice == "3":
                # Text chat
                user_input = input("You: ").strip()
                if user_input:
                    ai_response = voice_ai.get_ai_response(user_input)
                    tts_file = voice_ai.text_to_speech(ai_response)
                    if tts_file:
                        voice_ai.play_audio(tts_file)
                        voice_ai.cleanup_audio_file(tts_file)
            
            elif choice == "4":
                # Change TTS language
                new_lang = input(f"Enter new language code (current: {tts_language}): ").strip()
                if new_lang:
                    voice_ai.tts_language = new_lang
                    print(f"✅ TTS language changed to: {new_lang}")
            
            elif choice == "5":
                print("👋 Goodbye!")
                break
            
            else:
                print("❌ Invalid option!")
            
            print("\n" + "-" * 50 + "\n")
    
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Application error: {e}")


if __name__ == "__main__":
    main()
