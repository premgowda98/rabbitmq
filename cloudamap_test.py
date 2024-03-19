import pika
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_URL=os.getenv('CLOUD_RABBITMQ_EXAM_URL')

conn_params = pika.URLParameters(CONNECTION_URL)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

exchange_key = 'exchange.bb214c60-fe8d-4084-9c5a-4b6642c10afe'
routing_key = 'bb214c60-fe8d-4084-9c5a-4b6642c10afe'
queue_name = 'exam'

channel.exchange_declare(exchange_key)
queue = channel.queue_declare(queue_name, durable=True)

channel.queue_bind(exchange=exchange_key, queue=queue.method.queue, routing_key=routing_key)

properties = pika.BasicProperties(delivery_mode=2)

channel.basic_publish(exchange=exchange_key, 
                        routing_key=routing_key,
                        body='Hi CloudAMQP, this was fun!',
                        properties=properties
                        )

channel.queue_delete(queue=queue_name)
channel.exchange_delete(exchange=exchange_key)
connection.close()



