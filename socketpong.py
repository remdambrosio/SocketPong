import os
import socket
import random
import string


def main():
    ping_sock, pong_sock = socket.socketpair()
    pid = os.fork()

    if pid != 0:                                    # parent/pinger
        pong_sock.close()
        ping = random.randint(0, 9)
        ping_sock.send(str(ping).encode())
        ping_sock.close()
    else:                                           # child/ponger
        ping_sock.close()
        ping = pong_sock.recv(1024).decode()
        pong = random.choice(string.ascii_letters)
        pong_sock.close()
        print(f"Ping: {ping}, Pong: {pong}")


if __name__ == "__main__":
    main()