import requests
import re
import os.path

URL = "http://192.168.56.101/.hidden/"
OUTFILE = "retrieved_readmes.txt"

def parse_readme(url):
	r = requests.get(url).text
	f = open(OUTFILE, "a")
	f.write(r)
	f.close()

def parse_url(path):

	if os.path.exists(OUTFILE):
		print(f"Error: {OUTFILE}: file already exists")
		return

	r = requests.get(path).text

	urls = re.findall(r'href=[\'"]?([^\'" >]+)', r)
	urls.remove('../')

	for url in urls:
		full_url = path + url

		if "README" in url:
			parse_readme(full_url)
		else:
			parse_url(full_url)

def find_flag(file):
	f = open(OUTFILE, "r")
	lines = f.read().split('\n')
	f.close()

	for line in lines:
		match = re.match(r'[0-9]', line)
		if match:
			print(line)
	

if __name__ == "__main__":
	parse_url(URL)
	find_flag(OUTFILE)
