from confluent_kafka import Producer
import json
import random
import time

config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(config)

TOPICO = "novos_pedidos"

print("Iniciando envio de pedidos...\n")

for i in range(1, 6):

    pedido = {
        "pedido_id": i,
        "produto": f"Produto_{random.randint(1,100)}",
        "valor": round(random.uniform(10, 500), 2)
    }

    producer.produce(
        TOPICO,
        key=str(pedido["pedido_id"]),
        value=json.dumps(pedido)
    )

    producer.flush()

    print(f"Pedido enviado: {pedido}")

    time.sleep(1)

print("\n5 pedidos enviados com sucesso.")