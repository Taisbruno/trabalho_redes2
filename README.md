# Trabalho de Redes de Computadores 2 para Sistemas de Informação
# Jogo com conexão Cliente Servidor

![Imagem](logo.jpg)

**Jogo no estilo "Pedra, Papel e Tesoura" com conexão Cliente Servidor.**

- Como proposto pela disciplina de "Redes de Computadores 2 para Sistemas de Informação", desenvolvemos um Jogo no estilo
"Pedra, Papel e Tesoura" com uma conexão Cliente Servidor. Para isso, foi necessário conhecimento sobre Threads, Socket,
Pygame, Orientação a Objetos, Biblioteca Pickle, etc, para prosseguir com a implementação do projeto.

## Pré-requisitos de instalação:
- Git instalado na máquina.
- Python instalado na máquina.
- Instalar a biblioteca "Pygame" através do comando "pip install pygame".
- Alguma IDLE instalada na máquina, que execute códigos em Python. Sugestão: VSCode.
- Servidor Linode configurado, de preferência com uma imagem Ubuntu na última versão. https://www.linode.com/pt/
- Software WinSCP instalado, ou Filezilla para realizar a transferência dos arquivos para o Servidor. https://winscp.net/eng/index.php
- Software PuTTY instalado para emular o terminal e se conectar ao Servidor Linode. https://www.putty.org/

## Instruções para execução da demonstração:

- Usar o comando "git clone..." para clonar o repositório e ter acesso ao código na sua máquina.

- Ter o Servidor Linode configurado e rodando, de preferência com uma imagem Ubuntu. Esse servidor já vem com o Python instalado dentro dele.

- Instalar o software PuTTY para acessar o servidor remotamanete por meio de um terminal emulado. Para acessar, é necessária a inserção do endereço IPv4 do servidor, assim como a senha de acesso do mesmo. Dentro do software PuTTY, inserir o endereço IP citado, porta 22, conexão do tipo SSH, e clicar em "Open". No terminal, realizar login com o usuário: root. A senha será a configurada para acessar o Servidor Linode previamente. 
 - Aplicar os comandos:
 1. "cd .."
 2. "ls"
 3. "cd root"
 4. "mkdir trabredes"
 5. "cd trabredes"
Os comandos acima são importantes para navegar pelo terminal e criar a pasta para qual o arquivo server.py será transferido posteriormente.

- Instalar o Software WinSCP para se conectar ao servidor por meio do endereço IPv4 do mesmo e de sua senha de acesso(configurada durante a configuração do Servidor Linode). Dentro do software WinSCP, inserir o endereço IP citado, porta 22, protocolo de transferência de arquivo SFTP, Username: root, inserir a senha de acesso do servidor, e clicar em "Login". Entrar na pasta "trabredes" criada, copiar o arquivo Server_.py e o arquivo Game_.py para dentro do servidor.

- Voltar ao PuTTY, e dentro da pasta chamada "trabredes", executar o arquivo server_py com o uso do comando: python3 server_.py. 

- Abrir a IDLE escolhida que contem os códigos clonados do repositório, e executar apenas o arquivo client.py no modo DEBUG. Esse arquivo client.py deverá ser executado pelo menos duas vezes para que uma conexão possa ser estabalecida entre duas instâncias da aplicação.

- Para que uma conexão possa ser estabelecida de fato, é necessário não apenas executar os clients, como também dentro da tela do Client, clicar na tela de "Clique para jogar!". Quando duas instâncias de client estiverem conectadas entre si, será possível ver, pelo terminal, que ambas estão conectadas, assim como o endereço IPv4 de localização da máquina em que esses clients foram abertos.

- Com dois clients conectados na mesma partida, testar o jogo para esses dois players. Selecionar alguma opção de botão(Pedra, Papel ou Tesoura) para o primeiro client e em seguida escolher uma segunda opção de botão para o segundo client. Assim que ambos os players já tiverem escolhido uma opção, será exibida na tela o resultado final sobre qual player ganhou aquela rodada e qual player perdeu. Os movimentos são automaticamente resetados em seguida para que uma próxima rodada entre esses players possa acontecer. 

- Após testar o funcionamento do jogo, fechar os dois clients, matar os terminais abertos pela IDLE no modo DEBUG, e abrir o terminal emulado para visualizar a conexão perdida ao fechar um dos clients e o fechamento da conexão entre os clients em seguida.

## Autoria e contribuições:

#### Autoria: 
Juliana Scapim,
Tais Bruno Rabelo,
Thales Fonseca

#### Contribuições: 
- https://www.pygame.org/docs/
- http://www.linhadecodigo.com.br/artigo/503/introducao-ao-pygame.aspx
- https://docs.python.org/3/library/pickle.html
- https://realpython.com/python-rock-paper-scissors/
- https://realpython.com/pygame-a-primer/
- https://medium.com/analytics-vidhya/basics-for-network-communication-on-python-af3f677af42c
- https://wiki.python.org/moin/UsingPickle
- https://levelup.gitconnected.com/program-your-first-multiple-user-network-game-in-python-9f4cc3650de2
- https://www.geeksforgeeks.org/8-bit-game-using-pygame/
- https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
- https://inventwithpython.com/makinggames.pdf
- https://codingshiksha.com/python/python-3-pygame-rock-paper-scissors-game-script-using-random-module-gui-desktop-app-full-project-for-beginners/
- StackOverflow

#### Slides:
- [Slide](https://docs.google.com/presentation/d/1ledoMvHJP1VEG5ob6n5uI0QZWT0OJiZBL7NjWiVAGyI/edit#slide=id.g110ad1f8954_0_6)