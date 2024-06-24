DEFAULT_GESTURE_CONFIG = {
    'pinch': 'select',
    'double_pinch': 'open',
    'pinch_threshold': 0.05  # Add a default pinch threshold
}

def get_gesture_config():
    return DEFAULT_GESTURE_CONFIG

def update_gesture_config(new_config):
    global DEFAULT_GESTURE_CONFIG
    DEFAULT_GESTURE_CONFIG.update(new_config)
