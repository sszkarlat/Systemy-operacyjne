import threading
import socket
import random
import subprocess
import time

# default ip and port
IP = '127.0.0.1'
PORT = 21375

# setting up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((IP, PORT))
    server.listen()
except OSError:
    print('OSError: socket already in use')

# dict that contains nickname and info about client
clients = {}
word = ''


def disconnect(nick):
    if nick in clients.keys():
        print(f'{nick} disconnected ...')
        clients[nick].close()
        clients.pop(nick)
        send_mess(nick, f'{nick} left the game'.encode('utf-8'))


# sending message to everyone except client that sent that mess
def send_mess(nick, mess):
    for k, v in clients.items():
        if nick != k:
            v.send(mess)
        else:
            # this else must be here
            # else sends message to client
            # thanks that it knows whether the client disconnects or not
            v.send(''.encode('utf-8'))


def find_word():
    global word
    x = random.randint(1, 3185955)
    temp_word = subprocess.check_output(f'head -n {x} slowa.txt | tail -1', shell=True).strip().decode('utf-8')
    if len(temp_word) <= 5:
        find_word()
    word = ''
    for letter in temp_word:
        word += f'{letter} '
    print(f'The Chosen One: {word}')


# handle mess from clients
def handle(nick):
    guesses = []
    allowed_errors = 7

    while True:
        try:
            # update the current state of the guessed word
            temp_word = ''
            for letter in word:
                if letter.lower() in guesses:
                    temp_word += f'{letter} '
                elif letter == ' ':
                    pass
                else:
                    temp_word += '_ '

            # find out if the word was guessed
            if temp_word == word:
                clients[nick].send(
                    f'Congratulations, YOU WON\nGuessed word is {word}'.encode('utf-8'))
                send_mess(nick, f'Player {nick} just guessed the word.\nThe word was: {word}\nEnding game...\nThank you for playing'.encode('utf-8'))
                time.sleep(5)
                for c in clients.keys():
                    disconnect(c)
                break
            else:
                clients[nick].send(
                    f'You can make {allowed_errors} errors\nYour word: {temp_word}'.encode('utf-8'))

            # receive a message from the client
            mess = clients[nick].recv(1024).decode('utf-8')
            mess = mess.strip()

            # check if the player is guessing the whole word or just 1 letter
            if len(mess) < 2:
                if mess in guesses:
                    allowed_errors -= 1
                else:
                    guesses.append(mess.lower())
            else:
                try_guess = ''
                for letter in mess:
                    try_guess += f'{letter} '

                if try_guess == word:
                    clients[nick].send(
                        f'Congratulations, you guessed it correctly!\nThe word was: {word}'.encode('utf-8'))
                    send_mess(nick, f'Player {nick} just guessed the word.\nThe word was: {word}\nEnding game ...\nThank you for playing'.encode('utf-8'))
                    time.sleep(5)
                    for c in clients.keys():
                        disconnect(c)
                    break

            # handle allowed errors
            if mess.lower() not in word.lower():
                allowed_errors -= 1
            if allowed_errors < 0:
                clients[nick].send(
                    f'Better luck next time, your word was:\n{word}'.encode('utf-8'))
                send_mess(nick, f'Player {nick} did not guess the word'.encode('utf-8'))
                time.sleep(5)
                disconnect(nick)
                break

        except:
            # remove, close, and send a message that the client is no more
            disconnect(nick)
            break


# main function
def receive_mess():
    while True:
        # accept connection from the client
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # get the nickname from the client
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients[nickname] = client

        # print the nickname on the server and broadcast the new client
        print(f'{nickname} connected to the server!')
        send_mess(nickname, f'\n{nickname} just joined the game!!\n'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # each client runs on 1 thread
        thread = threading.Thread(target=handle, args=(nickname,))
        thread.start()


print(f'{"*" * 5} Hangman the Game {"*" * 5}')
find_word()
receive_mess()

