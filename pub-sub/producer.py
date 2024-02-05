import pika
from pika.exchange_type import ExchangeType

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = 'Broadcast this message'

channel.basic_publish(exchange='pubsub', routing_key='key', body = message)

print('Message broadcasted')

connection.close()