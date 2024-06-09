#Saving in the csv file

from bs4 import BeautifulSoup
import requests
import csv

#Example shows how to use the code to get values and save it to the csv file
#You need to figure it out
val = "https://coreyms.com"
source = requests.get(val).text
soup = BeautifulSoup(source, 'lxml')

#Writing into the csv file
csv_file = open("cms_scrape.csv", 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_ = "youtube-player")['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except Exception as e:
        #raise e 
        #pass
        #Something to save
        yt_link = None
    print(yt_link)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

    