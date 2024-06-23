from flask import Flask, render_template, Response, request, jsonify
from langchain_community.llms import Ollama
import cv2

app = Flask(__name__)

def generate_frames():
    camera = cv2.VideoCapture(0)  # Use the default webcam
    while True:
        success, frame = camera.read()  # Read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Mime type and frame

@app.route('/')
def index():
    return render_template('videochat.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    local_llm = "llama3"
    llm = Ollama(model=local_llm)

    response = llm.invoke(user_message)
    return jsonify({'bot_response': response})

if __name__ == "__main__":
    app.run(debug=True)