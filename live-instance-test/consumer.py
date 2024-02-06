import pika
import time
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_URL=os.getenv('CLOUD_RABBITMQ_URL')

conn_params = pika.URLParameters(CONNECTION_URL)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

queue = 'test'

channel.queue_declare(queue=queue)

def on_message(ch, method, properties, body):
    time.sleep(2)
    print('New message recieve:', body)


channel.basic_consume(queue=queue,auto_ack=True, on_message_callback=on_message)


print('Strating to consume from', queue)

channel.start_consuming()