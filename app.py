import eventlet
import cv2
import pyautogui
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, Response, send_from_directory, request, jsonify
from hand_tracker import detect_pinch_and_move_cursor
import config

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

cap = None
tracking = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/start_tracking')
def start_tracking():
    global tracking, cap
    if not tracking:
        cap = cv2.VideoCapture(0)
        tracking = True
        socketio.start_background_task(track)
    return {'status': 'tracking started'}

@app.route('/stop_tracking')
def stop_tracking():
    global tracking, cap
    if tracking:
        tracking = False
        cap.release()
    return {'status': 'tracking stopped'}

@app.route('/config', methods=['POST'])
def config_route():
    if request.method == 'POST':
        data = request.get_json()
        # Update your configuration based on the received data
        config.update_gesture_config(data)
        return jsonify({'status': 'success', 'config': config.get_gesture_config()})

def track():
    global cap, tracking
    while tracking:
        ret, frame = cap.read()
        if not ret:
            continue

        frame, pinch_detected = detect_pinch_and_move_cursor(frame, config.get_gesture_config())
        
        if pinch_detected == 'select':
            pyautogui.click()
        elif pinch_detected == 'open':
            pyautogui.doubleClick()

        # Encode the frame in JPEG format
        (flag, encoded_image) = cv2.imencode(".jpg", frame)
        if not flag:
            continue

        # Yield the output frame in byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate():
    global cap, tracking
    while tracking:
        ret, frame = cap.read()
        if not ret:
            continue

        frame, pinch_detected = detect_pinch_and_move_cursor(frame, config.get_gesture_config())
        
        if pinch_detected == 'select':
            pyautogui.click()
        elif pinch_detected == 'open':
            pyautogui.doubleClick()

        # Encode the frame in JPEG format
        (flag, encoded_image) = cv2.imencode(".jpg", frame)
        if not flag:
            continue

        # Yield the output frame in byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')

if __name__ == '__main__':
    print("Starting the server at http://127.0.0.1:5001")
    socketio.run(app, host='127.0.0.1', port=5001, debug=True)
