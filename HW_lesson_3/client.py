from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from common.utils import check_port, receive_message, send_message, print_message
from HW_lesson_4.variables import DEFAULT_PORT, DEFAULT_API_ADDRESS


def gen_presence_message(account):
    return {
        "action": "authenticate",
        "time": datetime.now().timestamp(),
        "user": {
            "account_name": f"{account}",
            "password": "CorrectHorseBatterStaple"
        }
    }


def check_response(message, expected_status):
    if message.get('response') == expected_status:
        return message
    raise Exception(f'server response {message}')


def main():
    addr = argv[1] if len(argv) > 2 else DEFAULT_API_ADDRESS
    port = check_port(argv[2]) if len(argv) > 2 else DEFAULT_PORT

    socket_client = socket(family=AF_INET, type=SOCK_STREAM)
    socket_client.connect((addr, port))
    send_message(socket_client, gen_presence_message('Vasya'))
    message = receive_message(socket_client)
    print_message(message)
    check_response(message, 200)
    socket_client.close()


if __name__ == '__main__':
    main()