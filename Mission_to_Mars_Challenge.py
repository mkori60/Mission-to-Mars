#!/usr/bin/env python
# coding: utf-8

# In[1906]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[1907]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[1908]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[1909]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[1910]:


slide_elem.find('div', class_='content_title')


# In[1911]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[1912]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# In[1913]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[1914]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[1915]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[1916]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[1917]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[1918]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[1919]:


df.to_html()


# In[1920]:


browser.quit()


# In[1921]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[1922]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[1923]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[1924]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[1925]:


slide_elem.find('div', class_='content_title')


# In[1926]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[1927]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[1928]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[1929]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[1930]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[1931]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[1932]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[1933]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[1934]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[1935]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[1936]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
hemisphere_image_urls = []

for i in range(4):
    # Create empty dictionary 
    hemispheres = {}
    
    # Find titles 
    img_titles = browser.find_by_css('a.itemLink h3')[i].text
    hemispheres['title'] = img_titles
    
    # Click to next page 
    browser.find_by_css('a.itemLink h3')[i].click()
    
    # Find Urls
    img_url = browser.find_by_css('img.wide-image')['src']
    hemispheres["img_url"] = img_url
    
    # Return to previous page 
    browser.back()
    
    # Add info to dictionary 
    hemisphere_image_urls.append(hemispheres)
    
hemisphere_image_urls    


# In[1937]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




