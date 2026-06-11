from confluent_kafka import Consumer
import json

config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "grupo-notificadores",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(config)

consumer.subscribe(["novos_pedidos"])

print("Aguardando pedidos...\n")

try:

    while True:

        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            continue

        pedido = json.loads(
            msg.value().decode("utf-8")
        )

        print(
            f"[NOTIFICAÇÃO] Pedido #{pedido['pedido_id']} "
            f"recebido | Produto: {pedido['produto']} "
            f"| Valor: R$ {pedido['valor']}"
        )

except KeyboardInterrupt:
    print("\nEncerrando consumidor...")

finally:
    consumer.close()