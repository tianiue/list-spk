#!/usr/bin/env python3
import webdav3.client as wc
from flask import Flask, jsonify
import os
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()

class OpenListManager:
    def __init__(self):
        self.mount_points = {}
        
    def webdav_login(self, url, username, password):
        options = {
            'webdav_hostname': url,
            'webdav_login': username,
            'webdav_password': password
        }
        return wc.Client(options)
...
