# Personalized Job Board Scraper
Below are the steps to create a simple tool to scrape select job boards from commmonly-used job hosting sites to automatically send a personalized email of relevant postings

1. Job scraping script will hold the list of job sites you're interested in, the function to scrape the sites, and the function to send the email with the personalized job postings
2. This script gets uploaded as a [lambda function](https://us-east-2.console.aws.amazon.com/lambda/home?ad=c&cp=bn&p=lbd&region=us-east-2#/functions)
    1. Open Lambda Console and create function using Python runtime
    2. Copy/paste your python script into the lambda_function.py window. Make sure import statements are above the lambda_function.
    3. To make your import statements work, add a layer to your lambda function. THis layer gets created in AWS Cloud9. You'll make a virtual environment to pip install your packages. See more [HERE](https://towardsdatascience.com/python-packages-in-aws-lambda-made-easy-8fbc78520e30)
    4. Once the proper layer gets added, you can deploy and test your lambda function to make sure it's working as desired.
3. Set up a schedule to send your emails via [Amazon EventBridge](https://us-east-2.console.aws.amazon.com/events/home?region=us-east-2#/). See more [HERE](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)
