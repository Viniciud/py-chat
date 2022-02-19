import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

nickname = input('Choose your nickname in this chat: ')


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if (message == 'NICK'):
                client.send(nickname.encode('ascii'))
            else:
                if not (nickname in message):
                    print(message)
        except:
            print('An error occurred!')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}:  {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
