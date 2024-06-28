import numpy as np
import pandas as pd

from confluent_kafka import Producer
import json

config = {
    'bootstrap.servers': 'localhost:9093',  # адрес Kafka сервера
    'client.id': 'simple-producer',
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.username': 'admin',
    'sasl.password': 'admin-secret'
}

producer = Producer(**config)

def connect_CH():

    from clickhouse_driver import Client

    try:
        client = Client(
            data["server"][0]["host"],
            user=data["server"][0]["user"],
            password=data["server"][0]["password"],
            verify=False,
            database="",
            settings={"numpy_columns": True, "use_numpy": True},
            compression=True,
        )
    except Exception as e:
        print(e, "No connection")

    return client
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def send_message(data):
    try:
        producer.produce('topic_click', data.encode('utf-8'), callback=delivery_report)
        producer.poll(0)
    except BufferError:
        print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): try again")

def get_data_from_ch():

    client = connect_CH()

    data = client.execute('select place_name, place_cod from dict_StoragePlace limit 100')

    res = []

    for i in range(len(data)):
        result = data[i]
        pp = pd.DataFrame([result], columns=["place_name", "place_cod"])
        res.append(pp.to_json(orient="records")[1:-1])

    return res

if __name__ == '__main__':
    data_from_ch = get_data_from_ch()
    for row in data_from_ch:
        send_message(row)
    producer.flush()