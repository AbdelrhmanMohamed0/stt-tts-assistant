# Required installations:
# pip install gTTS SpeechRecognition pydub google-generativeai
# sudo apt install ffmpeg  # Required for pydub to play audio

import os
import time
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import google.generativeai as genai

# ⚠️ Load API key from environment variable for security
# Example: export GEMINI_API_KEY="your_api_key"
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a directory to store output audio files
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 🔊 Convert text to speech and play it
def text_to_speech(text, lang='en'):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(OUTPUT_DIR, f"tts_{timestamp}.mp3")
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"✅ Saved TTS to: {filename}")
        audio = AudioSegment.from_mp3(filename)
        play(audio)
    except Exception as e:
        print(f"🔊 Error in TTS: {e}")

# 🎤 Convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening... (Speak now)")
            audio = r.listen(source)
        text = r.recognize_google(audio)
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")
    except Exception as e:
        print(f"⚠️ Error in speech recognition: {e}")
    return None

# 🧭 Main menu loop
def main():
    print("🌟 Voice Assistant System 🌟")
    while True:
        print("\n1. Text to Speech\n2. Speech to Text\n3. Exit")
        try:
            choice = input("Choose (1-3): ").strip()
        except EOFError:
            print("❌ No input detected. Exiting...")
            break

        if choice == "1":
            try:
                text = input("Enter text: ").strip()
                if text:
                    text_to_speech(text)
                else:
                    print("⚠️ No text entered.")
            except EOFError:
                print("❌ No input provided.")
        elif choice == "2":
            result = speech_to_text()
            if result:
                text_to_speech(f"You said: {result}")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

