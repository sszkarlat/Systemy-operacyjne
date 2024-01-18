import threading
import socket
import random
import subprocess
import time

# default ip and port
IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 21375

# set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP_ADDRESS, PORT_NUMBER))
    server_socket.listen()
except OSError:
    print('OSError: socket already in use')

clients_dict = {}
chosen_word = ''


def disconnect_client(nickname):
    if nickname in clients_dict.keys():
        print(f'{nickname} disconnected ...')
        clients_dict[nickname].close()
        clients_dict.pop(nickname)
        send_message(nickname, f'{nickname} left the game'.encode('utf-8'))


def send_message(sender_nickname, message):
    for client_nickname, client_socket in clients_dict.items():
        if sender_nickname != client_nickname:
            client_socket.send(message)
        else:
            client_socket.send(''.encode('utf-8'))


def choose_word():
    global chosen_word
    x = random.randint(1, 3185955)
    temp_word = subprocess.check_output(
        f'head -n {x} slowa.txt | tail -1', shell=True).strip().decode('utf-8')
    if len(temp_word) <= 5:
        choose_word()
    chosen_word = ''
    for letter in temp_word:
        chosen_word += f'{letter} '
    print(f'The Chosen One: {chosen_word}')


def handle_guessing_player(nickname):
    guessed_letters = []
    allowed_errors = 7

    while True:
        try:
            current_word_state = ''
            for letter in chosen_word:
                if letter.lower() in guessed_letters:
                    current_word_state += f'{letter} '
                elif letter == ' ':
                    pass
                else:
                    current_word_state += '_ '

            if current_word_state == chosen_word:
                clients_dict[nickname].send(
                    f'Congratulations, YOU WON\nGuessed word is {chosen_word}'.encode('utf-8'))
                send_message(nickname, f'Player {nickname} just guessed the word.\nThe word was: {
                             chosen_word}\nEnding game...\nThank you for playing'.encode('utf-8'))
                time.sleep(5)
                for other_nickname in clients_dict.keys():
                    disconnect_client(other_nickname)
                break
            else:
                clients_dict[nickname].send(
                    f'You can make {allowed_errors} errors\nYour word: {current_word_state}'.encode('utf-8'))

            mess = clients_dict[nickname].recv(1024).decode('utf-8')
            mess = mess.strip()

            if len(mess) < 2:
                if mess in guessed_letters:
                    allowed_errors -= 1
                else:
                    guessed_letters.append(mess.lower())
            else:
                try_guess = ''
                for letter in mess:
                    try_guess += f'{letter} '

                if try_guess == chosen_word:
                    clients_dict[nickname].send(
                        f'Congratulations, you guessed it correctly!\nThe word was: {chosen_word}'.encode('utf-8'))
                    send_message(nickname, f'Player {nickname} just guessed the word.\nThe word was: {
                                 chosen_word}\nEnding game ...\nThank you for playing'.encode('utf-8'))
                    time.sleep(5)
                    for other_nickname in clients_dict.keys():
                        disconnect_client(other_nickname)
                    break

            if mess.lower() not in chosen_word.lower():
                allowed_errors -= 1
            if allowed_errors < 0:
                clients_dict[nickname].send(
                    f'Better luck next time, your word was:\n{chosen_word}'.encode('utf-8'))
                send_message(nickname, f'Player {
                             nickname} did not guess the word'.encode('utf-8'))
                time.sleep(5)
                disconnect_client(nickname)
                break

        except:
            disconnect_client(nickname)
            break


def receive_messages():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connected with {str(client_address)}')

        client_socket.send('NICK'.encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        clients_dict[nickname] = client_socket

        print(f'{nickname} connected to the server!')
        send_message(nickname, f'\n{
                     nickname} just joined the game!!\n'.encode('utf-8'))
        client_socket.send('Connected to the server!\n'.encode('utf-8'))

        thread = threading.Thread(
            target=handle_guessing_player, args=(nickname,))
        thread.start()


print(f'{"*" * 5} Hangman the Game {"*" * 5}')
choose_word()
receive_messages()
