# Image downloader script
This python3 based project basically contains a 
  - python script which accepts a text file as an argument
  - Said text file contains one or more image urls
  - Downloads the images from those urls and saves it locally
 
Supporting libraries include:
  - [Os](https://docs.python.org/3.4/library/os.html)
  - [Urllib](https://docs.python.org/3/howto/urllib2.html)


Steps to run project:
  - git clone the project
  - Make sure you have python3 installed and set up properly
  - apply the command `python3 main.py images.txt` to initiate the program and save all the image urls in a folder labelled `images` in your current working directory of that project.
  - apply the command `python3 test.py` to run some simple test cases that include testing for
    1. assert the existense of the file we'll be reading from
    2. assert the existense of valid urls in said file that was tested on.
