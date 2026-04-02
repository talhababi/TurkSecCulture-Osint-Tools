# Made by Ar-Ge Team - Turkhackteam - Tbabi

import os
from colorama import Fore, init, Style
from pyfiglet import figlet_format
import files.urlfinder as urlf
import files.phoneNoosint as phoneo
import files.iposint as iposint
import files.whoisQuery as whoisquery
import files.domaininfo as domaininfo
import files.reverseip as reverseip
import files.subdomainfinder as subs
import files.dnspython as dnspy
import time
import files.recons as reconn
from urllib.parse import urljoin, urlparse

init()
version = "v1"
app_name = f"TurkSecCulture Osint Tools {version}"
developer = "@tbabi - TurkHackTeam"
banner = figlet_format("TSC - Osint", font="doom")
selectList = """
1 - Phone Number Osint
2 - URLFinder
3 - IP Osint
4 - Whois Query
5 - Domain Info
6 - Reverse IP
7 - Subdomain Finder (With IP)
8 - Find All IPs
9 - Find All MX Records
10 - Full Detailed Recon!
"""

class App:
    def __init__(self) -> None:
        print("\n" + Fore.RED + banner + "\n" + Fore.GREEN + app_name + "\t" + developer)
        print(selectList)
        self.select = input("> " + Style.RESET_ALL)
        if self.select == "1":
            self.phonenoosint()
        elif self.select == "2":
            self.urlfinder()
        elif self.select == "3":
            self.ipOsint()
        elif self.select == "4":
            self.whoisq()
        elif self.select == "5":
            self.domaininf()
        elif self.select == "6":
            self.reverseipf()
        elif self.select == "7":
            self.subdomain()
        elif self.select == "8":
            self.allip()
        elif self.select == "9":
            self.allsmtp()
        elif self.select == "10":
            self.detailedrecon()
        else:
            print("\nLütfen geçerli bir değer giriniz")
            time.sleep(3)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            App()
    def phonenoosint(self):
        selectPhone = input("\nTelefon Numarasını Giriniz (Örn: +905555555555): ")
        phoneo.phoneosint(selectPhone)
        time.sleep(3)
        App()
    def urlfinder(self):
        selectUrl = input("\nURL Giriniz (Örn: https://google.com/): ")
        urlf.urlFinder(url=selectUrl.strip())
        time.sleep(3)
        App()
    def ipOsint(self):
        selectIp = input("\nIP Adresi Giriniz (Örn: 127.0.0.1): ")
        iposint.getİpİnformations(selectIp)
        time.sleep(3)
        App()
    def whoisq(self):
        selectDomain = input("\nDomain Giriniz (Örn: https://google.com/): ")
        whoisquery.whoiss(selectDomain)
        time.sleep(3)
        App()
    def domaininf(self):
        selectDomain = input("\nHTTP/HTTPS Olmadan Domain Giriniz (Örn: google.com): ")
        domaininfo.domain_info(selectDomain)
        time.sleep(3)
        App()
    def reverseipf(self):
        selectIp = input("\nIP Adresi Giriniz (Örn: 127.0.0.1): ")
        reverseip.find_ips(selectIp)
        time.sleep(3)
        App()
    def subdomain(self):
        selectDomain = input("\nHTTP/HTTPS Olmadan Domain Giriniz (Örn: google.com): ")
        subs.find_subdomains(selectDomain)
        time.sleep(3)
        App()
    def allip(self):
        selectDomain = input("\nHTTP/HTTPS Olmadan Domain Giriniz (Örn: google.com): ")
        dnspy.find_all_ip(selectDomain)
        time.sleep(3)
        App()
    def allsmtp(self):
        selectDomain = input("\nHTTP/HTTPS Olmadan Domain Giriniz (Örn: google.com): ")
        dnspy.find_all_smtp(selectDomain)
        time.sleep(3)
        App()
    def detailedrecon(self):
        selectUrl = input("Domain Giriniz (Örn: https://google.com/): ")
        parsed = urlparse(selectUrl)
        domain = parsed.netloc
        reconn.run_recon(selectUrl)
        print(f"\nSonuçlar {domain}_recon.txt olarak kaydedildi!")
        time.sleep(3)
        App()

if __name__ == "__main__":
    App()
