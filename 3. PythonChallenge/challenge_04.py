import re
from urllib.request import *

base_url = "http://www.pythonchallenge.com/pc/def/"
url = base_url + "linkedlist.php?nothing=12345"
solved = False

for i in range(400):
    page_source = urlopen(url).read().decode("utf-8")
    print(page_source)

    temp = "".join(re.findall("nothing is (\d+)", page_source))

    if temp == "":
        if page_source.find("Divide by two") > -1:
            nothing = str(int(int(nothing)/2))
        elif page_source.find("html") > -1:
            solved = True
            break
    else:
        nothing = temp

    url = base_url + "linkedlist.php?nothing=" + nothing

if solved:
    print("\nSolution found\nGo to:", base_url + page_source)
else:
    print("\nSolution not found")
