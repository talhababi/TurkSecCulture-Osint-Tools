import requests

def find_ips(ip: str):
    header = {"User-Agent":"Mozilla/5.0"}
    r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}",headers=header)
    domains = r.text
    if "error check" in domains:
        print("IP Adresi Yanlış, Geçerli IP Giriniz")
    elif "No DNS" in domains:
        print("Sonuç Bulunamadı")
    else:
        print(domains + "\n")
        with open("results/reverseip.txt","w",encoding="utf-8") as f:
            f.write(domains)
        print("Dosya Kaydedildi: reverseip.txt")