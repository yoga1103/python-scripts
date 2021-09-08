from bs4 import BeautifulSoup
import requests
import csv

#scrape a webpage for some date.

'''
Needed to scrape https://wptranslationday.org/htmlarchive/wptd-2019/the-local-events/ to get info of all the events that were organized in 2019.
The data to be scraped is Organizer's name, location, WordPress.org profile, making WordPress Slack profile
Beautifulsoup does the job
'''

BASE_URL = "https://wptranslationday.org/htmlarchive/wptd-2019/the-local-events/"
TITLES = [
    "area",
    "organizer",
    "WP Org Profile",
    "Slack Profile",
]

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, "html.parser")


#Open a csv file in append mode. This can be in write mode as well. 

with open("events.csv", "a", newline="") as ef:

    csv_writer = csv.writer(ef, delimiter=' ', quoting=csv.QUOTE_ALL)

    #Write the Titles array to the file
    csv_writer.writeheader()

    #find all the reeat divs by name 'local-event' 
    evs = soup.find_all("div", class_="local-event")

    #in the local-event, find the data needed for each of those local-events
    for ev in evs:

    	location = ev.find("div", class_="area")
    	org_name = ev.find("div", class_="organizer")
    	wp_profile, slack_profile = org_name.find_all('a')[0], org_name.find_all('a')[1] 

        #Format the data and write it to the csv file
    	csv_writer.writerow([location.text.strip(), org_name.text.strip(), wp_profile['href'], slack_profile['href']])

    #remember to close the file.
    ef.close()