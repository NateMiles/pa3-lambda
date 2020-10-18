import json
import boto3
import uuid
import random

UVA_ID = 'YOUR_UVA_ID'
QURL = 'YOUR_QUEUE_URL'
rand = random.randint(10,50)
sqs = boto3.client('sqs')

def lambda_handler(event, context):
  # randomizer() sends a variable # of messages per minute.
  # Leave this running the entire time.
  randomizer()

  # Uncomment process_messages() when you are ready to test your function
  # at scale
  #
  # process_messages() is the function you are to complete, following all 
  # requirements in the PA instructions.
  # process_messages()

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

def process_messages():
  """ [YOU MAY DELETE THIS COMMENT]
  This function MUST perform the following tasks:
    1. Fetch the ApproximateNumberOfMessages for your queue using the get_queue_attributes()
       method of the sqs client. Save that number as a variable.
    2. Read as many messages as possible each time the function is executed, extracting the 
       value of the MessageBody and the value of the "interval" custom MessageAttribute, 
       storing as vars for each message. These are found by using the receive_message method.
       Remember there may be ways to receive more than one message at a time.
    3. Using the fields you collect, print() out the values of these three values, in comma-
       separated form. The values should be as follows, in this order:
           a) ApproximateNumberOfMessages (a number)
           b) MessageBody (a UUID string)
           c) Interval (a custom MessageAttribute, a number)
       These printed values will be recorded to CloudWatch logs.
    4. Delete messages once they have been parsed. boto3 may have more than one method for
       message deletion. Consult the documentation.
    5. Create sub-functions as needed. Work on your local workstation to dev and test your
       code.
    6. Once your code achieves those goals, check the number of messages in your queue.
       If it is far above 1000, purge the queue and wait for it to get to 1000 again.
    7. Then uncomment lines 21 to enable your function.
       Remember to observe the pace of new messages flowing into the queue. One of the 
       priorities of your function is that it not only keep up with this pace, but steadily
       catch up to it, so that your queue depth is reduced to almost nothing.
  """
  print('')
