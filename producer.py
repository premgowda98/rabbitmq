import pika

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "Hello this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print("Message sent")

connection.close()

