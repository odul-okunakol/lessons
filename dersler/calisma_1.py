#Koşullu İfadeler: if-elif-else

sayi=10
if sayi>0:
    print("pozif bir sayi")
elif sayi<0:
    print("negatif bir sayi")
else:
    print("sayi 0'dir")

#Mantıksal Operatörler--and,or,not
x=5
y=10
if x>0 and y>0:
    print("x ve y pozitiftir")
if x>0 or y<0:
    print("En az biri pozitiftir")
if not (x < 0):
    print("x negatif değildir")

#fonksiyonlar
def fonksiyon_adi(parametreler):
    return sonuc

def topla(a,b):
    return a+b

sonuc=topla(10,20)
print(sonuc)

#Parametre ve Varsayılan Değerler
def merhaba(isim="Misafir"):
    print(f"Merhaba, {isim}!")

merhaba()
merhaba("Ali")

#Anahtar Kelime ve Esnek Parametreler
def bilgi(isim,yas):
    print(f"{isim}: {yas}")
bilgi(yas=25, isim="Ayşe")

#Esnek Parametreler--*args: --**kwargs:
def toplama(*sayilar):
    return sum(sayilar)

print(toplama(10,20,45,67))

def detaylar(**bilgiler):
   for anahtar,deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

(detaylar(isim="Ali", yas=30))

topla = lambda x, y: x + y
print(topla(5, 3))


#def kullanici_girisi(kullanici_adi, sifre):
#    dogru_kullanici = "admin"
 #   dogru_sifre = "1234"

 #   if kullanici_adi == dogru_kullanici and sifre == dogru_sifre:
 #       return "Giriş Başarılı!"
 #   else:
#        return "Kullanıcı adı veya şifre hatalı."
#
#kullanici_adi = input("Kullanıcı Adı: ")
#sifre = input("Şifre: ")

#print(kullanici_girisi(kullanici_adi, sifre))

def cift_sayilari_bultopla(sayilar):
    cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
    toplam = sum(cift_sayilar)
    return cift_sayilar, toplam

liste = [5, 10, 15, 20, 25,30]

ciftler, toplam = cift_sayilari_bultopla(liste)
print(f"Çift Sayılar: {ciftler}")
print(f"Toplam: {toplam}")


def ogrenci_notlarini_isle(ogrenci_notlari):
    print("Öğrenci ve notlar:")
    for ogrenci, notu in ogrenci_notlari.items():
        print(f"- {ogrenci}: {notu}")

    ortalama = sum(ogrenci_notlari.values()) / len(ogrenci_notlari)
    print(f"Sınıf Ortalaması: {ortalama:.2f}")


# Örnek Veri
ogrenciler = {"Ayşe": 85, "Ali": 90, "Mehmet": 78}

# Fonksiyonu Çağır
ogrenci_notlarini_isle(ogrenciler)

def siparis_ozeti(*args, **kwargs):
    print("Siparişler:")
    for urun in args:
        print(f"- {urun}")
    print("\nMüşteri Bilgileri:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Örnek Kullanım
siparis_ozeti("Pizza", "Kola", "Tatlı", ad="Ayşe", adres="İstanbul", telefon="1234567890")

def calisan_ekle(ad, soyad, **kwargs):
    calisan = {
        "Ad": ad,
        "Soyad": soyad,
    }
    calisan.update(kwargs)
    return calisan

# Örnek Kullanım
calisan = calisan_ekle("Ali", "Kaya", pozisyon="Mühendis", maas=10000)
print(calisan)

def not_donustur(puan):
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    elif puan >= 50:
        return "CC"
    else:
        return "FF"

# Örnek Kullanım
print(f"Not: {not_donustur(85)}")

def not_donustur(puan):
    not_araliklari = {
        "AA": 90,
        "BA": 80,
        "BB": 70,
        "CB": 60,
        "CC": 50,
        "FF": 0,  # Minimum değer, her durumda "FF" için çalışır
    }

    for harf_notu, alt_limit in not_araliklari.items():
        if puan >= alt_limit:
            return harf_notu

# Örnek Kullanım
print(f"Not: {not_donustur(85)}")


def toplam_ve_ortalama(*args):
    toplam = sum(args)
    ortalama = toplam / len(args) if args else 0
    return toplam, ortalama

# Örnek Kullanım
sonuc = toplam_ve_ortalama(10, 20, 30, 40)
print(f"Toplam: {sonuc[0]}, Ortalama: {sonuc[1]:.2f}")



def kisi_bilgisi(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Örnek Kullanım
kisi_bilgisi(ad="Ali", soyad="Yılmaz", yas=25, meslek="Mühendis")


#notpuan = 72

#not_araliklari = {
#"CC": 50,
 #       "AA": 90,
   #     "BA": 80,
    #    "BB": 70,
      #  "CB": 60,
    #    "FF": 0,  # Minimum değer, her durumda "FF" için çalışır
   # }

#for harf,puan in not_araliklari.items():
#    if notpuan >= puan:
#       print(harf)


yenipuan=45

if yenipuan >= 90:
    print('AA')
elif yenipuan >= 80:
    print('BA')
elif yenipuan >= 70:
    print('BB')
else:
    print('FF')

def kullanici_giris(kullanici_adi,sifre):
    if kullanici_adi=="admin" and sifre==123:
        return "Giris Basarili"
    else:
        return "Giris Basarili Degil"

kullanici_giris("admin",123)
print(kullanici_giris("admin",123))