import pika
from pika.exchange_type import ExchangeType

def on_message(ch, method, prop, body):
    print('Message recived on Payments service', body)

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='paymentsonly')
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message)

channel.start_consuming()