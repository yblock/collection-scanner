from flask import Flask, request, jsonify, render_template, send_file
import sqlite3
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import qrcode
from io import BytesIO

# Explicitly set the template folder
app = Flask(__name__, template_folder='../templates')

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/cards.db')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../data/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No image file provided"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{image.filename}")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    # Placeholder for image processing logic
    # Example: Extract card details (name, series, market price)
    card_name = "Pikachu"  # Replace with actual recognition logic
    series = "Base Set"    # Replace with actual recognition logic
    market_price = 10.99   # Replace with actual API integration

    # Insert card details into the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cards (card_name, series, market_price, image_path)
        VALUES (?, ?, ?, ?)
    ''', (card_name, series, market_price, filepath))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Card processed and saved", "filename": filename})

@app.route('/cards', methods=['GET'])
def get_cards():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cards")
    cards = cursor.fetchall()
    conn.close()
    return jsonify(cards)

@app.route('/qr-code')
def qr_code():
    # Use the ngrok URL for the mobile URL
    server_url = "https://<random-subdomain>.ngrok.io/mobile"  # Replace with your ngrok URL
    
    # Generate the QR code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(server_url)
    qr.make(fit=True)
    
    # Create an in-memory image
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Serve the QR code image
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
