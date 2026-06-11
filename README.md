# Apache Kafka - Seminário
Repositório para o seminário sobre apache kafka, da disciplina de padrões de projeto

## Subir Kafka

docker compose up -d

## Entrar no container

docker exec -it kafka bash

## Criar tópico

/opt/kafka/bin/kafka-topics.sh \
--create \
--topic novos_pedidos \
--bootstrap-server localhost:9092

## Listar tópicos

/opt/kafka/bin/kafka-topics.sh \
--list \
--bootstrap-server localhost:9092

## Executar consumidor

python consumer.py

## Executar produtor

python producer.py