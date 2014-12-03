pydownload
====

A simple python script to download files of given extension types from a web page.  

## Dependencies
-------------------
<b>requests</b> - `pip install requests`<br>
<b>wget</b> - `pip install wget`<br>
<b>beautifulsoup4</b> - `pip install beautifulsoup4`<br>

## Features
-------------------

 * Download files with any extension name
 * Progress bar for indvidual files

## Setup
-------------------
Clone the repo:
```
git clone https://github.com/rishy/pydownload.git
```
Or you can alternatively download the zip file from: <b>https://github.com/rishy/pydownload.git</b>

For first use, install all the dependencies from <b>requirements.txt</b> file:
```
pip install -r requirements.txt
```

You are now ready to download files, <b>cd</b> into the cloned folder and run the python script:
```
python download.py 
```

## Example Usage

After running the script using above command, you will be prompted to enter the <b>url</b> of the page to download files from:
```
Enter the url: www.example.com
```

Enter a comman separated list of extensions of files to download:
```
Enter a comma seperated list of file Extensions: zip, pdf, srt
```