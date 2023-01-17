import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QColor, QPalette

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EasyBrowser")
        self.setGeometry(0, 0, 1920, 990)

        # Set up dark theme
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.Text, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.BrightText, QColor(240, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        QApplication.setPalette(dark_palette)
        self.setPalette(dark_palette)

        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.urlbar = QLineEdit(self)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.browser.forward)

        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.browser.reload)

        self.browser.urlChanged.connect(self.update_urlbar)

        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.back_button)
        h_layout.addWidget(self.forward_button)
        h_layout.addWidget(self.refresh_button)
        h_layout.addWidget(self.urlbar)

        layout.addLayout(h_layout)
        layout.addWidget(self.browser)

        main_frame = QWidget(self)
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())

