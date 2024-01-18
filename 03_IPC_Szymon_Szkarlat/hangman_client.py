import socket
import threading

def get_user_nickname():
    return input('Choose your nickname: ')

def establish_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 21375))
    except:
        exit()

    return client_socket

def disconnect(client_socket):
    print('Disconnected from the server')
    client_socket.close()

def receive_messages(client_socket, close_flag):
    while True:
        if close_flag[0]:
            disconnect(client_socket)
            break

        try:
            received_message = client_socket.recv(1024).decode('utf-8')
            if received_message == 'NICK':
                client_socket.send(nick.encode('utf-8'))
            elif received_message == '':
                disconnect(client_socket)
                break
            else:
                print(received_message)

        except:
            client_socket.close()
            break

def send_messages(client_socket, close_flag):
    while True:
        user_input = input("")

        if user_input == '':
            close_flag[0] = True
            break

        message_to_send = f'{user_input}'
        client_socket.send(message_to_send.encode('utf-8'))

def main():
    global nick
    nick = get_user_nickname()

    client = establish_connection()
    can_close = [False]

    receive_thread = threading.Thread(target=receive_messages, args=(client, can_close))
    receive_thread.start()

    write_thread = threading.Thread(target=send_messages, args=(client, can_close))
    write_thread.start()

if __name__ == "__main__":
    main()
