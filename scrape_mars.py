#!/usr/bin/env python
# coding: utf-8


from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# # NASA Mars News

#open Chromedriver
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


#change the url to the site I want to visit
url = "https://mars.nasa.gov/news/"
browser.visit(url)

#set html and soup
html = browser.html
soup = bs(html, "html.parser")
time.sleep(30)
#inspect the site to find what I want to scrape
news_title= soup.find('li',class_='slide').find('div',class_='content_title').text

news_title



#inspect the site to find what I want to scrape
news_p= soup.find('li',class_='slide').find('div',class_='article_teaser_body').text

news_p


# # NJPL Mars Space Images



#open Chromedriver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=True)


#change the url to the site I want to visit
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


#set html and soup
html = browser.html
soup = bs(html, "html.parser")



#browser.links.find_by_partial_text('FULL IMAGE')
image = browser.find_by_id('full_image')
image.click()


image2 = browser.find_link_by_partial_text('more info')
image2.click()



#inspect the site to find what I want to scrape
image3= soup.find('div',class_='grid_layout')
#.find('img',class_='fancybox-image')



html = browser.html
soup = bs(html, "html.parser")

image4 = soup.select_one("figure.lede a img").get("src")
print(image4)



featured_image_url = f"https://www.jpl.nasa.gov{image4}"



featured_image_url


# # Mars Facts


#open Chromedriver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=True)


#change the url to the site I want to visit
url = "https://space-facts.com/mars/"
browser.visit(url)



#set html and soup
html = browser.html
soup = bs(html, "html.parser")


equator= soup.find('tr',class_='row-1 odd').find('td',class_='column-1').text



print(equator)



equator2= soup.find('tr',class_='row-1 odd').find('td',class_='column-2').text



print(equator2)



polar= soup.find('tr',class_='row-2 even').find('td',class_='column-1').text
polar2= soup.find('tr',class_='row-2 even').find('td',class_='column-2').text



polar



polar2



mass= soup.find('tr',class_='row-3 odd').find('td',class_='column-1').text
mass2= soup.find('tr',class_='row-3 odd').find('td',class_='column-2').text



mass



mass2



moon= soup.find('tr',class_='row-4 even').find('td',class_='column-1').text
moon2= soup.find('tr',class_='row-4 even').find('td',class_='column-2').text



moon


moon2



orbitd= soup.find('tr',class_='row-5 odd').find('td',class_='column-1').text
orbitd2= soup.find('tr',class_='row-5 odd').find('td',class_='column-2').text
orbitp= soup.find('tr',class_='row-6 even').find('td',class_='column-1').text
orbitp2= soup.find('tr',class_='row-6 even').find('td',class_='column-2').text



orbitd



orbitd2



orbitp



orbitp2



surface= soup.find('tr',class_='row-7 odd').find('td',class_='column-1').text
surface2= soup.find('tr',class_='row-7 odd').find('td',class_='column-2').text
firstrecord= soup.find('tr',class_='row-8 even').find('td',class_='column-1').text
firstrecord2= soup.find('tr',class_='row-8 even').find('td',class_='column-2').text



surface



surface2



firstrecord




firstrecord2



recordby= soup.find('tr',class_='row-9 odd').find('td',class_='column-1').text
recordby2= soup.find('tr',class_='row-9 odd').find('td',class_='column-2').text



recordby



recordby2



marsfacts = {'Key':  [equator, polar, mass, moon, orbitd, orbitp, surface, firstrecord, recordby],
        'Value': [equator2, polar2, mass2, moon2, orbitd2, orbitp2, surface2, firstrecord2, recordby2]
        }



import pandas as pd



marsfacts_df = pd.DataFrame (marsfacts, columns = ['Key','Value'])



marsfacts_df



# render dataframe as html
mars_html = marsfacts_df.to_html()
print(mars_html)

# # Mars Hemispheres



#open Chromedriver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=True)




#change the url to the site I want to visit
#url = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
#browser.visit(url)




#change the url to the site I want to visit
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)




#set html and soup
html = browser.html
soup = bs(html, "html.parser")




#inspect the site to find what I want to scrape
hemi_title= soup.find('div',class_='description').find('h3').text



print(hemi_title)

def scrape_info():

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "equator": equator,
        "equator2": equator2,
        "polar": polar,
        "polar2": polar2,
        "mass": mass,
        "mass2": mass2,
        "moon": moon,
        "moon2": moon2,
        "orbitd": orbitd,
        "orbitd2": orbitd2,
        "orbitp": orbitp,
        "orbitp2": orbitp2,
        "surface": surface,
        "surface2": surface2,
        "firstrecord": firstrecord,
        "firstrecord2": firstrecord2,
        "recordby": recordby,
        "recordby2": recordby2,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

