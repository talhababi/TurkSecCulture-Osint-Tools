from phonenumbers import carrier, parse, geocoder, timezone, is_valid_number
from colorama import Fore, Style

def phoneosint(userPhoneNumber):
    parseNumber = parse(str(userPhoneNumber), "tr")
    operatör = carrier.name_for_number(parseNumber, "tr")
    ülke = geocoder.description_for_number(parseNumber, "tr")
    saat_dilimi = timezone.time_zones_for_number(parseNumber)
    isValidNumber = is_valid_number(parseNumber)
    if isValidNumber:
        isValidNumber = Fore.GREEN + "Geçerli!" + Style.RESET_ALL
        isValidNumberU = "Geçerli!"
    else:
        isValidNumber = Fore.RED + "Geçersiz!" + Style.RESET_ALL
        isValidNumberU = "Geçersiz!"

    print(f"""
    [+] Telefon Numarası   :  {userPhoneNumber}
    [+] Operatör   :  {operatör}
    [+] Ülke       :  {ülke}
    [+] Saat Dilimi:  {saat_dilimi}
    [+] Telefon numarası geçerli mi : {isValidNumber}
    """)
    with open("results/phonenumberosint.txt","w",encoding="utf-8") as f:
        f.write(f"""
    [+] Telefon Numarası   :  {userPhoneNumber}
    [+] Operatör   :  {operatör}
    [+] Ülke       :  {ülke}
    [+] Saat Dilimi:  {saat_dilimi}
    [+] Telefon numarası geçerli mi : {isValidNumberU}
        """)
    print("Dosya Kaydedildi: phonenumberosint.txt")
