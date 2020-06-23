#!/usr/bin/env python
# coding: utf-8

# In[135]:


def scrape():

    from bs4 import BeautifulSoup as bs      
    import requests
    from splinter import Browser
    import pandas as pd
    import re


    # In[30]:


    # scraping latest news


    # In[31]:


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


    # In[32]:


    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    # print(soup.prettify())


    # In[33]:


    results_title = soup.find('div', class_="content_title")


    # In[34]:


    # print(results_title)
    

    # In[73]:


    news_title = results_title.a.text.replace('\n', '')

    # news_title


    # In[36]:


    results_p = soup.find('div', class_='rollover_description_inner')
    # print(results_p)


    # In[75]:


    news_p = results_p.text.replace('\n', '')
    # news_p


    # In[38]:


    # Scraping featured image


    # In[117]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[118]:


    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)


    # In[119]:


    html = browser.html
    soup2 = bs(html, 'html.parser')
    # print(soup2.prettify())


    # In[120]:


    image = soup2.find('div').find('a', class_='button fancybox')['data-fancybox-href']


    # In[121]:


    featured_image_url = 'https://www.jpl.nasa.gov' + image


    # In[44]:

    browser.quit()


    #scraping weather


    # In[98]:


    url3 = 'https://twitter.com/marswxreport?lang=en'


    # In[127]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url3)


    # In[128]:


    twitter_html = browser.html
    soup3 = bs(twitter_html, 'html.parser')
    # print(soup3.prettify())


    # In[134]:


    mars_weather = soup3.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").find('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")


    # In[148]:


    char1 = '>'
    char2 = '</span>'
    mars_string = str(mars_weather)
    weather_on_mars = mars_string[mars_string.find(char1)+1 : mars_string.find(char2)]

    browser.quit()

    # In[49]:


    # scraping facts table


    # In[50]:


    url4 = 'https://space-facts.com/mars/'


    # In[51]:


    response_facts = requests.get(url4)
    soup_facts = bs(response_facts.text, 'html.parser')
    # print(soup_facts.prettify())


    # In[52]:


    table = soup_facts.find('table')
    # table


    # In[53]:


    df = pd.read_html(str(table))[0]
    #df


    mars_table = df.to_html(header=False)
    # print(mars_table)



    # scraping hemispheres


    hemisphere_image_urls = []


    # In[57]:


    url_hemi_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    url_hemi_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    url_hemi_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    url_hemi_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'


    # In[58]:


    response_hemi_1 = requests.get(url_hemi_1)
    soup_hemi_1 = bs(response_hemi_1.text, 'html.parser')
    # print(soup_hemi_1.prettify())


    # In[59]:


    hemi_1 = soup_hemi_1.find_all('a')[4]['href']
    # hemi_1


    # In[60]:


    hemisphere_image_urls.append({'title': 'Cerberus', 'image_url': hemi_1})


    # In[61]:


    response_hemi_2 = requests.get(url_hemi_2)
    soup_hemi_2 = bs(response_hemi_2.text, 'html.parser')
    #print(soup_hemi_2.prettify())
    hemi_2 = soup_hemi_2.find_all('a')[4]['href']
    # hemi_2


    # In[62]:


    hemisphere_image_urls.append({'title': 'Schiaparelli', 'image_url': hemi_2})


    # In[63]:


    response_hemi_3 = requests.get(url_hemi_3)
    soup_hemi_3 = bs(response_hemi_3.text, 'html.parser')
    #print(soup_hemi_3.prettify())
    hemi_3 = soup_hemi_3.find_all('a')[4]['href']
    # hemi_3


    # In[64]:


    hemisphere_image_urls.append({'title': 'Syrtis Major', 'image_url': hemi_3})


    # In[65]:


    response_hemi_4 = requests.get(url_hemi_4)
    soup_hemi_4 = bs(response_hemi_4.text, 'html.parser')
    #print(soup_hemi_4.prettify())
    hemi_4 = soup_hemi_4.find_all('a')[4]['href']
    # hemi_4


    # In[66]:


    hemisphere_image_urls.append({'title': 'Valles Marineris', 'image_url': hemi_4})


    # In[67]:


    # hemisphere_image_urls


    # In[146]:


    scraped_data = {}


    # In[149]:


    scraped_data['news_title'] = news_title
    scraped_data['news_headline'] = news_p
    scraped_data['featured_image'] = featured_image_url
    scraped_data['mars_weather'] = weather_on_mars
    scraped_data['facts_table'] = mars_table
    scraped_data['hemisphere_images'] = hemisphere_image_urls



    return scraped_data