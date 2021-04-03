# Web Scraping Challenge - Mission to Mars

![Mars](images/mars.jpg)

## Scraping Mars Data
The [Mission to Mars](Mission_to_Mars\mission_to_mars.ipynb) Jupyter Notebook includes uses BeautifulSoup, Pandas and Splinter to scrape data from the following sites.

> [NASA Mars News Site](https://redplanetscience.com/) - scrapes featured latest news title and paragraph text
<br/>[Mars Space Images](https://spaceimages-mars.com) - scrapes the featured image
<br/> [Mars Facts](https://galaxyfacts-mars.com) - scrapes the table containing facts about Mars
<br/> [Mars Hemispheres](https://marshemispheres.com/) - scrapes the images of the 4 Mars hemispheres and their corresponding titles

<br/>

## Mars MongoDB and Flask Application
The Mars application uses the scraping functionality created in the Mission to Mars jupyter notebook and stores the data retrieved a MongoDB database. The data is then pulled from the database and displayed. Each click of the "Scrape New Data" button on the page, will scrape the above sites for updated data. 

The following is a screenshot of the Mission to Mars application:

![Mission to Mars Application](images/Mission_to_Mars_fullscreen.PNG)
