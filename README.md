# Licenciatura de Engenharia Informática - IADE - 2026/2027
 ---------------------------------------------------------------------------
- **Projeto:** PBL (Projeto Grupo 4)

| UC | Professor
|---|---|---|
| Sistemas Distribuídos | Pedro Rosa | Gestão do projeto, arquitetura e infraestrutura |
| Computação Física e IoT | Alexandre Pereira | Firmware ESP32, sensores, atuador e envio REST |
| Engenharia de Software | Carla Pereira | Requisitos, modelação, plano e validação de testes |
| Inteligência Artificial | João Monge | Modelo preditivo de consumo energético |

- **Autores:** Diego Silva | Francisco Maia | Luis Carvalho | Ricardo Siqueira

# SmartLight AI

Projeto académico do 5º semestre de Engenharia Informática.

## Objetivo

Desenvolver um sistema inteligente de iluminação residencial que:

- deteta presença e mede a luz ambiente com um **ESP32**;
- ajusta o brilho da iluminação por **PWM**, evitando desperdício;
- envia as leituras por **REST** para um servidor que as guarda em **MySQL**;
- usa **IA** para prever o consumo energético;
- mostra tudo num **dashboard web**.

## Funcionalidades previstas

- Deteção de presença
- Medição da luminosidade ambiente
- Controlo automático de iluminação por PWM
- Estimativa de consumo energético
- Monitorização através de dashboard
- Previsão de consumo com Inteligência Artificial

## Arquitetura

ESP32 → REST → Backend → Base de Dados

O dashboard consulta o backend.
A IA utiliza dados históricos para gerar previsões.

## Tecnologias previstas

- ESP32 / C++ / PlatformIO
- MQTT / Mosquitto
- REST
- Python / FastAPI
- SQL
- pandas
- scikit-learn
- Dashboard Web

## Datas de entregas

| Data | Entrega |
|---|---|
| 27-10-2026 | Proposta inicial - (SD, IoT)|
| 13-11-2026 | Especificação de requisitos (ES) |
| 30-11-2026 | Protótipo (SD) |
| 15-01-2027 | Plano e validação de testes (ES) |
| 29-01-2027 | Modelo preditivo (IA) |
| 01-02-2027 | Entrega final e apresentação |


## Estado

Projeto em fase de planeamento e preparação
do ambiente de desenvolvimento.
