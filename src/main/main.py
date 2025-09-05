#!/usr/bin/env python3
import sys
import os
import configparser
from ui.window import MainWindow
from webdav.client import WebDAVClient
from api.client import APIClient

class OpenListClient:
    def __init__(self):
        self.config_path = "/var/packages/OpenList/etc/config.ini"
        self.config = self.load_config()
        self.mount_point = "/volume1/OpenList_Mount"
        self.client = None
        
    def load_config(self):
        """加载配置文件"""
        config = configparser.ConfigParser()
        if os.path.exists(self.config_path):
            config.read(self.config_path)
        return config
        
    def save_config(self):
        """保存配置文件"""
        with open(self.config_path, 'w') as f:
            self.config.write(f)
            
    def connect(self, method, server, username, password):
        """连接到OpenList服务"""
        if method == "webdav":
            self.client = WebDAVClient(server, username, password)
        else:  # api
            self.client = APIClient(server, username, password)
            
        # 保存配置
        if not self.config.has_section('Connection'):
            self.config.add_section('Connection')
        self.config.set('Connection', 'method', method)
        self.config.set('Connection', 'server', server)
        self.config.set('Connection', 'username', username)
        self.config.set('Connection', 'password', password)
        self.save_config()
        
        return self.client.test_connection()
        
    def mount(self):
        """挂载远程存储到本地目录"""
        if not self.client:
            return False
            
        return self.client.mount(self.mount_point)
        
    def unmount(self):
        """解除挂载"""
        if not self.client:
            return False
            
        return self.client.unmount(self.mount_point)

if __name__ == "__main__":
    client = OpenListClient()
    app = MainWindow(client)
    sys.exit(app.run())
