def cift_sayilari_bultopla(sayilar):
    cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
   toplam = sum(cift_sayilar)
  return cift_sayilar, toplam

liste = [5, 10, 15, 20, 25,30]

ciftler, toplam = cift_sayilari_bultopla(liste)
print(f"Çift Sayılar: {ciftler}")
print(f"Toplam: {toplam}")

def cift_sayilari_bultopla2(sayilar2):
    cift_sayilar=[]
    for i in sayilar2:
        if i %2==0:
            cift_sayilar.append(i)
    return cift_sayilar


print(cift_sayilari_bultopla2(liste))