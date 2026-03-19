import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
import os
urllists = ""

class urlFinder:
    def __init__(self, url: str):
        self.urllists = urllists
        self.url = url
        self.find_links()

    def find_links(self):

        headers = {
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01"
        }

        r = requests.get(self.url, headers=headers)

        if r.status_code != 200:
            print("Siteye erişilemedi")
            return

        soup = bs(r.content, "lxml")
        links = soup.find_all("a")

        sayac = 1

        for i in links:
            href = i.attrs.get("href")

            if href:
                print(sayac, "-->", urljoin(self.url, href))
                self.urllists = self.urllists+"\n"+urljoin(self.url, href)+"\n"
                sayac += 1

        print(f"\n{self.url} adresinde toplam {sayac-1} link bulundu.")
        with open("results/urlfinderlist.txt","w",encoding="utf-8") as f:
            f.write(self.urllists)
        print("urlfinderlist.txt Kaydedilmiştir!")