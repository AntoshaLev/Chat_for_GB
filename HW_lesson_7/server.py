import sys
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

from common.utils import check_port, receive_message, send_message, get_message
from common.variables import DEFAULT_API_ADDRESS, DEFAULT_PORT

import logging
import log.server_log_config
from common.errors import IncorrectPort

SERVER_LOG = logging.getLogger('server')


def gen_response(message):
    return {
        "response": 200,
        "alert": ""
    }


def read_request(rlist, clients):
    messages = {}
    for sock in rlist:
        try:
            messages[sock] = receive_message(sock)
            SERVER_LOG.info(get_message(messages[sock]))
        except:
            SERVER_LOG.info(f'{sock} отключился')
            clients.remove(sock)
    return messages


def write_messages(wlist, messages, clients):
    for sock in wlist:
        try:
            for s, message in messages.items():
                send_message(sock, gen_response(f'{s.getpeername()} отправил {message}'))
        except:
            SERVER_LOG.info(f'{sock} отключился')
            clients.remove(sock)


def main():
    addr = DEFAULT_API_ADDRESS
    port = DEFAULT_PORT
    if '-a' in argv:
        try:
            addr = argv[argv.index('-a') + 1]
        except IndexError:
            SERVER_LOG.error('после аргумента -a должен быть ip-адресс')
            raise ValueError('после аргумента -a должен быть ip-адресс')
    if '-p' in argv:
        try:
            port = check_port(argv[argv.index('-p') + 1])
        except IndexError:
            SERVER_LOG.error('после аргумента -p должен быть номер порта')
            raise ValueError('после аргумента -p должен быть номер порта')
        except IncorrectPort as e:
            SERVER_LOG.error(str(e))
            raise e

    socket_server = socket(family=AF_INET, type=SOCK_STREAM)
    try:
        socket_server.bind((addr, port))
    except OSError as e:
        SERVER_LOG.error(str(e))
        raise e

    socket_server.listen()
    while True:
        try:
            socket_client, address_client = socket_server.accept()
            SERVER_LOG.debug(f'подключение от {address_client}')
            message = receive_message(socket_client)
            SERVER_LOG.info(get_message(message))
            send_message(socket_client, gen_response(message))
        except(KeyboardInterrupt, OSError):
            socket_server.close()
            sys.exit()


if __name__ == '__main__':
    main()
