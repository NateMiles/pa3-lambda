# PA3 for AWS Starter Accounts

To launch the PA for AWS Starter Accounts:

1. STEP 2: Use an alternate stack in AWS CloudFormation and create a stack using this URL: 

    https://s3.amazonaws.com/cs4740-resources/templates/pa3-sqs-lambda-awsstarter.yml

2. Give the stack a name such as "pa3" and continue as per the PDF instructions and create your EC2 instance as directed. However, grant your IAM role FULL SQS permissions.
3. Steps 6-8: Instead of working with AWS Lambda, sudo su to become root and run your own `create_messages.py` script.
4. Copy the enclosed python script and paste it into a new file `/root/create_messages.py`. Be sure to customize line 6 with the value you got from Step 5.
5. Put the Python3 shebang line at the top of your script (something like `#!/usr/bin/python3`). `chmod` it to 755.
6. Following the same crontab directions in Step 17 in the PA instructions, put this script on a 1 minute cron schedule of its own.
7. Continue from Step 9 and you should see messages arriving in your queue.

That should get your `create_messages.py` script executed every 1 minute as AWS Lambda would have been doing for you.
