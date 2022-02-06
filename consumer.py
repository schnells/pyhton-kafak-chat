from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['chatroom1']

consumer = topic.get_simple_consumer(consumer_group="mychat",
    auto_offset_reset=OffsetType.EARLIEST,
    reset_offset_on_start=False)
for message in consumer:
    if message is not None:
        print(message.value)

