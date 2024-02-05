import pika
from pika.exchange_type import ExchangeType

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()


channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = 'Routing messages'

channel.basic_publish(exchange='routing', routing_key='both', body = message)

print('Message broadcasted')

connection.close()