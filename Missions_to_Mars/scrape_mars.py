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
    facts_table_html = facts_df.to_html()

    #Collect data in dictionary
    mars_data = {
        "title": title,
        "para": para,
        "image": featured_image_url,
        "table": facts_table_html
    }
   


    return mars_data
