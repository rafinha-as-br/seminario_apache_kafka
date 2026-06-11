# Apache Kafka - Seminário

Projeto desenvolvido para demonstração prática do Apache Kafka na disciplina de Padrões de Projeto.

O objetivo é apresentar os conceitos fundamentais de mensageria assíncrona através de um exemplo simples de comunicação entre microsserviços utilizando Apache Kafka, Docker e Python.

---

## Arquitetura

O fluxo da aplicação funciona da seguinte forma:

```text
Producer (Pedidos)
        ↓
Apache Kafka (Broker)
        ↓
Consumer (Notificações)
```

### Componentes

* **Producer** (`producer.py`)

  * Simula um microsserviço de pedidos.
  * Publica eventos no tópico `novos_pedidos`.

* **Apache Kafka**

  * Recebe, armazena e distribui os eventos.
  * Atua como intermediário entre produtores e consumidores.

* **Consumer** (`consumer.py`)

  * Simula um microsserviço de notificações.
  * Consome os eventos publicados no Kafka.

---

## Tecnologias Utilizadas

* Apache Kafka
* Docker
* Docker Compose
* Python 3
* Confluent Kafka Python

---

## Estrutura do Projeto

```text
kafka-seminario/
│
├── docker-compose.yml
├── producer.py
├── consumer.py
├── requirements.txt
└── README.md
```

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir instalado:

* Docker Desktop
* Python 3.10 ou superior
* Pip

---

## Instalação das Dependências

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

---

## Inicializando o Kafka

Suba o container Kafka:

```bash
docker compose up -d
```

Verifique se o container está em execução:

```bash
docker ps
```

---

## Criando o Tópico

Acesse o container:

```bash
docker exec -it kafka bash
```

Crie o tópico utilizado pela demonstração:

```bash
/opt/kafka/bin/kafka-topics.sh \
--create \
--topic novos_pedidos \
--bootstrap-server localhost:9092
```

---

## Verificando os Tópicos

Para listar os tópicos existentes:

```bash
/opt/kafka/bin/kafka-topics.sh \
--list \
--bootstrap-server localhost:9092
```

Resultado esperado:

```text
novos_pedidos
```

---

## Executando a Demonstração

### 1. Inicie o consumidor

Abra um terminal e execute:

```bash
python consumer.py
```

Resultado esperado:

```text
Aguardando pedidos...
```

---

### 2. Execute o produtor

Abra outro terminal e execute:

```bash
python producer.py
```

Resultado esperado:

```text
Pedido enviado...
Pedido enviado...
Pedido enviado...
```

---

### 3. Observe o consumo das mensagens

No terminal do consumidor:

```text
[NOTIFICAÇÃO] Pedido #1 recebido
[NOTIFICAÇÃO] Pedido #2 recebido
[NOTIFICAÇÃO] Pedido #3 recebido
...
```

---

## Conceitos Demonstrados

Este projeto demonstra os seguintes conceitos do Apache Kafka:

* Producer
* Consumer
* Broker
* Topic
* Mensageria Assíncrona
* Comunicação entre Microsserviços
* Processamento de Eventos

---

## Encerrando o Ambiente

Para parar o Kafka:

```bash
docker compose down
```

Para remover volumes e recursos associados:

```bash
docker compose down -v
```

---

## Autores

* Rafael Antunes Souza
* Daniel Mariano Marques
* Hudson

Disciplina: Padrões de Projeto
