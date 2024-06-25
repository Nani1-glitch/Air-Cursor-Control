# 🎈💻 AIR CURSOR CONTROL 🌟👆

Welcome to the **AIR CURSOR CONTROL** project! This innovative project leverages the power of Mediapipe and OpenCV to create an intuitive cursor control system using hand gestures. The system primarily tracks the index finger for cursor movement and detects a pinch gesture with the thumb and index finger for accurate selection actions. 🖱️✨

## 📋 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 📖 Introduction
This project aims to provide a natural and intuitive way to control the cursor on your screen using hand gestures. By tracking the index finger and detecting pinch gestures with the thumb, users can navigate and interact with their computer without touching any physical device. This can be particularly useful for touchless interfaces and accessibility applications. 👐🌟

## 👨‍💻 About the Author
Hi, I'm Nithin Rajulapati! I'm a master's student with a strong background in computer science and extensive training in artificial intelligence. I am passionate about developing innovative solutions and leveraging AI to create intuitive and effective user interfaces. 🤖📚💡

## 🤝 Contributing
We welcome contributions to enhance the functionality and features of this project. To contribute:

## Fork the repository 🍴
Create a new branch for your feature or bugfix 🌿
Submit a pull request with a detailed description of your changes 🔄


## ✨ Features
- **Real-time Finger Tracking** 🎥: Uses Mediapipe to track the index finger in real-time.
- **Pinch Gesture Detection** 🤏: Detects pinch gestures between the thumb and index finger to perform click actions.
- **Smooth Cursor Movement** 💨: Applies smoothing algorithms to ensure stable and precise cursor control.
- **Configurable Settings** ⚙️: Allows customization of gesture detection thresholds and actions.

## 🛠️ Installation
Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository** 🐙:
    ```sh
    git clone https://github.com/Nani1-glitch/air-cursor-control.git
    cd air-cursor-control
    ```

2. **Install Dependencies** 📦:
    Make sure you have Python 3.x installed. Then, install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application** 🚀:
    Start the backend server:
    ```sh
    python app.py
    ```

## 🚀 Usage
1. Open your web browser and navigate to `http://127.0.0.1:5001`.
2. You'll see the video feed from your webcam with the tracked finger. 📹👆
3. Move your index finger to control the cursor on the screen. 🖱️
4. Pinch your thumb and index finger together to perform a click action. 🤏✔️

## ⚙️ Configuration

You can customize the gesture detection settings by modifying the `config.py` file. The default settings are:

```python
DEFAULT_GESTURE_CONFIG = {
    'pinch': 'select',
    'double_pinch': 'open',
    'pinch_threshold': 0.05  # Default pinch threshold
}
Adjust the pinch_threshold to change the sensitivity of the pinch detection. 🎯


