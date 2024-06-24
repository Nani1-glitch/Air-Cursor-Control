import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cursor_movement_enabled = True  # Global flag to enable/disable cursor movement

def detect_pinch_and_move_cursor(frame, gesture_config):
    global cursor_movement_enabled
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    screen_width, screen_height = pyautogui.size()
    pinch_detected = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_tip = hand_landmarks.landmark[4]
            index_finger_tip = hand_landmarks.landmark[8]

            # Calculate distance between thumb tip and index finger tip
            distance = ((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2) ** 0.5
            pinch_threshold = gesture_config.get('pinch_threshold', 0.05)  # Default pinch threshold

            if distance < pinch_threshold:  # Pinch detected
                pinch_detected = gesture_config.get('pinch', 'select')
                cursor_movement_enabled = False
            else:
                cursor_movement_enabled = True

            if cursor_movement_enabled:
                # Invert x-coordinates
                cursor_x = screen_width - int(index_finger_tip.x * screen_width)
                cursor_y = int(index_finger_tip.y * screen_height)
                smooth_move(cursor_x, cursor_y)

            # Draw landmarks for thumb and index finger only
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                                      connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))

    return frame, pinch_detected

previous_position = None

def smooth_move(x, y, smoothing_factor=0.2, min_movement_threshold=5):
    global previous_position
    if previous_position is None:
        previous_position = np.array([x, y])
        pyautogui.moveTo(x, y)
    else:
        current_position = np.array([x, y])
        if np.linalg.norm(current_position - previous_position) > min_movement_threshold:
            smoothed_position = previous_position + smoothing_factor * (current_position - previous_position)
            pyautogui.moveTo(smoothed_position[0], smoothed_position[1])
            previous_position = smoothed_position
