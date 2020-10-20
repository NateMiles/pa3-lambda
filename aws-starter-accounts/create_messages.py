#!/usr/bin/python3

import json
import boto3
import uuid
import random

QURL = 'YOUR_QUEUE_URL'
rand = random.randint(10,50)
sqs = boto3.client('sqs', region_name='us-east-1')

def lambda_handler():
  # randomizer() sends a variable # of messages per minute.
  randomizer()

def randomizer():
  for x in range(rand):
    send_message(str(rand))
  
def send_message(rand):
  value = str(uuid.uuid1())
  response = sqs.send_message(
    QueueUrl=QURL,
    MessageBody=value,
    MessageAttributes={
        'interval': {
            'StringValue': rand,
            'DataType': 'Number'
        }
    }
  )
  print(response)

lambda_handler()
