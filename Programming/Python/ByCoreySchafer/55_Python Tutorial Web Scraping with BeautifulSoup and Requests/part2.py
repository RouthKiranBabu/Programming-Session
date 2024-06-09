from bs4 import BeautifulSoup
import requests

val = "https://github.com/RouthKiranBabu/Python-Reference"
source = requests.get(val).text
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
#Output
#[Running] python -u "c:\Users\kiran\OneDrive\Desktop\ScriptLearn\55_Python Tutorial Web Scraping with BeautifulSoup and Requests\part2.py"
#<!DOCTYPE html>
#<html data-a11y-animated-images="system" data-a11y-link-underlines="true" data-color-mode="auto" data-dark-theme="dark" data-light-theme="light" lang="en">
# <head>
#  <meta charset="utf-8"/>
#  <link href="https://github.githubassets.com" rel="dns-prefetch"/>
#  <link href="https://avatars.githubusercontent.com" rel="dns-prefetch"/>
#  <link href="https://github-cloud.s3.amazonaws.com" rel="dns-prefetch"/>
#  <link href="https://user-images.githubusercontent.com/" rel="dns-prefetch"/>

#title = soup.find('title')
#print(title.prettify())

#To get the titles
title = soup.find('title')
#print(title.prettify())
#Output
#<title>
# GitHub - RouthKiranBabu/Python-Reference: Provides Python Scripts for Learning or Revising
#</title>

headline = title.text 
#print(headline)
#Output
#GitHub - RouthKiranBabu/Python-Reference: Provides Python Scripts for Learning or Revising

link = soup.find("link")
#print(link.prettify())
#Output
#<link href="https://github.githubassets.com" rel="dns-prefetch"/>

#Example: p for paragraph and text to get the text
#summmary = article.find('div', class_ = 'entry-content').p.text

#For the youtube video
#<span class="embed-youtube" style="text-align:center; display:block;">
#<iframe allowfullscreen="true" class="youtube-player" height="390" 
#src="http://www.youtube.com/embed/K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent"
#Run the below program
#vid_src = article.find('iframe', class_ = "youtube-player")['src']
#Output
#http://www.youtube.com/embed/K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

#vid_id = vid_src.split('/')
#print(vid_id)
#Output
#['http:", '', 'www.youtube.com', 'embed', 'K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']
#vid_id = vid_src.split('/')[4]
#print(vid_id)
#Output
#K8L6KVGG-7o?version=3&amp;rel=1&amp;fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent
#vid_id = vid_id.split('?')
#print(vid_id)
#Output
#['K8L6KVGG-7o', 'version=3&amp;rel=1&amp;fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']
#vid_id = vid_id.split('?')[0]
#print(vid_id)
#Output
#'K8L6KVGG-7o'
#Youtube link
#yt_link = f"https://youtube.com/watch?v={vid_id}"
#print(yt_link)
#Output
#https://youtube.com/watch?v=K8L6KVGG-7o

#Example to get text and youtube link
#for article in soup.find_all('article'):
#    headline = article.h2.a.text
#    print(headline)
#    summary = article.find('div', class_ = 'entry-content').p.text
#    print(summary)
#    vid_src = article.find('iframe', class_ = "youtube-player")['src']
#    vid_id = vid_src.split('/')[4]
#    vid_id = vid_id.split('?')[0]
#    yt_link = f"https://youtube.com/watch?v={vid_id}"
#    print(yt_link)

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
        yt_link = None
    print(yt_link)