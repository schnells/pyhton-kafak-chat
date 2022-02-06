from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['chatroom1']

def writeChatMessage(sender, message):
    with topic.get_producer(delivery_reports=True) as producer:
        producer.produce(bytes(message, encoding='utf8'), partition_key=bytes(sender, encoding='utf8'))

writeChatMessage("testuser", "hello world")