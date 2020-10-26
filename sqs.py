import boto3
import csv
import time
client= boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/074482574465/pa3-queue'
response2 = client.get_queue_attributes(
    QueueUrl=queue_url,
    AttributeNames=[
        'All'
    ]
    )
num = response2.get('Attributes').get("ApproximateNumberOfMessages")
count=10 
while count>0 and int(num)>0:
    count-=1
    response = client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MessageAttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )
    for i in response.get('Messages'):
        with open('test.csv','a',newline='') as csvfile:
            response2 = client.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=[
                'All'
            ]
            )
            num = response2.get('Attributes').get("ApproximateNumberOfMessages")
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow([num, i.get('Body'), i.get('MessageAttributes').get('interval').get('StringValue'), time.strftime('%H:%M:%S %m/%d/%Y') ])
        print(client.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=i.get('ReceiptHandle')
    ))


