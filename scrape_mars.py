#!/usr/bin/env python
# coding: utf-8

# In[23]:


#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time


# In[24]:


executable_path = {"executable_path":"C:\chromedriver_win32\chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)


# In[26]:


#visiting the page
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[28]:


#using bs to write it into html
html = browser.html
soup = bs(html,"html.parser")


# In[32]:


news_title = soup.find("div",class_="content_title").text
news_p = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"P: {news_paragraph}")


# In[33]:


paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)


# In[35]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg"
browser.visit(featured_image_url)


# In[38]:


#get mars weather's latest tweet from the website
mars_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather)


# In[40]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[41]:


mars_facts = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts)
table[0]


# In[45]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg": "..."},
    {"title": "Cerberus Hemisphere", "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg": "..."},
    {"title": "Schiaparelli Hemisphere", "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg": "..."},
    {"title": "Syrtis Major Hemisphere", "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg": "..."},
]


# In[ ]:




