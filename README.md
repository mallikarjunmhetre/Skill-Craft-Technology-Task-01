# Skill-Craft-Technology-Task-01
Skill Craft Technology Cyber Security Internship Projects.
# 🔐 CipherX — Advanced Caesar Cipher Cybersecurity Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A full-stack **cybersecurity-themed** web application for encrypting and decrypting text using classical cipher algorithms. Built with Python Flask backend and a premium dark-themed frontend.

---

## 🌐 Live Demo

> Run locally: **http://127.0.0.1:5000**

---

## 📸 Pages Overview

| Page | URL | Description |
|------|-----|-------------|
| 🏠 Home | `/` | Live demo, feature cards, alphabet map visualizer |
| 🔒 Encrypt | `/encrypt` | Caesar cipher encryptor with frequency analysis |
| 🔓 Decrypt | `/decrypt` | Known-key decrypt + 25-shift brute-force attack |
| 🛠️ Tools | `/tools` | Vigenère, Atbash, ROT13, Hash, Base64, Frequency |
| 📖 About | `/about` | Cryptography history timeline & cipher comparison |

---

## 📁 Project Structure

```
caesar_cipher/
│
├── app.py                        # Flask backend — all cipher logic & API routes
│
├── templates/                    # HTML pages (Jinja2 templates)
│   ├── index.html                # 🏠 Home page
│   ├── encrypt.html              # 🔒 Encrypt page
│   ├── decrypt.html              # 🔓 Decrypt page
│   ├── tools.html                # 🛠️ Crypto tools page
│   └── about.html                # 📖 History & theory page
│
├── static/
│   ├── css/
│   │   └── style.css             # Global design system (dark cyberpunk theme)
│   └── js/
│       └── common.js             # Shared JS utilities
│
└── README.md                     # Project documentation
```

---

## ✨ Key Features

### 🔒 Caesar Cipher Core
- ✅ Encrypt any text with a custom shift value (1–25)
- ✅ Decrypt with known shift key
- ✅ **Brute-force attack** — automatically tries all 25 shifts
- ✅ Real-time letter-by-letter shift visualization

### 📊 Cryptanalysis Tools
- ✅ **Frequency Analysis** — bar chart of letter distribution
- ✅ **Shannon Entropy** calculation for plaintext vs ciphertext
- ✅ Smart shift **guess** based on most-frequent letter (E-theory)
- ✅ Security strength meter

### 🛠️ Extended Cipher Suite
- ✅ **Vigenère Cipher** — polyalphabetic encrypt & decrypt
- ✅ **Atbash Cipher** — reverse-alphabet substitution
- ✅ **ROT13** — live bidirectional encoding
- ✅ **Base64** encode & decode
- ✅ **MD5, SHA-1, SHA-256** hash functions

### 🎨 Premium UI/UX
- ✅ Cyberpunk dark theme with neon glow effects
- ✅ Animated matrix rain background (canvas)
- ✅ Glassmorphism cards with hover animations
- ✅ Interactive shift sliders with live preview
- ✅ Toast notifications & clipboard copy
- ✅ Keyboard shortcut (`Ctrl+Enter` to encrypt/decrypt)
- ✅ Fully responsive layout

### 🔗 REST API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/encrypt` | POST | Caesar encrypt |
| `/api/decrypt` | POST | Caesar decrypt |
| `/api/brute-force` | POST | Try all 25 shifts |
| `/api/frequency` | POST | Letter frequency analysis |
| `/api/vigenere` | POST | Vigenère encrypt/decrypt |
| `/api/atbash` | POST | Atbash cipher |
| `/api/rot13` | POST | ROT13 cipher |
| `/api/hash` | POST | MD5, SHA1, SHA256, Base64 |
| `/api/random-key` | GET | Generate random shift + keyword |

---

## 🛠️ Tools & Technologies Used

### Backend
| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Flask 3.1** | Web framework & REST API |
| **hashlib** | MD5, SHA-1, SHA-256 hashing |
| **base64** | Base64 encoding/decoding |
| **math** | Shannon entropy calculation |
| **string / random** | Key generation utilities |

### Frontend
| Tool | Purpose |
|------|---------|
| **HTML5** | Page structure & semantic markup |
| **CSS3** | Custom design system, animations, glassmorphism |
| **Vanilla JavaScript** | Interactivity, API calls, DOM manipulation |
| **Canvas API** | Matrix rain background animation |
| **Google Fonts** | Orbitron, Inter, JetBrains Mono |
| **Fetch API** | Async REST API communication |

### Cybersecurity Concepts Demonstrated
| Concept | Where Used |
|---------|-----------|
| Caesar Cipher | Encrypt / Decrypt pages |
| Vigenère Cipher | Tools page |
| Atbash Cipher | Tools page |
| ROT13 | Tools page |
| Frequency Analysis | Encrypt, Decrypt, Tools pages |
| Brute-force Attack | Decrypt page |
| Shannon Entropy | All cipher pages |
| MD5 / SHA-1 / SHA-256 | Tools → Hash section |
| Base64 Encoding | Tools → Base64 section |
| Cryptographic History | About page |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation & Run

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/cipherx.git
cd cipherx/caesar_cipher

# 2. Install dependencies
pip install flask

# 3. Run the app
python app.py

# 4. Open in browser
# → http://127.0.0.1:5000
```

---

## 📖 How Caesar Cipher Works

```
Plaintext:  H E L L O
Shift:      3 3 3 3 3
            ↓ ↓ ↓ ↓ ↓
Ciphertext: K H O O R
```

**Formula:**
- Encrypt: `C = (P + shift) mod 26`
- Decrypt: `P = (C - shift + 26) mod 26`

Where `P` = plaintext letter position (A=0, Z=25), `C` = ciphertext letter position.

---

## 🔑 Example API Usage

```bash
# Encrypt
curl -X POST http://127.0.0.1:5000/api/encrypt \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World", "shift": 3}'

# Response
{
  "original": "Hello World",
  "encrypted": "Khoor Zruog",
  "shift": 3,
  "stats": { "total_chars": 11, "letters": 10, "entropy": 3.1219 }
}
```

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Mallikarjun** — Built with ❤️ using Python Flask & Vanilla JS

> ⭐ If you found this helpful, please **star** this repository!
