
""""
Pozitif Sayıları Toplama
Bir liste içerisindeki pozitif sayıları bulan ve bunların toplamını döndüren bir fonksiyon yazın.
Eğer liste boşsa veya pozitif sayı yoksa 0 döndürsün.
Beklenen Çıktı:

Girdi: [-10, 15, -20, 30, -5]
Çıktı: 45
"""

#liste = [-10, 15, -20, 30, -5]


liste = [-10, 15, -20, 30, -5]
toplam = 0
if len(liste) == 0:
    print("Liste Bos!")
for x in liste:
    if x > 0:
        toplam += x
print('Toplam:',toplam)






