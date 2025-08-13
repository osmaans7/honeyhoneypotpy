# honeyhoneypotpy

This program is a honeypot that will capture IP Addresses, usernames, passwords, and commands from SSH and HTTP protocol. It is all written in python.


Install
1) Clone repository. git@github.com:osmaans7/cc-honeyhoneypotpy.git

2) Permissions. Move into ssh_honeypy folder.

Ensure main.py has proper permisions. (chmod 755 honeypy.py)

3) Keygen.

Create a new folder static.

mkdir static

Move into directory.

cd static

An RSA key must be generated for the SSH server host key. The SSH host key provides proper identification for the SSH server. Ensure the key is titled server.key and resides in the same relative directory to the main program.

ssh-keygen -t rsa -b 2048 -f server.key
