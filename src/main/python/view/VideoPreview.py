import cv2
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget


class Thread(QThread):
    change_pixel_map = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture('tcp://192.168.1.43:8090')  # how to use VideoCapture with online stream?
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixel_map.emit(p)


class VideoPreview(QLabel):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.resize(640, 480)

        th = Thread(self)
        th.change_pixel_map.connect(self.set_image)
        th.start()

    @pyqtSlot(QImage)
    def set_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))