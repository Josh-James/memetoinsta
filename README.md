# Meme Uploader For Instagram
## Intro
This project takes popular memes from Reddit and uploads them to an Instagram account of choice. 
Uses scrapy for web scraping / photo retrieval and instabot for uploading to an Instagram account
## How To Use
### Install:
* Scrapy
* PIL
* Requests
* Random (if not included in os)
* Instabot (Latest works fine, running *configdel.py* may not be needed if version 0.108.0 is installed)
### Run (in order):
Pre-requirements: 
* Update *postpicker.py* with username and password for the Instagram account being used
* Check root directory for photo downloads in *mememachine.py* to ensure that they end up in the proper directory
Steps once configured:

1. mememachine.py
2. postpicker.py
3. configdel.py (if you plan on running the program more than once) 

**Note:** Initially this project had a main.py file that automated the running process, however automating this process can trigger Instagram's botting filters.

**CREATED AND CONFIGURED FOR EDUCATIONAL PURPOSES ONLY**
**USE PROGRAM WITH CAUTION, CAN CAUSE ACCOUNT LOCKOUT OR TERMINATION IF USED IMPROPERLY.**
