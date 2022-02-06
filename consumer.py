from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['chatroom1']

consumer = topic.get_simple_consumer(consumer_group="mychat")
for message in consumer:
    if message is not None:
        print(message.value)

