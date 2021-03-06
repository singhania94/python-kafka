from kafka import KafkaConsumer, KafkaProducer
import sys

consumer = KafkaConsumer(sys.argv[1], bootstrap_servers='localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092')


for msg in consumer:
    print(msg)
    s = str(msg).encode('UTF-8')
    producer.send('KAFKA_RESPONSE_TOPIC', key=msg.topic.encode('UTF-8'), value=msg.value)

