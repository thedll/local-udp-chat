# UDP Chat

Esse projeto é uma implementação de um chat baseado no modelo cliente-servidor que utiliza o protocolo UDP.<br>

<h2> Uso </h2>

1 - Inicialização do servidor na máquina local com a porta padrão utilizada pelo programa (1060):

```
└─$ python3 main.py servidor

                 _                    _    ____ _           _   
                | |    ___   ___ __ _| |  / ___| |__   __ _| |_ 
                | |   / _ \ / __/ _` | | | |   | '_ \ / _` | __|
                | |__| (_) | (_| (_| | | | |___| | | | (_| | |_ 
                |_____\___/ \___\__,_|_|  \____|_| |_|\__,_|\__|
                                                        
    
Escutando em ('127.0.0.1', 1060)
```

Ou com a porta de sua escolha:

```
└─$ python3 main.py servidor -p 44001   

                 _                    _    ____ _           _   
                | |    ___   ___ __ _| |  / ___| |__   __ _| |_ 
                | |   / _ \ / __/ _` | | | |   | '_ \ / _` | __|
                | |__| (_) | (_| (_| | | | |___| | | | (_| | |_ 
                |_____\___/ \___\__,_|_|  \____|_| |_|\__,_|\__|
                                                        
    
Escutando em ('127.0.0.1', 44001)
```

2 - Agora que o servidor está escutando, inicialize o cliente em outro terminal utilizando a mesma porta:

```
└─$ python3 main.py cliente          

                 _                    _    ____ _           _   
                | |    ___   ___ __ _| |  / ___| |__   __ _| |_ 
                | |   / _ \ / __/ _` | | | |   | '_ \ / _` | __|
                | |__| (_) | (_| (_| | | | |___| | | | (_| | |_ 
                |_____\___/ \___\__,_|_|  \____|_| |_|\__,_|\__|
                                                        
    
Mensagem: 
```

3 - Agora que a comunicação está estabelecida, a troca de mensagem pode ser feita. Para encerrar a conexão de ambos é necessário que o cliente envie 'sair'.
