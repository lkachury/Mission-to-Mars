# --------------------------
# Scrape Mars Data: The News
# --------------------------

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Import pandas for .read_html() function.
import pandas as pd

# Set the executable path and initialize a browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Refactor the code as a function and add an argument
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Parse the HTML with BeautifulSoup 
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:     

        # Scrape the title 
        slide_elem = news_soup.select_one('div.list_text')
        
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    # Insert return statement
    return news_title, news_p

# --------------------------------
# Scrape Mars Data: Featured Image
# --------------------------------

# Declare and define the function 
def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try: 

        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError: 
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    # Add return statemnt 
    return img_url

# ----------------------------
# Scrape Mars Data: Mars Facts
# ----------------------------

# Define the function
def mars_facts():

    # Add try and except block 
    try: 

        # Scrape the entire table with Pandas' .read_html() function
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None
    
    # Assign columns and set the index of the DataFrame
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    # Convert the DataFrame back into HTML-ready code 
    df.to_html()