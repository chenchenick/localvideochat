from flask import Blueprint, Response
from services.video_service import generate_frames

video_bp = Blueprint('video', __name__)

@video_bp.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')