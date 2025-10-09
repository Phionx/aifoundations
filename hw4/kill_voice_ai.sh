#!/bin/bash

# Voice AI Application Kill Script
echo "🛑 Stopping Voice AI Application..."

# Kill Gradio voice app processes
echo "Killing Gradio voice app processes..."
pkill -f gradio_voice_app
pkill -f voice_ai_app

# Kill processes on ports 7860 and 7861
echo "Killing processes on ports 7860 and 7861..."
lsof -ti:7860 | xargs kill -9 2>/dev/null
lsof -ti:7861 | xargs kill -9 2>/dev/null

# Kill any Python processes that might be running voice AI
echo "Killing any remaining voice AI Python processes..."
ps aux | grep -E "(gradio_voice_app|voice_ai_app)" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null

echo "✅ Voice AI Application stopped!"
echo "All processes and ports have been cleared."
