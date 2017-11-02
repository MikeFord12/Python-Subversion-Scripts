__author__ = 'fordmi'
from bs4 import BeautifulSoup
import urllib2

directoryStrings = []
softwareNamesAndNums = []

SVUrl = "http://mystique/svn/te/testeng/software/"

pageData = urllib2.urlopen(SVUrl)

data = BeautifulSoup(pageData, "html.parser")

results = data.find_all("dir")

for element in results:
    softwareNamesAndNums.append(element['name'])

for sw in softwareNamesAndNums:
    print sw