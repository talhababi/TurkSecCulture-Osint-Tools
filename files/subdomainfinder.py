import requests

def find_subdomains(url: str):
    header = {"User-Agent":"Mozilla/5.0"}
    r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={url}",headers=header)
    domains = r.text
    if "error invalid" in domains:
        print("Domain yanlış girilmiş, yeni domain giriniz")
    elif "No sub" in domains:
        print("Sonuç Bulunamadı")
    else:
        print(domains + "\n")
        with open("results/subdomainlist.txt","w",encoding="utf-8") as f:
            f.write(domains)
        print("Dosya Kaydedildi: subdomainlist.txt")