# Mission-to-Mars

## Overview
The purpose of this analysis is to utilize BeautifulSoup and Splinter to scrape full-resolution images of Mars’ hemispheres and their titles, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Results 

### Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
Using BeautifulSoup and Splinter, full-resolution images and titles of Mars’s hemispheres were scraped. The full Jupyter Notebook for this deliverable can be referenced here: [Mission_to_Mars_Challenge.ipynb](https://github.com/lkachury/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb)

The full-resolution images and titles of the hemispheres were added to the dictionary: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/188778788-2042b224-4b88-4b4e-b571-7bfa9203db8a.png)

The list contains the dictionary of the full-resolution image URL string and title for each hemisphere image: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/188778714-9e49bcf2-c3b1-4f50-8182-0b9ad015386d.png)

### Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
Using Python and HTML skills, the code created in Deliverable 1 was added to the [scraping.py](https://github.com/lkachury/Mission-to-Mars/blob/main/scraping.py) file, the Mongo database was updated, and the [index.html](https://github.com/lkachury/Mission-to-Mars/blob/main/templates/index.html) file was modified so the webpage contains all the information collected in this module as well as the full-resolution image and title for each Mars hemisphere image. 

The [scraping.py](https://github.com/lkachury/Mission-to-Mars/blob/main/scraping.py) file contains code that retrieves the full-resolution image URL and title for each hemisphere image: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/188777871-728c00d4-ec54-4b60-b437-b6815b96af08.png)
![image](https://user-images.githubusercontent.com/108038989/188777954-1ee3ecc4-d67c-4c40-9742-b7a0bf297080.png)

The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/188778054-ddb0bc6d-4d1f-453e-9b58-6aa8993d51ae.png)

The [index.html](https://github.com/lkachury/Mission-to-Mars/blob/main/templates/index.html) file contains code that will display the full-resolution image URL and title for each hemisphere image: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/188778274-96cfcda2-560c-42c2-beac-70296648474a.png)

After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images:
<br /> ![image](https://user-images.githubusercontent.com/108038989/188779821-cfe13597-afe3-4f29-b1d7-ca948bb5c600.png)
![image](https://user-images.githubusercontent.com/108038989/188779892-c867552f-cca3-4eb8-935c-76af47cd3615.png)

### Deliverable 3: Add Bootstrap 3 Components
Update the web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.


The webpage is mobile-responsive: 

Two additional Bootstrap 3 components are used to style the webpage: 
