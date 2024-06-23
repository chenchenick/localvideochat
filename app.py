from flask import Flask, render_template
from routes.video_route import video_bp
from routes.chat_route import chat_bp
from routes.capture_route import capture_bp

app = Flask(__name__)

app.register_blueprint(video_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(capture_bp)

@app.route('/')
def index():
    return render_template('videochat.html')

if __name__ == "__main__":
    app.run(debug=True)