import socket
import threading

# choose nickname
nick = input('Choose your nickname: ')

# connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 21375))
except:
    exit()

canClose = False


# more formal way of disconnecting
def close(c):
    print('Disconnected from the server')
    c.close()


def receive():
    while True:
        if canClose:
            close(client)
            break

        try:
            # trying to receive a message from the server
            mess = client.recv(1024).decode('utf-8')
            if mess == 'NICK':
                client.send(nick.encode('utf-8'))
            elif mess == '':
                close(client)
                break
            else:
                print(mess)

        except:
            # close connection
            # this client.close() should be removed,
            # but for now everything is working so
            # I'll leave it here
            client.close()
            break


def write():
    global canClose
    while True:
        to_send = input("")

        if to_send == '':
            canClose = True
            break

        mess = f'{to_send}'
        client.send(mess.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

