import pika
from pika.exchange_type import ExchangeType

conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()


channel.exchange_declare(exchange='topic_exchange', exchange_type=ExchangeType.direct)

message = 'Routing messages'

channel.basic_publish(exchange='topic_exchange', routing_key='user.india.analytics', body = message)

print('Message broadcasted')

connection.close()