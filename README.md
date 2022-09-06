# Mission-to-Mars

## Overview
The purpose of this analysis is to utilize BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and their titles, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Results 

### Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
Using BeautifulSoup and Splinter, you’ll scrape full-resolution images of Mars’s hemispheres and the titles of those images.


Code is written that retrieves the full-resolution image and title for each hemisphere image: 

The full-resolution images of the hemispheres are added to the dictionary: 

The titles for the hemisphere images are added to the dictionary: 

The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image: 


### Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
Using Python and HTML skills, the code created in Deliverable 1 was added to scraping.py file, updated the Mongo database, and modified the index.html file so the webpage contains all the information collected in this module as well as the full-resolution image and title for each hemisphere image: 

The scraping.py file contains code that retrieves the full-resolution image URL and title for each hemisphere image: 

The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image: 

The index.html file contains code that will display the full-resolution image URL and title for each hemisphere image: 

After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images: 

### Deliverable 3: Add Bootstrap 3 Components
Update the web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.


The webpage is mobile-responsive: 

Two additional Bootstrap 3 components are used to style the webpage: 
