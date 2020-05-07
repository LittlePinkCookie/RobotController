import sys
from PyQt5.QtWidgets import QWidget, QApplication

from src.main.python.view.VideoPreview import VideoPreview


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Robot Controller'
        self.width = 640
        self.height = 480

        self.video_preview = VideoPreview(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        # Add video preview
        self.show()


class GUI(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = Window()

    def start_ui(self):
        self.window.init_ui()
        sys.exit(self.exec_())
