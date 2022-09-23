import socket
import argparse

BLOCK_LEN = 32
EOM = b"ENDOFMESSAGE___"


def read_message(connection) -> bytes:
    message = b''
    while len(message) < len(EOM) or message[-len(EOM):] != EOM:  # Обрабатываем условие нашего протокола.
        data = connection.recv(BLOCK_LEN)
        if not data:
            break
        message += data
    return message


def main(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
        clientsocket.connect((host, port))
        while True:
            message = input('> ').encode('utf8')
            message += EOM
            # Для отправки не обязательно разбивать сообщение на такие же чанки,
            # передача все равно будет согласованной.
            clientsocket.send(message)
            response = read_message(clientsocket).decode('utf8')
            print(response[:-len(EOM)])


def parse_cli_arguments():
    parser = argparse.ArgumentParser(description="Простой клиент")
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=9999)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_cli_arguments()
    main(host=args.host, port=args.port)
