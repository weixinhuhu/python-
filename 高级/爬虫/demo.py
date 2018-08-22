import urllib.request
import urllib.parse
import urllib.request, urllib.parse, http.cookiejar,re
from bs4 import BeautifulSoup

def getHtml(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string

html = getHtml("http://zst.aicai.com/ssq/openInfo/")

soup=BeautifulSoup(html,"html.parser")

# print(soup.prettify())

StrDate=soup.find(onmouseover="this.style.background='#fff7d8'")

datestr=StrDate.findAll("td")[0]

red=StrDate.findAll("td")[2:8]

blue=StrDate.findAll("td")[8]

l= [redboll.getText() for redboll in red]

print(datestr.getText()+" 期中奖号码： ")

for s in l:
    print('\033[1;31m'+s)

print('\033[1;34m' + blue.getText() + '\033[0m')




