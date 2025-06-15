# 🎙️ Voice Assistant with Text-to-Speech and Speech Recognition

This project is a simple voice assistant using Python libraries: `gTTS`, `SpeechRecognition`, `pydub`, and optionally Google Gemini API (for future AI integration).

---

## 🧰 Requirements

### Install required Python packages

```bash
pip install gTTS SpeechRecognition pydub google-generativeai
```

### System dependencies (required for `pydub`)

```bash
sudo apt install ffmpeg
```
> ⚠️ `ffmpeg` is essential for audio playback with `pydub`.

---

## 🔐 Setting up Google Gemini API

1. Get your API key from Google AI Studio.
2. Set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
3. **Never** hard-code your API key into the script for security reasons.

---

## 📁 Project Structure

```
voice_assistant/
├── output/                # Folder to store generated audio files
├── assistant.py           # Main script file
├── README.md              # This documentation
```

---

## ⚙️ Core Features

### 1. Text-to-Speech (`text_to_speech`)
- Uses `gTTS` to convert text to MP3 audio.
- Saves and plays the result using `pydub`.

### 2. Speech-to-Text (`speech_to_text`)
- Captures microphone input and uses Google Speech Recognition API.
- Currently supports English (`en-US`).

### 3. Interactive Menu (`main`)
- User-friendly CLI interface.
- Options to convert text to speech, listen and transcribe speech, or exit.

---

## 🚀 Running the Assistant

```bash
python assistant.py
```

You will see a simple menu like:

```
1. Text to Speech
2. Speech to Text
3. Exit
```

---

## ✅ Example Output

```
Choose (1-3): 1
Enter text: Hello, I am your assistant.
✅ Saved TTS to: output/tts_20250616_141502.mp3
```

---

## 📌 Notes

- Ensure your microphone is working.
- For better experience, use headphones to avoid echo.
- You can change the language (e.g., use `lang='ar'` for Arabic).

---

## 🔮 Future Improvements

- Add multilingual support.
- Integrate Gemini API responses for conversational AI.
- Add a graphical interface (e.g., Tkinter or PyQt).

---

## 👨‍💻 Developer Notes

This project was created as a hands-on exercise to explore:
- Speech-to-text and text-to-speech in Python.
- API integration.
- Real-time user interaction.

---

## License

Open-source under MIT License.