from flask import Flask, jsonify, request
import webdav3.client as wc
import os
import configparser
import threading
import json

app = Flask(__name__)
config = configparser.ConfigParser()

class MountManager:
    def __init__(self):
        self.active_mounts = {}
        
    def mount_webdav(self, mount_path, url, username, password):
        try:
            options = {
                'webdav_hostname': url,
                'webdav_login': username,
                'webdav_password': password
            }
            client = wc.Client(options)
            self.active_mounts[mount_path] = client
            return True
        except Exception as e:
            return False

mount_manager = MountManager()

@app.route('/api/mount', methods=['POST'])
def create_mount():
    data = request.json
    success = mount_manager.mount_webdav(
        data['mount_path'],
        data['url'],
        data['username'],
        data['password']
    )
    return jsonify({"status": "success" if success else "error"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
