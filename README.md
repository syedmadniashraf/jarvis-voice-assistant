# 🤖 Jarvis Voice Assistant

A smart voice-controlled assistant built using Python that can perform tasks like playing any song, opening websites, and reading the latest news using voice commands.

---

## 📌 About

Jarvis is a desktop voice assistant inspired by AI assistants like Iron Man’s JARVIS.
It uses speech recognition and text-to-speech to interact with users and automate everyday tasks.

This project demonstrates how to build a basic AI assistant using Python with real-time features.

---

## 🚀 Features

* 🎤 Voice Recognition (Speech-to-Text)
* 🔊 Text-to-Speech response
* 🎵 Play ANY song from YouTube
* 🌐 Open ANY website
* 📰 Get latest news using News API
* ⏹️ Stop news anytime using voice command
* ⚡ Wake word activation ("Jarvis")

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* requests
* python-dotenv
* pywhatkit
* webbrowser

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/syedmadniashraf/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Setup

Create a `.env` file in the root directory and add your API key:

```
NEWS_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the program:

```
python main.py
```

---

## 🗣️ Example Commands

* "Jarvis" → Activate assistant
* "Play kesariya" → Plays any song
* "Open instagram" → Opens any website
* "News" → Reads latest news
* "Stop" → Stops news / exits

---

## 📁 Project Structure

```
jarvis-voice-assistant/
│── main.py
│── requirements.txt
│── README.md
│── .env (not included)
```

---

## ⚠️ Limitations

* Requires internet connection
* Voice recognition depends on microphone quality
* News API has request limits
* Browser autoplay may vary

---

## 🔮 Future Improvements

* Add ChatGPT integration 🤖
* Add GUI interface
* Add more commands (weather, time, reminders)
* Background listening mode

---

## 👨‍💻 Author

**Syed Madni Ashraf**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is open-source and free to use.
