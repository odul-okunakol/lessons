

def not_hesapla(ogrenci_notlari):
    for ogrenci, notu in ogrenci_notlari.items():
        try:
            # Notun sayı olup olmadığını kontrol et
            notu = int(notu)
            if not 0 <= notu <= 100:
                raise ValueError("Not 0 ile 100 arasında olmalı.")

            # Harf notu hesaplama
            if notu >= 90:
                harf_notu = "AA"
            elif notu >= 80:
                harf_notu = "BA"
            elif notu >= 70:
                harf_notu = "BB"
            elif notu >= 60:
                harf_notu = "CB"
            elif notu >= 50:
                harf_notu = "CC"
            else:
                harf_notu = "FF"

            # Sonucu yazdır
            print(f"{ogrenci}: {harf_notu}")
        except ValueError as e:
            print(f"Hatalı giriş tespit edildi: {ogrenci} ({e})")

# Örnek Kullanım
ogrenci_notlari = {
    "Ahmet": -75,
    "Ayşe": 95,
    "Mehmet": 50,
    "Burcu": "yüz"  # Hatalı giriş
}

not_hesapla(ogrenci_notlari)
