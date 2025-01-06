"""
 Sözlükte Değer Arama
Bir sözlükte verilen bir anahtarın olup olmadığını kontrol eden bir fonksiyon yazın.
Eğer anahtar mevcutsa, değerini döndürün. Mevcut değilse bir hata mesajı yazdırın.
Beklenen Çıktı:

Girdi: {"ad": "Ali", "yas": 25, "meslek": "Mühendis"}, Anahtar: "yas"
Çıktı: 25
"""
sozluk = {"ad": "Ali", "yas": 25, "meslek": "Mühendis"}

def deger_bulma(sozluk):
    for anahtar, deger in sozluk.items():
        if anahtar == "yas":
            return deger

print(deger_bulma(sozluk))