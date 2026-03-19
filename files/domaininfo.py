import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore


def domain_info(url: str):

    r = requests.get(f"https://urlvoid.com/scan/{url}/")

    if r.status_code != 200:
        return ""

    soup = bs(r.content, "lxml")

    tables = soup.find_all(
        "table",
        attrs={"class": "table table-custom table-striped"},
        limit=2
    )

    result_domain = ""

    for table in tables:
        for row in table.find("tbody").find_all("tr"):

            key = row.find_all("td")[0].getText(strip=True)
            value = row.find_all("td")[1].getText(strip=True)

            result_domain += (
                Fore.GREEN + "[ - ] "
                + Fore.WHITE + key
                + Fore.YELLOW + " ==== >> "
                + Fore.LIGHTWHITE_EX + value
                + Fore.RESET + "\n"
            )

    print(result_domain)
    with open("results/domaininfo.txt","w",encoding="utf-8") as f:
        f.write(result_domain)
    print("\nDosya Kaydedildi: domaininfo.txt")