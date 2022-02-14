from confluent_kafka import Consumer
import socket

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': socket.gethostname(),
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)


consumer.subscribe(["chatroom1"])
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.key().decode('utf-8') + ":" + msg.value().decode('utf-8')))

consumer.close()


