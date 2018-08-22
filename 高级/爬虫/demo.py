import urllib.request
import urllib.parse
import urllib.request, urllib.parse, http.cookiejar,re
from typing import List, Any

from bs4 import BeautifulSoup

def gethtml(url):
    cj = http.cookiejar.CookieJar()

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()

    html_string = html_bytes.decode('utf-8')

    return html_string

html_url = gethtml("http://zst.aicai.com/ssq/openInfo/")

soup=BeautifulSoup(html_url, "html.parser")

# print(soup.prettify())

Str_Date=soup.find(onmouseover="this.style.background='#fff7d8'")

date_str = Str_Date.findAll("td")[0]

red = Str_Date.findAll("td")[2:8]

blue = Str_Date.findAll("td")[8]

print(date_str.getText()+" 期中奖号码： ")

for s in red:

    print('\033[1;31m'+s.getText())

print('\033[1;34m' + blue.getText() + '\033[0m')




