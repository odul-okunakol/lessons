
#1. Liste Toplamı ve Ortalaması
#Bir fonksiyon yaz:
#Parametre olarak liste alsın.
#Listenin elemanlarının toplamını ve ortalamasını döndür.
#Beklenen Çıktı:

#Liste: [10, 20, 30, 40]
#Toplam: 100
#Ortalama: 25.0

def ort_bulma(sayilar):
    toplam = sum(sayilar)
    ortalama=toplam / len(liste)
    return (toplam,ortalama)


liste = [10, 20, 30,40]

toplam,ortalama = ort_bulma(liste)
print(liste)
print(f"Toplam: {toplam}")
print(f"ortalama: {ortalama}")







