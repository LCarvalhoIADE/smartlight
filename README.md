# SmartLight AI

Licenciatura em Engenharia Informática · IADE · Universidade Europeia · 2026/2027

Projeto PBL do 5.º semestre, grupo g04.

Autores: Diego Silva, Francisco Maia, Luís Carvalho e Ricardo Siqueira

Unidades curriculares:
- Sistemas Distribuídos (Pedro Rosa)
- Computação Física e IoT (Alexandre Pereira)
- Engenharia de Software (Carla Pereira)
- Inteligência Artificial (João Monge)

## Objetivo

O SmartLight AI é um projeto de iluminação inteligente para casa. Pretendemos desenvolver um sistema que:

- deteta presença e mede a luz ambiente através de nós ESP32, instalados em divisões de várias casas;
- acende a luz quando é necessária e ajusta a intensidade em função da luz natural, através de PWM, mesmo sem ligação à rede;
- mede o consumo da iluminação num nó de referência e estima o consumo nos restantes;
- envia as leituras por REST, sobre HTTPS, para um servidor com uma base de dados MySQL;
- usa IA para prever o consumo da iluminação;
- permite consultar o estado da iluminação, o histórico, as previsões e os alertas num dashboard web.

## Arquitetura

![Arquitetura](Documentacao/1aEntrega/img/arquitetura.png)

O controlo da iluminação é feito no próprio nó, sem depender do Wi-Fi ou do servidor. Quando não há ligação à Internet, as leituras ficam guardadas no nó e são enviadas quando a ligação é restabelecida.

O dashboard consulta os dados através da API. Para gerar previsões de consumo, o módulo de IA irá combinar as leituras dos nós com dados meteorológicos da Open-Meteo.

## Tecnologias previstas

- Nós: ESP32 e ESP32-S3, programados em C++ com PlatformIO ou Arduino IDE
- Comunicação: REST sobre HTTPS, com dados em JSON
- Servidor: PHP 8 e MySQL, em Docker
- IA: Python, com pandas e scikit-learn

## Estrutura do repositório

## Documentação
