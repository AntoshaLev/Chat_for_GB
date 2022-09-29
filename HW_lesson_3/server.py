from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from HW_lesson_4.utils import check_port, receive_message, send_message, print_message
from HW_lesson_4.variables import DEFAULT_API_ADDRESS, DEFAULT_PORT


def gen_response(message):
    return {
        "response": 200,
        "alert": ""
    }


def main():
    addr = DEFAULT_API_ADDRESS
    port = DEFAULT_PORT
    if '-a' in argv:
        try:
            addr = argv[argv.index('-a') + 1]
        except IndexError:
            raise ValueError('после аргумента -a должен быть ip-адресс')
    if '-p' in argv:
        try:
            port = check_port(argv[argv.index('-p') + 1])
        except IndexError:
            raise ValueError('после аргумента -p должен быть номер порта')

    socket_server = socket(family=AF_INET, type=SOCK_STREAM)
    socket_server.bind((addr, port))
    socket_server.listen()

    socket_client, address_client = socket_server.accept()
    message = receive_message(socket_client)
    print_message(message)
    send_message(socket_client, gen_response(message))
    socket_server.close()
    socket_client.close()


if __name__ == '__main__':
    main()