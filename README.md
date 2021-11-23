# GUIPsyin: Interface Gráfica de Interação Psicológica Infantil

Desenvolvido por Diogo Henrique Godoi

#### Objetivo
O objetivo deste projeto é desenvolver uma interface para a manipulação do Robô NAO.

## Manual de Utilização

#### Informações Gerais
Essa interface foi desenvolvida com o intuito de simplificar a manipulação do robô humanóide NAO. Este será utilizado em sessões de terapia  com crianças.
O método que será utilizado nas sessões de terapia  é chamado de Mágico de OZ. Este método consiste em 3 agentes: usuário (criança), mágico (assistente) e OZ(NAO). 
Esse método consiste fazer com que o usuário acredite que esteja interagindo com uma entidade inteligente, nesse casa o NAO, no entanto tal entidade é controlada pelo mágico,
ou seja pelo assistente (psicólogo).

obs: É necessário ter o python 2.7.18 instalado em seu computador para a utilização da interface.
#### Bibliotecas necessárias
Para utilizar a interface é necessário ter o Naoqi 2.1.4.13 e o PyQt4 instalado em um ambiente virtual em seu computador.

Acesse: https://docs.python.org/pt-br/3/library/venv.html para criar um ambiente virtual.

Acesse: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4 para download do PyQt4.

Para a instalação das outras bibliotecas utilize pip install requeriments.txt

#### Módulos da Interface

A interface GUIPsyin é responsável pela comunicação do computador com o robô NAO. Primeiro é necessário obter-se o IP do robô NAO, esse IP pode ser adquirido pressionando-se o botão no meio do peito do robô NAO.

![alt text](https://github.com/diogodoi/proteger/blob/main/Guipsyn.png "GUIPsyin")

Figura 1: Interface GUIPsyin, em 1) Configurações , 2) Sessão,3) Movimentos, 4) Botão de emergência, 5) Área de Avisos.

ATENÇÃO: qualquer procedimento que necessite ligar ou operar o robô NAO, deve ser feito de preferência por pessoas habilitadas para isso,  com muito cuidado e máxima atenção pois, o robô não é um brinquedo, pode eventualmente causar lesões superficiais na pele, através de suas partes móveis e movimentos ou pode ser danificado permanentemente, por ocasião de eventuais quedas. O robô não deve ser operado por crianças.

1. Configurações: no espaço em branco na frente de IP Robô coloque o IP do robô NAO, esse IP é obtido quando você pressiona o botão localizado no peito do robô.Após isso pressione em Conectar, o botão irá ficar verde se a conexão estabelecida, caso não seja, verifique a aba de avisos. Assim que a conexão for estabelecida, pressione o botão” Câmera NAO” para abrir uma janela que transmite o vídeo da câmera localizada na testa do NÃO. Quando quiser encerrar a conexão com o robô pressione o botão “Desconectar”.  Antes de iniciar esta conexão o computador e o NAO devem estar conectados na mesma rede wifi.

2. Sessão:  Para iniciar a sessão pressione o botão “Iniciar Vida”, este botão faz o robô NAO, ativar o detector de face, além de fazer o robo levantar e ficar pronto para a fazer os movimentos pré-programados. O botão “Encerrar Vida”, coloca o robo NAO em modo standby, ou seja, ele irá sentar, e todos os leds irão desligar, além do sistema de detecção de face. Utilize este botão para nos intervalos da sessão, assim você não irá precisar reconectar o robô toda vez que iniciar uma sessão.

3. Botão EMERGÊNCIA: Esse botão desliga o robô instantaneamente, utilize somente em caso de EMERGÊNCIA, pois pode danificar o robô NAO.

4. Movimentos: Aqui encontram-se os movimentos desenvolvidos para a interação

5. Avisos: Aqui são dadas as mensagens de erros, avisos e alertas.	



