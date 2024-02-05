import pika
import time
conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

for i in range(5):
    time.sleep(2)

    message = f"Message {i}"

    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print("Message sent")

connection.close()

