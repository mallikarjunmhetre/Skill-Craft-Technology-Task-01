from flask import Flask, render_template, request, jsonify
import string
import time
import random
import hashlib
import base64
app = Flask(__name__)
# ─────────────────────────────────────────────
#  Caesar Cipher Core Logic
# ─────────────────────────────────────────────
def caesar_encrypt(text, shift):
    result = []
    shift = shift % 26
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def brute_force_decrypt(ciphertext):
    results = []
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append({
            "shift": shift,
            "text": decrypted
        })
    return results
def frequency_analysis(text):
    text_upper = text.upper()
    letters = [ch for ch in text_upper if ch.isalpha()]
    total = len(letters)
    if total == 0:
        return {}
    freq = {}
    for letter in string.ascii_uppercase:
        count = letters.count(letter)
        freq[letter] = {
            "count": count,
            "percentage": round((count / total) * 100, 2)
        }
    return freq
def calculate_entropy(text):
    """Shannon entropy of text"""
    if not text:
        return 0
    from collections import Counter
    import math
    freq = Counter(text)
    length = len(text)
    entropy = -sum((count/length) * math.log2(count/length) for count in freq.values())
    return round(entropy, 4)
def get_stats(text):
    letters = sum(1 for c in text if c.isalpha())
    digits  = sum(1 for c in text if c.isdigit())
    spaces  = sum(1 for c in text if c == ' ')
    special = len(text) - letters - digits - spaces
    return {
        "total_chars": len(text),
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "special": special,
        "entropy": calculate_entropy(text)
    }
def rot13(text):
    return caesar_encrypt(text, 13)
def vigenere_encrypt(text, keyword):
    keyword = keyword.upper()
    result = []
    key_idx = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(keyword[key_idx % len(keyword)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            key_idx += 1
        else:
            result.append(ch)
    return ''.join(result)
def vigenere_decrypt(text, keyword):
    keyword = keyword.upper()
    result = []
    key_idx = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(keyword[key_idx % len(keyword)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            key_idx += 1
        else:
            result.append(ch)
    return ''.join(result)
def atbash_cipher(text):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr(base + 25 - (ord(ch) - base)))
        else:
            result.append(ch)
    return ''.join(result)
# ─────────────────────────────────────────────
#  Routes – Pages
# ─────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/encrypt')
def encrypt_page():
    return render_template('encrypt.html')
@app.route('/decrypt')
def decrypt_page():
    return render_template('decrypt.html')
@app.route('/tools')
def tools_page():
    return render_template('tools.html')
@app.route('/about')
def about_page():
    return render_template('about.html')
# ─────────────────────────────────────────────
#  API Endpoints
# ─────────────────────────────────────────────
@app.route('/api/encrypt', methods=['POST'])
def api_encrypt():
    data = request.get_json()
    text  = data.get('text', '')
    shift = int(data.get('shift', 3))
    if not text:
        return jsonify({"error": "No text provided"}), 400
    encrypted  = caesar_encrypt(text, shift)
    stats      = get_stats(text)
    enc_stats  = get_stats(encrypted)
    freq_plain = frequency_analysis(text)
    freq_enc   = frequency_analysis(encrypted)
    return jsonify({
        "original":  text,
        "encrypted": encrypted,
        "shift":     shift,
        "stats":     stats,
        "enc_stats": enc_stats,
        "freq_plain": freq_plain,
        "freq_enc":   freq_enc
    })
@app.route('/api/decrypt', methods=['POST'])
def api_decrypt():
    data = request.get_json()
    text  = data.get('text', '')
    shift = int(data.get('shift', 3))
    if not text:
        return jsonify({"error": "No text provided"}), 400
    decrypted  = caesar_decrypt(text, shift)
    stats      = get_stats(text)
    freq_plain = frequency_analysis(text)
    freq_dec   = frequency_analysis(decrypted)
    return jsonify({
        "original":  text,
        "decrypted": decrypted,
        "shift":     shift,
        "stats":     stats,
        "freq_plain": freq_plain,
        "freq_dec":   freq_dec
    })
@app.route('/api/brute-force', methods=['POST'])
def api_brute_force():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    results = brute_force_decrypt(text)
    return jsonify({"results": results})
@app.route('/api/frequency', methods=['POST'])
def api_frequency():
    data = request.get_json()
    text = data.get('text', '')
    freq = frequency_analysis(text)
    return jsonify({"frequency": freq, "entropy": calculate_entropy(text)})
@app.route('/api/vigenere', methods=['POST'])
def api_vigenere():
    data    = request.get_json()
    text    = data.get('text', '')
    keyword = data.get('keyword', 'KEY')
    mode    = data.get('mode', 'encrypt')
    if not text or not keyword:
        return jsonify({"error": "Text and keyword required"}), 400
    if mode == 'encrypt':
        result = vigenere_encrypt(text, keyword)
    else:
        result = vigenere_decrypt(text, keyword)
    return jsonify({"result": result, "keyword": keyword, "mode": mode})
@app.route('/api/atbash', methods=['POST'])
def api_atbash():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = atbash_cipher(text)
    return jsonify({"result": result})
@app.route('/api/rot13', methods=['POST'])
def api_rot13():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = rot13(text)
    return jsonify({"result": result})
@app.route('/api/hash', methods=['POST'])
def api_hash():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    return jsonify({
        "md5":    hashlib.md5(text.encode()).hexdigest(),
        "sha1":   hashlib.sha1(text.encode()).hexdigest(),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "base64": base64.b64encode(text.encode()).decode()
    })
@app.route('/api/random-key', methods=['GET'])
def api_random_key():
    shift   = random.randint(1, 25)
    keyword = ''.join(random.choices(string.ascii_uppercase, k=random.randint(4, 10)))
    return jsonify({"shift": shift, "keyword": keyword})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
