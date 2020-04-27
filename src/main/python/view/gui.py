from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Robot Controller v0.1")

        toolbar = QToolBar("Ma toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        bt_action = QAction(QIcon("src/main/icons/fugue/bug.png"), "Action", self)
        bt_action.setStatusTip("un status tip")
        bt_action.setCheckable(True)
        bt_action.triggered.connect(self.toolbarClick)
        toolbar.addAction(bt_action)

        toolbar.addSeparator()

        bt_action2 = QAction(QIcon("src/main/icons/fugue/camera.png"), "Record", self)
        bt_action2.setStatusTip("Record cam")
        bt_action2.setCheckable(True)
        bt_action2.triggered.connect(self.toolbarClick)
        toolbar.addAction(bt_action2)

        toolbar.addWidget(QCheckBox("Check it"))

        layout = QVBoxLayout()
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setStatusBar(QStatusBar(self))


    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        print("Context menu")

    def toolbarClick(self, e):
        print("click ", e)

class GUI:

    def __init__(self):
        self.app = QApplication([])
        self.window = MainWindow()
        self.window.setFixedSize(640, 480)
        self.window.show()

    def start_ui(self):
        self.app.exec_()
