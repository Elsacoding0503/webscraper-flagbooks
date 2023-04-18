# 旗標
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

url_flags = 'https://www.flag.com.tw/books/school'
res_flags = requests.get(url=url_flags,headers=headers)
soup_flags = bs(res_flags.text, 'lxml')

title = [i.text for i in soup_flags.find("table", "rwd-table").select("p")]
links = [i.find("a")['href'] for i in soup_flags.find("table", "rwd-table").find_all("div", {'style': 'height:10x;background-color:#6e6962;'})]
zipped_flags = zip(title, links)
df_flags = pd.DataFrame(list(zipped_flags))
print(df_flags)