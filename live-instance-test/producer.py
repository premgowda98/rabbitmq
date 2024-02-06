import pika
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_URL=os.getenv('CLOUD_RABBITMQ_URL')

conn_params = pika.URLParameters(CONNECTION_URL)

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.queue_declare(queue='test')

channel.basic_publish(exchange='', routing_key='test', body="Hi Boss")

print("Message sent")

connection.close()

