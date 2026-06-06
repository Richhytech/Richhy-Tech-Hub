import sys
import cv2
import numpy as np
import pyaudio
import struct

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from nova.voice import listen, speak
from nova.core import respond


# 🎤 BACKGROUND VOICE THREAD (NO FREEZE
class VoiceThread(QThread):
    result_signal = pyqtSignal(str)

    def run(self):
        user = listen()
        if user:
            self.result_signal.emit(user)


class NovaGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA HUD")
        self.showFullScreen()

        self.setStyleSheet("""
            background-color: black;
            color: cyan;
            font-family: Consolas;
        """)

        layout = QVBoxLayout()

        # 🔵 TITLE (ANIMATED)
        self.title = QLabel("NOVA SYSTEM ONLINE")
        self.title.setAlignment(Qt.AlignCenter)

        # 💬 CHAT
        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setStyleSheet("border: 2px solid cyan;")

        # 🎥 CAMERA
        self.camera_label = QLabel()
        self.camera_label.setFixedHeight(250)

        # 🔊 WAVEFORM DISPLAY
        self.wave_label = QLabel()
        self.wave_label.setFixedHeight(100)

        layout.addWidget(self.title)
        layout.addWidget(self.chat)
        layout.addWidget(self.wave_label)
        layout.addWidget(self.camera_label)

        self.setLayout(layout)

        # 🎥 CAMERA INIT
        self.cap = cv2.VideoCapture(self.find_camera())

        # FACE DETECTOR
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # 🎥 CAMERA TIMER
        self.cam_timer = QTimer()
        self.cam_timer.timeout.connect(self.update_camera)
        self.cam_timer.start(30)

        # 🔊 WAVE TIMER
        self.wave_timer = QTimer()
        self.wave_timer.timeout.connect(self.update_waveform)
        self.wave_timer.start(100)

        # 🎤 VOICE LOOP TIMER
        self.voice_timer = QTimer()
        self.voice_timer.timeout.connect(self.start_listening)
        self.voice_timer.start(7000)

        # 🎨 TITLE ANIMATION
        self.anim_timer = QTimer()
        self.anim_timer.timeout.connect(self.animate_title)
        self.anim_timer.start(500)

        # 🎤 AUDIO STREAM FOR WAVEFORM
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024
        )

    # 🎥 FIND CAMERA (Iriun supported)
    def find_camera(self):
        for i in range(5):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                cap.release()
                return i
        return 0

    # 🎥 CAMERA + FACE DETECTION
    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.camera_label.setPixmap(QPixmap.fromImage(img))

    # 🔊 REAL WAVEFORM
    def update_waveform(self):
        try:
            data = self.stream.read(1024, exception_on_overflow=False)
            samples = struct.unpack('1024h', data)
            amplitude = np.abs(samples).mean()

            bars = int(amplitude / 1000)
            waveform = "|" * bars

            self.wave_label.setText(waveform)
        except:
            pass

    # 🎤 START VOICE THREAD
    def start_listening(self):
        self.chat.append("🎤 Listening...")
        self.voice_thread = VoiceThread()
        self.voice_thread.result_signal.connect(self.process_voice)
        self.voice_thread.start()

    # 🤖 PROCESS VOICE RESULT
    def process_voice(self, user):
        self.chat.append(f"You: {user}")

        reply = respond(user)

        self.chat.append(f"NOVA: {reply}")
        speak(reply)

    # 🎨 ANIMATED TITLE
    def animate_title(self):
        import random
        size = random.randint(24, 32)
        self.title.setStyleSheet(f"font-size: {size}px; color: cyan;")

    def closeEvent(self, event):
        self.cap.release()
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()


def start_gui():
    app = QApplication(sys.argv)
    win = NovaGUI()
    win.show()
    sys.exit(app.exec_())