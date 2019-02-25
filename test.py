import os

from urllib.request import urlopen


class TestURLFile:
	
	file_name = "images.txt"
	
	def test_file_exists(self):
		assert os.path.isfile(self.file_name)
	
	def test_valid_urls(self):
		with open(self.file_name, "r") as f:
			for url in f.readlines():
				assert urlopen(url)


if __name__ == "__main__":
	
	test = TestURLFile()
	test.test_file_exists()
	test.test_valid_urls()
	
