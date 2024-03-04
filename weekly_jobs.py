import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import tabulate
import time 
# List of company job board URLs 

# Greenhouse
greenhouse_job_boards = [
    "https://boards.greenhouse.io/questbridge",
    "https://boards.greenhouse.io/coursera",
    "https://boards.greenhouse.io/outschool",
    "https://boards.greenhouse.io/articulate",
    "https://boards.greenhouse.io/equilibriumenergy",
    "https://boards.greenhouse.io/antora",
    "https://boards.greenhouse.io/amperon",
    "https://boards.greenhouse.io/pluspower",
    "https://boards.greenhouse.io/spanio",
    # Add more job board URLs here
]

# Breezy HR
breezy_job_boards = [
    "https://everydaylabs.breezy.hr",
    "https://sown-to-grow.breezy.hr",
    "https://edquity.breezy.hr/"
    # Add more job board URLs here
]

# Lever
lever_job_boards = [
    "https://jobs.lever.co/indigoag",
    "https://jobs.lever.co/stradaeducation",
    "https://jobs.lever.co/gridmatic",
    "https://jobs.lever.co/stable",
    "https://jobs.lever.co/qcells",
    "https://jobs.lever.co/yardstick"
    # Add more job board URLs here
]

# Random
random_job_boards = [
    "https://www.flyzipline.com/careers",
    # Add more job board URLs here
]

# Greenhouse boards
def greenhouse_jobs(url_list):
    job_listings_all = []
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        job_listings = soup.find_all("div", class_="opening")
        total_postings = str(len(job_listings)) + " postings searched"
        for job_listing in job_listings:
            posting_title = (job_listing.find("a").text.strip())
            if "Data" in posting_title:
                posting_link = f"https://boards.greenhouse.io{job_listing.find('a')['href']}"
                job_listings_all.append({
                    'job_board': url,
                    'name': posting_title,
                    'url': posting_link,
                    'total_postings': total_postings
                })
        job_listings_all.append({
            'job_board': url,
            'name': "No more data positions available",
            'url': "No more data positions available",
            'total_postings': total_postings
        })      
    return job_listings_all
  
# Breezy HR boards
def breezy_jobs(url_list):
    job_listings_all = []
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('li', class_='position transition')
        total_postings = str(len(job_listings)) + " postings searched"
        for job_listing in job_listings:
            posting_title = job_listing.find('h2').text.strip()
            if "Data" in posting_title:
                posting_link = f"{url}{job_listing.find('a')['href']}"
                job_listings_all.append({
                    'job_board': url,
                    'name': posting_title,
                    'url': posting_link,
                    'total_postings': total_postings
                })
        job_listings_all.append({
            'job_board': url,
            'name': "No more data positions available",
            'url': "No more data positions available",
            'total_postings': total_postings
        })      
    return job_listings_all

# Lever boards
def lever_jobs(url_list):
    job_listings_all = []
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_ = 'posting')
        total_postings = str(len(job_listings)) + " postings searched"
        for job_listing in job_listings:
            posting_title = job_listing.find('h5').text.strip()
            if "Data" in posting_title:
                posting_link = f"{job_listing.find('a')['href']}"
                job_listings_all.append({
                    'job_board': url,
                    'name': posting_title,
                    'url': posting_link,
                    'total_postings': total_postings
                })
        job_listings_all.append({
            'job_board': url,
            'name': "No more data positions available",
            'url': "No more data positions available",
            'total_postings': total_postings
        })      
    return job_listings_all

# Append all jobs to one list
jobs = {}
jobs = greenhouse_jobs(greenhouse_job_boards) + breezy_jobs(breezy_job_boards) + lever_jobs(lever_job_boards)

# Function to send an email with the job listings
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

subject = "Jobs Report"
body = tabulate.tabulate(jobs, tablefmt='simple', headers='keys')  
sender = "email@email.com"
recipients = ["email@email.com"]
password = "password"

send_email(subject, body, sender, recipients, password)
