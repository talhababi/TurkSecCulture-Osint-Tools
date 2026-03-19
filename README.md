# TurkSecCulture-Osint-Tools
TurkSecCulture Osint Tools v2 Yayında!

+] İçerik Listesi [+]

1. Telefon Numarası Bilgi Toplama
2. URL Finder (Link Ayıklayıcı)
3. IP Osint & Coğrafi Konum
4. Detaylı Whois Sorgusu
5. Domain Güvenlik Analizi
6. Subdomain Finder (Alt Alan Adları)
7. IP Listeleme & MX Kayıtları
8. Kurulum ve Kullanım



Herkese Merhaba Değerli TürkHackTeam Üyeleri,

Ar-Ge ekibi olarak geliştirdiğimiz, hedef hakkında pasif ve aktif bilgi toplama süreçlerini hızlandıran "TurkSecCulture Osint Tools" projemiz tamamlanmıştır. Python ile geliştirilen bu araç, siber istihbarat çalışmalarında ihtiyaç duyulan temel sorguları tek bir arayüzden yapmanıza olanak sağlar.

Emeği Geçenler: @0x1A7 (https://www.turkhackteam.org/uye/934046/) , @tbabi (https://www.turkhackteam.org/uye/1036371/)



[+] Modül Detayları ve Görsel Analiz [+] 


1. Telefon Numarası Bilgi Toplama:
Hedef numara girildiğinde operatör bilgisi (Turk Telekom vb.), ülke kodu ve numaranın aktiflik/geçerlilik durumu saniyeler içinde analiz edilir. Sonuçlar phonenumberosint.txt dosyasına kaydedilir.


2. URL Finder (Link Ayıklayıcı):
Herhangi bir web sitesi verildiğinde, sayfa içerisindeki tüm iç ve dış bağlantıları (Mail, Google Services, Privacy vb.) tarayarak liste halinde sunar.


3. IP Osint & Coğrafi Konum:
Hedef IP adresinin hangi ülkede (Örn: Finlandiya), hangi şehirde ve hangi ISP (Örn: Google LLC) üzerinde barındığını, koordinat verileriyle birlikte getirir.


4. Detaylı Whois Sorgusu:
Domainin tescil edildiği firma, kayıt (1997) ve bitiş (2028) tarihleri ile DNS sunucu bilgilerini eksiksiz dökerek raporlar.


5. Domain Güvenlik Analizi:
Hedef domainin geçmiş analizlerini ve 35'ten fazla global güvenlik motorundaki (Fortinet, BitDefender, DrWeb vb.) itibar durumunu kontrol eder.


6. Subdomain Finder:
Domain altındaki tüm gizli veya açık subdomainleri (ctf, dergi, ihbar, intel vb.) bağlı oldukları IP adresleriyle birlikte listeler.




7. IP Listeleme & MX Kayıtları:
Domainin kullandığı tüm aktif IP bloklarını ve mail trafiğinin yönetildiği MX (Mail Exchanger) kayıtlarını anlık olarak çeker.




[!] Kurulum Adımları [!]

cd Desktop

git clone https://github.com/talhababi/TurkSecCulture-Osint-Tools/

cd TurkSecCultureOsint/Modules

pip install -r requirements.txt

python main.py


Saygılarla Ar-Ge Team
