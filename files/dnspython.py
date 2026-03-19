import dns.resolver

def find_all_ip(domain: str):
    iplist = ""
    try:
        all_ip = dns.resolver.resolve(domain,"A")
    except dns.resolver.NoAnswer:
        print("Kayıt Bulunamadı")
        return
    except dns.resolver.NXDOMAIN:
        print("Domain yok")
        return

    for i in all_ip:
        iplist += str(i) + "\n"
    print(iplist)
    
    with open("results/iplist.txt","w",encoding="utf-8") as f:
        f.write(iplist)
    
    print("\nDosya Kaydedildi: iplist.txt")

def find_all_smtp(domain: str):
    smtplist = ""
    try:
        all_smtp = dns.resolver.resolve(domain, "MX")
    except dns.resolver.NoAnswer:
        print("MX kaydı yok")
        return
    except dns.resolver.NXDOMAIN:
        print("Domain yok")
        return

    for i in all_smtp:
        smtplist += str(i) + "\n"
    print(smtplist)

    with open("results/smtplist.txt","w",encoding="utf-8") as f:
        f.write(smtplist)

    print("\nDosya Kaydedildi: smtplist.txt")

