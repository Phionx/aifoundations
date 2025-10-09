#!/usr/bin/env python3
"""
Gradio Voice AI Application
A web-based interface for the Voice AI application using Gradio.
"""

import os
import tempfile
import gradio as gr
from dotenv import load_dotenv
from voice_ai_app import VoiceAI

# Load environment variables
load_dotenv()

class GradioVoiceAI:
    """Gradio-based Voice AI interface"""
    
    def __init__(self):
        """Initialize the Gradio Voice AI"""
        tts_language = os.getenv("DEFAULT_TTS_LANGUAGE", "en")
        whisper_model = os.getenv("WHISPER_MODEL", "base")
        
        self.voice_ai = VoiceAI(
            tts_language=tts_language,
            whisper_model=whisper_model
        )
        
        self.current_tts_language = tts_language
    
    def process_audio_upload(self, audio_file) -> str:
        """Process uploaded audio file"""
        if audio_file is None:
            return "❌ Please upload an audio file"
        
        try:
            # Handle different audio file formats from Gradio
            if isinstance(audio_file, tuple):
                # Gradio returns a tuple (sample_rate, audio_data) for some formats
                sample_rate, audio_data = audio_file
                # Save to temporary file
                import tempfile
                import soundfile as sf
                temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
                sf.write(temp_file.name, audio_data, sample_rate)
                audio_path = temp_file.name
            else:
                # Regular file path - ensure it's a file, not a directory
                audio_path = str(audio_file)
                
                # Check if it's actually a file
                if os.path.isdir(audio_path):
                    return f"❌ Please select a file, not a directory: {audio_path}"
                
                if not os.path.isfile(audio_path):
                    return f"❌ File not found: {audio_path}"
            
            # Additional validation
            if not audio_path or audio_path.strip() == "":
                return "❌ No audio file provided"
            
            # Process the audio file (but don't return the audio file path to avoid Gradio issues)
            self.voice_ai.process_voice_input(audio_path)
            
            # Get the last conversation from memory
            chat_history = self.voice_ai.memory.chat_memory.messages
            if len(chat_history) >= 2:
                user_msg = chat_history[-2].content if hasattr(chat_history[-2], 'content') else str(chat_history[-2])
                ai_msg = chat_history[-1].content if hasattr(chat_history[-1], 'content') else str(chat_history[-1])
                return f"✅ Processed successfully!\n\n**Your message:** {user_msg}\n\n**AI Response:** {ai_msg}"
            else:
                return "✅ Audio processed successfully!"
                
        except Exception as e:
            return f"❌ Error processing audio: {str(e)}"
    
    def process_text_input(self, user_text: str) -> str:
        """Process text input"""
        if not user_text.strip():
            return "❌ Please enter some text"
        
        try:
            # Get AI response
            ai_response = self.voice_ai.get_ai_response(user_text)
            
            # Convert to speech (but don't return the file path to avoid Gradio issues)
            tts_file = self.voice_ai.text_to_speech(ai_response)
            
            return f"**AI Response:** {ai_response}"
            
        except Exception as e:
            return f"❌ Error processing text: {str(e)}"
    
    def change_language(self, new_language: str) -> str:
        """Change TTS language"""
        if not new_language.strip():
            return f"Current language: {self.current_tts_language}"
        
        self.voice_ai.tts_language = new_language.strip()
        self.current_tts_language = new_language.strip()
        return f"✅ Language changed to: {new_language}"
    
    def get_conversation_history(self) -> str:
        """Get conversation history"""
        try:
            messages = self.voice_ai.memory.chat_memory.messages
            if not messages:
                return "No conversation history yet."
            
            history = "**Conversation History:**\n\n"
            for i, msg in enumerate(messages):
                role = "**You:**" if i % 2 == 0 else "**AI:**"
                content = msg.content if hasattr(msg, 'content') else str(msg)
                history += f"{role} {content}\n\n"
            
            return history
        except Exception as e:
            return f"Error retrieving history: {str(e)}"
    
    def clear_history(self) -> str:
        """Clear conversation history"""
        try:
            self.voice_ai.memory.clear()
            return "✅ Conversation history cleared!"
        except Exception as e:
            return f"❌ Error clearing history: {str(e)}"
    
    def check_api_connection(self) -> str:
        """Check if the API key is working"""
        try:
            # Test with a simple prompt
            test_response = self.voice_ai.get_ai_response("Hello, this is a test message.")
            
            # Check if we got a valid response
            if test_response and not test_response.startswith("Sorry, I encountered an error"):
                return "✅ API connection working! Gemini is responding correctly."
            else:
                return "❌ API connection failed. Please check your API key."
                
        except Exception as e:
            return f"❌ API connection error: {str(e)}"


