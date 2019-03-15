#!/usr/bin/env python

import os
import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver

### Script for scrapping movie.com.uy site, it checks the list of available movies in the index site and sends an email if your favorite movie is published for buying a ticket on the best seat!
### Add it to a cron job if you wish to regularly check for you movie availability

### Navigation and scrapping implemented with BeautifulSoup and selenium for firefox usage

# If this script is running on a server without a screen, firefox needs one for running
# You can install xvfb: apt-get install xvfb
# Run xvfb in background: Xvfb :99 -ac & 
# Then set up "DISPLAY" environment variable with this value to be able to run firefox
os.environ['DISPLAY'] = ':99'

selectedMovie = "#YourFavoriteMovie"

url = "https://www.movie.com.uy/home"
driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

smtpServer = #Your SMTP server
smtpUser = #Your SMTP user
smtpPass = #Your SMTP pass
mailSubject = selectedMovie + " disponible!!!"
mailText = "Las entradas ya se encuentran disponibles en el sitio"
mailReceivers = ["#YourReceiver1", "#YourReceiver2"]

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

moviesList = soup.findAll("div", {"class": "input-group"})

if selectedMovie in str(moviesList):
   server = smtplib.SMTP(smtpServer, 25)
   server.starttls()
   server.login(smtpUser, smtpPass)
   msg = 'Subject: {}\n\n{}'.format(mailSubject, mailText)
   server.sendmail(smtpUser, mailReceivers, msg)
   server.quit()
