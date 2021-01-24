import paramiko
import time
from getpass import getpass

class backup:
    
    def __init__(self, ip_file):
        self.ip_file = ip_file
#        self.login()
#        self.login_to_device()

    def login(self):
        self.username = input('Enter your username: ')
        self.password = getpass('Enter you password: ')
    
    def login_to_device(self):
        with open(self.ip_file) as f:
            for ips in f.readlines():
                self.ip = ips.strip()
                self.ssh_client = paramiko.SSHClient()
                self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh_client.connect(hostname=self.ip, username=self.username, password=self.password, look_for_keys=False)
                self.command = self.ssh_client.invoke_shell()
                print (f'Sucessfully login to {self.ip}')
        
if __name__ == '__main__':
    backup = backup('ip_list.txt')
    backup.login()
    backup.login_to_device()
    
