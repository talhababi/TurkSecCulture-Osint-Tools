import whois
from colorama import Fore, init


def whoiss(user_value):

        try:
                w = whois.whois(user_value)
        except socket.gaierror:
                print("Bağlantı Kurulamadı, Daha Sonra Tekrar Deneyin")
                return
        whois_result = f"""[-] Domain Name: ,{w["domain_name"]}
        [-] Registrar:  ,{w["registrar"]}
        [-] Whois Server:  ,{w["whois_server"]}
        [-] Referral Url:  , {w["referral_url"]}
        [-] Updated Date:  ,{w["updated_date"]}
        [-] Creation Date:  ,{w["creation_date"]}
        [-] Expiration Data:  ,{w["expiration_date"]}
        [-] Name Server:  ,{w["name_servers"]}
        [-] Status:  ,{w["status"]}
        [-] Emails:  ,{w["emails"]}
        [-] Dnssec:  ,{w["dnssec"]}
        [-] Name:  ,{w["name"]}
        [-] Org:  ,{w["org"]}
        [-] Address:  ,{w["address"]}
        [-] City ,{w["city"]}
        [-] State ,{w["state"]}
        [-] Registrant Postal Code: ,{w["registrant_postal_code"]}
        [-] County ,{w["country"]}"""


        print(whois_result)
        with open("results/whoisresult.txt","w",encoding="utf-8") as f:
                f.write(whois_result)
        print("Dosya Kaydedildi: whoisresult.txt")


