"""
Sayı Tahmin Oyunu
Kullanıcıdan bir sayı girmesini isteyin. Sayı, bilgisayar tarafından rastgele belirlenen bir sayı
ile karşılaştırılsın.
Kullanıcı doğru tahmin edene kadar ipuçları (daha büyük ya da daha küçük) verin. Beklenen Çıktı:

Bilgisayarın seçtiği sayı: 8
Kullanıcı tahmini: 5
Çıktı: Daha büyük!
"""
import random

def tahminleme():
    while True:
        bilgisayar_tahmini = random.randint(1, 100)

        while True:
            kullanici_sayisi = int(input("Kullanıcı tahmini: "))
            print(f"Kullanıcı tahmini: {kullanici_sayisi}")
            if kullanici_sayisi < bilgisayar_tahmini:
             print(f"Cikti: Daha büyük!")
            elif kullanici_sayisi > bilgisayar_tahmini:
              print(f"Cikti: Daha kücük!")
            else:
              print(f"Bilgisayarın seçtiği sayı: {bilgisayar_tahmini}")
              print(f"Dogru!")
              break

tahminleme()
