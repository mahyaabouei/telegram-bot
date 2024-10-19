'''
For subscription of Farasite  
connect to telegram Bot
'''

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# توکن بات تلگرام و شناسه چت مورد نظر را مشخص کنید
TOKEN = '7029103499:AAGTuXTGfx4pMiDZH_GJPvb1vMMXgP5Z9FI'  # جایگزین کنید با توکن بات خود

TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

@app.route('/send_message/', methods=['POST'])
def send_message():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    message = data['message']
    CHAT_ID = data['chat_id']
    payload = { 
        'chat_id': CHAT_ID,
        'text': message
    }

    try:
        response = requests.post(TELEGRAM_API_URL, json=payload)
        response_data = response.json()
        if response.status_code == 200 and response_data['ok']:
            return jsonify({'status': 'Message sent', 'telegram_response': response_data}), 200
        else:
            return jsonify({'error': 'Failed to send message', 'telegram_response': response_data}), 500
    except Exception as e:
        return jsonify({'error': 'Exception', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=8080)
