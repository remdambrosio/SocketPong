import os
import socket
import random
import string


def main():
    parent_cha_sock, child_cha_sock = socket.socketpair()
    parent_num_sock, child_num_sock = socket.socketpair()

    pid_1 = os.fork()                   # create two children, one with pid_1 = 0, other with pid_2 = 0
    if pid_1 != 0:                      # parent has both pids > 0
        pid_2 = os.fork()
    
    if pid_1 == 0:                      # in cha child
        parent_cha_sock.close()
        parent_num_sock.close()
        child_num_sock.close()

        cha = random.choice(string.ascii_letters)
        child_cha_sock.send(str(cha).encode())
        child_cha_sock.close()

        print(f"cha child: {cha}")
        return

    if pid_2 == 0:                      # in num child
        parent_cha_sock.close()
        parent_num_sock.close()
        child_cha_sock.close()

        num = random.randint(0, 9)
        child_num_sock.send(str(num).encode())
        child_num_sock.close()

        print(f"num child: {num}")
        return

    if pid_1 != 0 and pid_2 != 0:       # in parent
        child_cha_sock.close()
        child_num_sock.close()

        cha = parent_cha_sock.recv(1024).decode()
        num = parent_num_sock.recv(1024).decode()
        parent_cha_sock.close()
        parent_num_sock.close()

        print(f"parent: {cha}{num}")
        return


if __name__ == "__main__":
    main()