ogrenciler=[{"isim":"Ayse","not":85},
            {"isim":"Ali","not":90},
            {"isim":"Mehmet","not":78},]
toplam = 0
eleman = 0
for x in ogrenciler:
    print(f"{x['isim']}:{x['not']}")
    toplam += int(x['not'])
    eleman=int(len(ogrenciler))
print('Sinif Ortalamasi:',toplam / eleman)