def create_gradio_interface():
    """Create and launch the Gradio interface"""
    
    gradio_app = GradioVoiceAI()
    
    with gr.Blocks(
        title="Voice AI Assistant",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            max-width: 1200px !important;
        }
        .chat-message {
            padding: 10px;
            margin: 5px 0;
            border-radius: 10px;
        }
        """
    ) as demo:
        
        gr.Markdown("""
        # 🎙️ Voice AI Assistant
        
        Talk to an AI assistant using voice or text! This application uses:
        - **OpenAI Whisper** for speech-to-text
        - **Google Gemini** for AI responses
        - **Google Text-to-Speech** for voice responses
        
        ## How to use:
        1. **Audio Upload**: Upload an audio file and get a voice response
        2. **Text Chat**: Type your message and get a voice response
        3. **Language Settings**: Change the TTS language
        4. **History**: View and clear conversation history
        """)
        
        with gr.Tab("🎤 Audio Upload"):
            with gr.Row():
                with gr.Column(scale=2):
                    audio_input = gr.Audio(
                        label="Upload Audio File",
                        type="filepath"
                    )
                    process_audio_btn = gr.Button("🎤 Process Audio", variant="primary")
                
                with gr.Column(scale=1):
                    audio_result = gr.Markdown(label="Audio Processing Result")
        
        with gr.Tab("💬 Text Chat"):
            with gr.Row():
                with gr.Column(scale=2):
                    text_input = gr.Textbox(
                        label="Your Message",
                        placeholder="Type your message here...",
                        lines=3
                    )
                    text_submit_btn = gr.Button("💬 Send Message", variant="primary")
                
                with gr.Column(scale=1):
                    text_result = gr.Markdown(label="Chat Result")
        
        with gr.Tab("⚙️ Settings"):
            with gr.Row():
                with gr.Column():
                    language_input = gr.Textbox(
                        label="TTS Language Code",
                        placeholder="en, fr, es, de, it, etc.",
                        value=gradio_app.current_tts_language
                    )
                    language_btn = gr.Button("🌍 Change Language")
                    language_result = gr.Markdown(label="Language Status")
                    
                    gr.Markdown("---")  # Separator
                    
                    api_check_btn = gr.Button("🔌 Check API Connection", variant="secondary")
                    api_status = gr.Markdown(label="API Status")
        
        with gr.Tab("📜 Conversation History"):
            with gr.Row():
                history_display = gr.Markdown(label="Conversation History")
                with gr.Column():
                    refresh_history_btn = gr.Button("🔄 Refresh History")
                    clear_history_btn = gr.Button("🗑️ Clear History", variant="stop")
        
        # Event handlers
        process_audio_btn.click(
            fn=gradio_app.process_audio_upload,
            inputs=[audio_input],
            outputs=[audio_result]
        )
        
        text_submit_btn.click(
            fn=gradio_app.process_text_input,
            inputs=[text_input],
            outputs=[text_result]
        )
        
        language_btn.click(
            fn=gradio_app.change_language,
            inputs=[language_input],
            outputs=[language_result]
        )
        
        refresh_history_btn.click(
            fn=gradio_app.get_conversation_history,
            outputs=[history_display]
        )
        
        clear_history_btn.click(
            fn=gradio_app.clear_history,
            outputs=[history_display]
        )
        
        api_check_btn.click(
            fn=gradio_app.check_api_connection,
            outputs=[api_status]
        )
        
        # Load initial history and check API status
        demo.load(
            fn=gradio_app.get_conversation_history,
            outputs=[history_display]
        )
        
        # Auto-check API connection on load
        demo.load(
            fn=gradio_app.check_api_connection,
            outputs=[api_status]
        )
    
    return demo


def main():
    """Launch the Gradio interface"""
    print("🚀 Starting Voice AI Gradio Interface...")
    
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        print("Please create a .env file with your Gemini API key")
        return
    
    try:
        demo = create_gradio_interface()
        demo.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            show_error=True,
            quiet=False
        )
    except Exception as e:
        print(f"❌ Error launching Gradio interface: {e}")


if __name__ == "__main__":
    main()
