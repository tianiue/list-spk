import sys
import json
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, 
                            QLineEdit, QPushButton, QFileDialog)

class OpenListClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_config()
        
    def initUI(self):
        self.setWindowTitle('OpenList Mount Manager')
        self.tabs = QTabWidget()
        
        # Auth Tab
        self.auth_type = QComboBox()
        self.auth_type.addItems(['API Token', 'Password'])
        
        self.api_token = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        # Mount Tab
        self.mount_path = QLineEdit()
        self.browse_btn = QPushButton('Browse')
        self.browse_btn.clicked.connect(self.select_mount_path)
        
        self.save_btn = QPushButton('Save Config')
        self.save_btn.clicked.connect(self.save_config)
        
    def select_mount_path(self):
        path = QFileDialog.getExistingDirectory()
        if path:
            self.mount_path.setText(path)
            
    def save_config(self):
        config = {
            "auth_type": "api" if self.auth_type.currentIndex() == 0 else "password",
            "api_token": self.api_token.text(),
            "username": self.username.text(),
            "password": self.password.text(),
            "mount_point": self.mount_path.text()
        }
        with open('/var/packages/OpenListMount/etc/config.json', 'w') as f:
            json.dump(config, f)
            
    def load_config(self):
        try:
            with open('/var/packages/OpenListMount/etc/config.json', 'r') as f:
                config = json.load(f)
                # Update UI fields...
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenListClient()
    ex.show()
    sys.exit(app.exec_())
