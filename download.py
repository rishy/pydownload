import requests
import re
import wget
import os
from bs4 import BeautifulSoup

# Prompt user to enter the url to download files from
url = raw_input("Enter the url: ")

# Prompt user to enter file extensions of the file types to download
exts = raw_input("Enter a comma seperated list of file Extensions: ").split(",")

# Remove leading and trailing spaces from extensions
exts = [x.strip(' ') for x in exts]

# Convert extension list in regex form
reg = '|'.join(exts)

# Requests object for given url
req = requests.get(url)
req.raise_for_status()

html_doc = req.text.encode(req.encoding)
soup = BeautifulSoup(html_doc)

# Get the list of all the files in current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Get the link url of files with mentioned extension name
links = soup.findAll(href=re.compile("\."+reg+"$"))

for link in links:

	# Get the url from anchor tag
	href = link.get('href')

	# Get the file name from url
	file_name = href[href.rfind('/')+1:]

	# If file already exists then skip downloading it
	if file_name not in files:
		print "Downloading %s..." % href
		wget.download(href)
	