import socket, argparse

MAX_BYTES = 65535

def figlet():
    print('''
                 _                    _    ____ _           _   
                | |    ___   ___ __ _| |  / ___| |__   __ _| |_ 
                | |   / _ \ / __/ _` | | | |   | '_ \ / _` | __|
                | |__| (_) | (_| (_| | | | |___| | | | (_| | |_ 
                |_____\___/ \___\__,_|_|  \____|_| |_|\__,_|\__|
                                                        
    ''')

def servidor(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', porta))
    figlet()
    print('Escutando em {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        texto = data.decode('utf-8')
        if texto == 'sair':
            break
        print('Cliente: {}'.format(texto))
        texto = input('Mensagem: ')
        data = texto.encode('utf-8')
        sock.sendto(data, address)

def cliente(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    figlet()
    while True:
        texto = input("Mensagem: ")
        data = texto.encode('utf-8')
        sock.sendto(data, ('localhost', porta))
        if texto == 'sair':
            break
        data = sock.recv(MAX_BYTES)
        texto = data.decode('utf-8')
        print('Servidor: {}'.format(texto))

if __name__ == '__main__':
    escolhas = {'servidor': servidor, 'cliente': cliente}
    parser = argparse.ArgumentParser(description='Enviar e receber UDP localmente')
    parser.add_argument('posicao', choices=escolhas, help='cliente ou servidor')
    parser.add_argument('-p', metavar='PORTA', type=int, default=1060, help='Porta UDP (default 1060)')
    args = parser.parse_args()
    function = escolhas[args.posicao]
    function(args.p)

        
    


