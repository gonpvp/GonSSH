import time
import sys
import os
from secret import *

import paramiko
from rich import print
from rich.console import Console

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def execute():
    console = Console()
    print('[bold red]Wait...')
    ssh.connect(getconfig.ip(), username=getconfig.username(), password=getconfig.password(), port=getconfig.port())
    print('[green]connected !')
    while True:
        command = console.input("[bold magenta]Type[/] the [bold red]command[/]: ")
        if command == 'close':
            print('[bold red]ByeBye my friend !')
            break
        else:
            (stdin, stdout, stderr) = ssh.exec_command(command, get_pty = True)
            output = stdout.readlines()
            for i in output:
                print(i)

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
slowprint("Made By GonPvP ...")
execute()
