# Chatbot Projects

This repository contains two chatbot projects:
- A **Web-based Chatbot** (using HTML, CSS, JavaScript)
- An **NLP-powered Chatbot** (using Python with `nlp_utils.py`)

---

## 1. Web-based Chatbot

**Description:**  
A front-end chatbot created with basic web technologies (HTML, CSS, and JavaScript). It simulates a chat interface in the browser.

**Files:**
- `chatbot.html` - Main chat interface
- `Logo.png` - Logo used in the chatbot

**How to Run:**
1. Open `chatbot.html` in any web browser (Chrome, Edge, Firefox).
2. Start chatting through the UI.

**Features:**
- Basic user interface
- Static responses (predefined or rule-based)
- Good for demonstration or prototypes

---

## 2. NLP-powered Chatbot

**Description:**  
A Python-based chatbot leveraging NLP techniques for smarter interactions.

**Folder Structure:**
- `app.py` - Main Flask app to run the server
- `chatbot.py` - Core chatbot logic
- `nlp_utils.py` - NLP utility functions (tokenization, stemming, etc.)
- `requirements.txt` - List of required Python packages
- `templates/` - HTML templates (for Flask frontend)
- `static/` - Static files like CSS and JavaScript
- `TravelPreference (1).xlsx` - Dataset possibly used for training or preferences

**How to Run:**
1. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   .\venv\Scripts\activate    # Windows
2. pip install -r requirements.txt
3. python app.py


**Features**
-Smart replies based on NLP
-Flask-based web integration
-Extendable for machine learning models
