import os

from urllib import request
from urllib.error import HTTPError


class Downloader:

	file_path = ""
	
	def __init__(self, file_name):
		self.file_name = file_name
	
	def create_directory(self):
		directory_name = "images"
		directory_path = os.path.join(os.getcwd(), directory_name)
		if not os.path.exists(directory_path):
			print("Images directory doesn't exist. Creating anew.")
			os.makedirs(directory_name)
		return directory_path
	
	def download_images(self):
		path = self.create_directory()
		
		with open(self.file_name, "r") as image_urls:
			for url in image_urls.readlines():
				try:
					filename = url.split("/")[-1]
					filename_path = os.path.join(path, filename)
					print("Saving file ", filename, " in the ", path, 							  "directory.")
					request.urlretrieve(url, filename_path)
				except FileNotFoundError as path_error:
					print(path_error)
				except HTTPError as url_error:
					print(url_error)

