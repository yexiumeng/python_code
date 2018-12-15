#/usr/bin/env python36
import pika
import sys
import socket
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

channel.queue_declare(queue='task_queue', durable=True) #durable是持久化队列


while True:
	mes = input("input your mes:")
	channel.basic_publish(exchange='',routing_key='task_queue',body=mes,properties=pika.BasicProperties(delivery_mode=2,)) #properties中的delivery_mode=2是为了持久化消息
	print("the mes is %s" %mes)
