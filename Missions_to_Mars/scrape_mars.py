from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    #Gather Mars News Title and Para Text
    url_mars_news = 'https://redplanetscience.com/'
    browser.visit(url_mars_news)

    html_mars_news = browser.html
    soup_mars_news = BeautifulSoup(html_mars_news, 'html.parser')

    title_content = soup_mars_news.find('div', class_='content_title')
    para_content = soup_mars_news.find('div', class_='article_teaser_body')

    title = title_content.text.strip()
    para = para_content.text.strip()

    browser.quit()
    
    #New Browser to get featured mars image
    browser = Browser('chrome', **executable_path, headless=True)
    url_space_image = "https://spaceimages-mars.com/"
    browser.visit(url_space_image)
    html_mars_image = browser.html
    soup_mars_image = BeautifulSoup(html_mars_image, 'html.parser')

    image_url = soup_mars_image.find('img', 'headerimage')

    href = image_url['src']

    featured_image_url = url_space_image + href
    browser.quit()

    #Use pandas to scrape mars table
    url_mars_facts = 'https://galaxyfacts-mars.com/'
    facts_table = pd.read_html(url_mars_facts)
    facts_df = facts_table[0]
    new_header = facts_df.iloc[0] #grab the first row for the header
    facts_df = facts_df[1:] #take the data less the header row
    facts_df.columns = new_header #set the header row as the df header  
    facts_df = facts_df.set_index('Mars - Earth Comparison')
    facts_table_html = facts_df.to_html(classes='table table-striped table-bordered')

    #Gather Hemisphere images
    browser = Browser('chrome', **executable_path, headless=True)  

    url_hemi = "https://marshemispheres.com/"
    browser.visit(url_hemi)

    html_hemi = browser.html
    soup_hemi = BeautifulSoup(html_hemi, 'html.parser')
    items = soup_hemi.find_all('div', 'item')

    links = []
    hemisphere_image_urls = []

    for item in items:
        image_link = url_hemi + item.find('a')['href']
        links.append(image_link)

    browser.quit()

    for link in links:
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(link)
        html_hemi = browser.html
        soup_hemi = BeautifulSoup(html_hemi, 'html.parser')
        
        title = soup_hemi.find('h2', 'title').text.strip()
        download = soup_hemi.find('div', 'downloads')
        image_list = download.find('li')
        hemi_image_link = image_list.find('a')
        href = url_hemi + hemi_image_link['href']
        hemisphere_image_urls.append({"title":title, "img_url":href}) 

        browser.quit()




    #Collect data in dictionary
    mars_data = {
        "title": title,
        "para": para,
        "image": featured_image_url,
        "table": facts_table_html,
        "hemispheres": hemisphere_image_urls
    }
   


    return mars_data
