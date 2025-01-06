"""
Benzersiz Elemanları Bulma
Bir liste içerisindeki tekrar eden elemanları çıkararak sadece benzersiz elemanları döndüren bir fonksiyon yazın.
Beklenen Çıktı:

Girdi: [1, 2, 2, 3, 4, 4, 5]
Çıktı: [1, 3, 5]
"""

#liste = [1, 2, 2, 3, 4, 4, 5]
#def benzersiz_bul(liste):
 #      benzersiz = set(liste)
#       return benzersiz

#print(benzersiz_bul(liste))

liste = [1, 2, 2, 3, 4, 4, 5]
def benzersiz_bul(liste):
    benzersiz_liste = []
    for x in liste:
      if liste.count(x) == 1:
        benzersiz_liste.append(x)
    return benzersiz_liste

print(benzersiz_bul(liste))



