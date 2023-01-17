import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EasyBrowser")
        self.setGeometry(0, 0, 1920, 990)

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

