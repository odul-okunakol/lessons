#Bir fonksiyon dışarıdan dictionary parametresi alacak.
#Bunlar öğrenci ismi ve notlarından oluşuyor olacak.
#Öncelikle notlar 100('dan büyük olamaz ve str değer olamaz. '
#                   'Eğer 100')den büyük ise basitçe hata mesajı döndürmeli (Raise error).
#Eğer int veri gelmemişse Value error döndürmeli. Notların harf değerleri hesaplanmalı şuna göre.

#90> AA
#80>= BA
#70 >= BB
#60>= CB
#50>=CC
#Geriye kalanlar FF.

#Sonuçrta bir return dönmeyeceğiz öğrenci ismini ve harf notunu aynı satırda print etmeliyiz.

sozluk={'Ali':-10,'Ayse':'aaa','Ahmet':101,'Fatma':91,'Jale':13}

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

def notlar(sozluk):
    for isim, puan in sozluk.items():
     try:
        if not isinstance(puan, int):
            raise TypeError(f"Hata: {isim} için puan bir int değil! ({puan})")
        if puan > 100:
            raise ValueError(f"Hata: {isim} için puan 100'den büyük! ({puan})")
        elif puan <= 100:
            print(f"{isim}: {not_donustur(puan)}")
     except (TypeError, ValueError) as e:
            print(e)
    return ""

print(notlar(sozluk))

