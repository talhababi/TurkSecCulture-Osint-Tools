from colorama import Fore, init
import requests
import json
import sys

def getİpİnformations(ip: str) -> str:

    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    r = requests.get(f'http://ip-api.com/json/{ip}',headers=header)
    jsondict = json.loads(r.text)
    if jsondict["status"] == "fail":
        print(red+"Process Resulted in an Error")
        sys.exit()
    else:
        result = f"""
------------
[-] İşlem: {jsondict["status"]}
[-] Ülke: {jsondict["country"]}
[-] Ülke Kodu: {jsondict["countryCode"]}
[-] Bölge: {jsondict["region"]}
[-] Bölge Adı: {jsondict["regionName"]}
[-] Şehir: {jsondict["city"]}
[-] Zip: {jsondict["zip"]}
[-] lat: {jsondict["lat"]}
[-] lon: {jsondict["lon"]}
[-] Saat Dilimi: {jsondict["timezone"]}
[-] isp: {jsondict["isp"]}
[-] Organizasyon: {jsondict["org"]}
[-] İp: {jsondict["query"]}
------------
"""
        print(result)
        with open("results/iposint.txt","w",encoding="utf-8") as f:
            f.write(result)
        print("\nDosya Kaydedildi: iposint.txt")