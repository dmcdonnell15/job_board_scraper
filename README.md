# Personalize Job Board Scraper
Below are the steps to create a simple tool to scrape select job boards from commmonly-used job hosting sites to automatically send a personalized email of relevant postings

1) Job scraping script will hold the list of job sites you're interested in, the function to scrape the sites, and the function to send the email with the personalized job postings
2) This script gets uploaded as a [lambda function]([url](https://us-east-2.console.aws.amazon.com/lambda/home?ad=c&cp=bn&p=lbd&region=us-east-2#/functions))
3) virtual environment to create a layer to import python packages https://towardsdatascience.com/python-packages-in-aws-lambda-made-easy-8fbc78520e30
4) hosting lambda function in aws
5) scheduling amazon eventbridge to run function
