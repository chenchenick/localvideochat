from flask import Blueprint, request, jsonify
from services.chat_service import process_message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    bot_response = process_message(user_message)
    return jsonify({'bot_response': bot_response})