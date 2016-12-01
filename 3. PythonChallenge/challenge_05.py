import pickle
from urllib.request import *

url = "http://www.pythonchallenge.com/pc/def/banner.p"
page_source = urlopen(url).read()
data = pickle.loads(page_source)

for line in data:
    print("".join(tup[0] * tup[1] for tup in line))