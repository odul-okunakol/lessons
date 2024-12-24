def cift_sayilari_bultopla(sayilar):
    cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
    toplam = sum(cift_sayilar)
    return cift_sayilar, toplam

liste = [5, 10, 15, 20, 25,30]

ciftler, toplam = cift_sayilari_bultopla(liste)
print(f"Çift Sayılar: {ciftler}")
print(f"Toplam: {toplam}")

