from kafka import KafkaProducer
bootstrap_servers = ['localhost:9092']
topicName = 'my-topic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

ack = producer.send(topicName, b'Hello World!')
metadata = ack.get()
print("topic: ",metadata.topic)
print("Partition: ",metadata.partition)