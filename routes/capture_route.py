from flask import Blueprint, jsonify, request
from services.capture_service import capture_image

capture_bp = Blueprint('capture', __name__)

@capture_bp.route('/capture', methods=['POST'])
def capture():
    image_data = request.form['image_data']
    status, filename = capture_image(image_data)
    if status:
        return jsonify({'status': 'success', 'filename': filename})
    else:
        return jsonify({'status': 'failure'})