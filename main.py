import sys

from downloader import Downloader


if __name__ == "__main__":
	try:
		file_name = sys.argv[1]
	except IndexError:
		print("Must provide one argument as the filename.")
	
	d = Downloader(file_name=file_name)
	d.download_images()

