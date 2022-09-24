import chat
import jim

client_name = ''

if __name__ == '__main__':
    parser = chat.create_parser()
    namespace = parser.parse_args()

    sock = chat.get_server_socket(namespace.addr, namespace.port)

    serv_addr = sock.getsockname()
    print(f'Server started at {serv_addr[0]}:{serv_addr[1]}')

    client, address = sock.accept()
    print(f'Client connected from {address[0]}:{address[1]}')

    while True:
        data = chat.get_data(client)

        if client_name == '':
            if data['action'] == 'presence' and data['user']['account_name'] != '':
                client_name = data['user']['account_name']
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[0]
                print(f'{data["time"]} - {data["user"]["account_name"]}: {data["user"]["status"]}')
            else:
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[1]

        if client_name != '' and data['action'] == 'msg':
            print(f'{data["time"]} - {client_name}: {data["message"]}')
            jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[0]

            if data["message"] == 'exit':
                jim.RESPONSE['response'], jim.RESPONSE['alert'] = jim.SERV_RESP[2]

        chat.send_data(client, jim.RESPONSE)

        if jim.RESPONSE['response'] != '200':
            client.close()
            break

    sock.close()