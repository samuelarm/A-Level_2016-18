import re
from urllib.request import *

url = "http://www.pythonchallenge.com/pc/def/equality.html"
page_source = urlopen(url).read().decode("utf-8")
text = re.findall("<!--(.*?)-->", page_source, re.DOTALL)[0]

pattern = "[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"
matches = re.findall(pattern, text)

for match in matches:
    print(match[4], end="")