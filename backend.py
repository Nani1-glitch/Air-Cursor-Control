from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import config

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/config', methods=['GET', 'POST'])
def handle_config():
    if request.method == 'POST':
        new_config = request.json
        config.update_gesture_config(new_config)
        return jsonify({'status': 'success', 'new_config': config.get_gesture_config()})
    return jsonify(config.get_gesture_config())

if __name__ == '__main__':
    socketio.run(app, debug=True)
