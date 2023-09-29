# ssh_manager.py

import subprocess
from config import Config

class SSHManager:
    def __init__(self):
        self.config = Config()

    def execute_ssh_command(self, command):
        ssh_command = [
            'ssh',
            '-i', self.config.ssh_key_path,
            f'{self.config.ssh_user}@{self.config.remote_host}',
            command
        ]

        try:
            subprocess.run(ssh_command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error executing SSH command: {e}")
            return False
