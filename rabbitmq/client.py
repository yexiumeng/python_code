#/usr/bin/env python36
import pika
import sys
import time
import signal

def signal_handler(signal,frame):
	print('exit')
	sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

username="guest"
pwd="guest"

user_pwd = pika.PlainCredentials(username,pwd)
s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=user_pwd))

channel = s_conn.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
	print("Received %r" %body)
	time.sleep(10)
	print("Done")
	ch.basic_ack(delivery_tag=method.delivery_tag)

#类似权重设置，如果消费者消费数量超过这个值，则服务端不会发新的消息过来
channel.basic_qos(prefetch_count=2)

channel.basic_consume(callback,queue='task_queue',)

channel.start_consuming()


