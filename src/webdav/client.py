import subprocess
import os
import requests

class WebDAVClient:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.mounted = False
        
    def test_connection(self):
        """测试WebDAV连接是否有效"""
        try:
            response = requests.request(
                'PROPFIND', 
                self.server,
                auth=(self.username, self.password),
                headers={'Depth': '1'},
                timeout=10
            )
            return response.status_code in [207, 401]
        except Exception as e:
            print(f"连接测试失败: {str(e)}")
            return False
            
    def mount(self, mount_point):
        """使用rclone挂载WebDAV存储"""
        # 检查rclone是否安装
        if not self._check_rclone():
            return False
            
        # 配置rclone
        self._configure_rclone()
        
        # 执行挂载命令
        cmd = [
            'rclone', 'mount', 
            'openlist_webdav:', 
            mount_point,
            '--daemon',
            '--allow-other',
            '--vfs-cache-mode', 'full'
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            self.mounted = True
            return True
        except subprocess.CalledProcessError as e:
            print(f"挂载失败: {e.stderr}")
            return False
            
    def unmount(self, mount_point):
        """解除挂载"""
        if not self.mounted:
            return True
            
        try:
            subprocess.run(['fusermount', '-u', mount_point], check=True)
            self.mounted = False
            return True
        except subprocess.CalledProcessError as e:
            print(f"解除挂载失败: {str(e)}")
            return False
            
    def _check_rclone(self):
        """检查rclone是否安装"""
        try:
            subprocess.run(['rclone', 'version'], check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("rclone未安装，尝试安装...")
            return self._install_rclone()
            
    def _install_rclone(self):
        """安装rclone"""
        try:
            subprocess.run(
                ['curl', 'https://rclone.org/install.sh', '|', 'sudo', 'bash'],
                shell=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"rclone安装失败: {str(e)}")
            return False
            
    def _configure_rclone(self):
        """配置rclone连接"""
        config_content = f"""[openlist_webdav]
type = webdav
url = {self.server}
vendor = other
user = {self.username}
pass = {self.password}
"""
        # 写入rclone配置
        rclone_config_dir = os.path.expanduser('~/.config/rclone')
        os.makedirs(rclone_config_dir, exist_ok=True)
        rclone_config_path = os.path.join(rclone_config_dir, 'rclone.conf')
        
        with open(rclone_config_path, 'w') as f:
            f.write(config_content)
