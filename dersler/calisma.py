#Python Syntax
print("bu_dogru")

toplam= 10+25+30+\
    40+50
print(toplam)

###########################################################

#Veri_tipleri

#string/character
metin="odul"
print(metin)
print(metin[1])
print(metin[0])
print(len(metin))

#integer
sayi=75
print(sayi-5)

#float
pi=3.14
print(pi*2)

#boolen
hava_yagisli_mi= True
print(hava_yagisli_mi and False)

#Veri_Yapilari: liste,tuple,set,dict

#liste--köseli parantez
liste=[5,'odul',3.14]
print(liste)
print(liste[2])
liste.append(25)
print(liste)
liste.pop()
print(liste)
liste[0] = 12
print(liste)
liste.insert(1,"alper")
print(liste)

#tuple--normal parantez,degistirilemez sabittir
demet=(5,'odul',3.14)
print(demet)
print(demet[0])

#set-- süslü parantez,no_dublicate
kume={1,'odul',3.14}
print(kume)
kume={1,1,'odul',3.14,3.14}
print(kume)

#dictionary
sozluk1= {"isim": "Odul", "yas": 28, "boy":1.65}
print(sozluk1)
print(sozluk1["isim"])

sozluk2 = {"isim": "Odul", "boy": 1.65}
sozluk2["year"] = 1996
print(sozluk2)

#someexp
meyveler = ["Elma", "Armut", "Çilek", "Muz"]
meyveler.append("Karpuz")
print(meyveler)

meyveler.insert(1, "Mango")
print(meyveler)

meyveler.remove("Çilek")
print(meyveler)

meyveler.pop()
print(meyveler)
print(len(meyveler))

meyveler.reverse()
print(meyveler)

meyveler.sort() #alfabetik sirladi.
print(meyveler)

sayilar=[5,2,16,6.2,45]
sayilar.sort()
print(sayilar)

#veritpleri icin döngüler ve bayi ornekler
sayi_listesi=[1,2,3,4,5]
for i in sayi_listesi:
    print(i)

for indeks, eleman in enumerate(sayi_listesi):
    print(f" {indeks}. Eleman {eleman}")

carpilmis = [x * 2 for x in sayi_listesi]
print(carpilmis)

demet=(1,2,3,4,5)
for indeks, eleman in enumerate(demet):
    print(f"İndeks: {indeks}, Eleman: {eleman}")


sayilar1 = {1, 2, 3, 4, 5}
sayilar1.add(3)
sayilar1.add(6)
print(sayilar1)
sayilar1.remove(4)
print(sayilar1)

A = {1, 2, 3}
B = {3, 4, 5}
print(A&B)
print(A-B)


sozluk3 = {"isim": "Ali", "yas": 25, "meslek": "Mühendis"}
print(sozluk3["isim"])
sozluk3["sehir"] = "İstanbul"
print(sozluk3)
del sozluk3["yas"]
print(sozluk3)

for anahtar, deger in sozluk3.items():
    print(f"Anahtar: {anahtar}, Değer: {deger}")

ogrenciler=[
    {"isim":"Ali","yas":25,"dersler":["Mat","Fen"]},
    {"isim":"Ayse","yas":20,"dersler":["Kimya","Fizik"]},
]

for ogrenci in ogrenciler:
    print(f"{ogrenci['isim']} adlı öğrencinin dersleri: {', '.join(ogrenci['dersler'])}")

liste_x = [1, 2, 3, 3, 4, 4, 5]
benzersiz = set(liste_x)
print(benzersiz)

########################################################################

#Döngüler&Kosullar

x = 10
print(x)
if x > 5:
    print("x, 5'ten büyüktür!")

x=2
print(x)
if x>5:
    print("x, 5'ten büyüktür!")
else:
    print("x,5'ten kücüktür!")

not_ort=75
if not_ort >= 90:
    print("AA notunu aldi")
elif not_ort >= 80:  #ifelse gibi
    print("BA notunu aldi")
elif not_ort >= 70:
    print("BB notunu aldi")
else:
    print("Ögrenci Kaldi")


sayi = 16
if sayi > 0:
    if sayi % 2 == 0:
       print("Pozitif ve çift bir sayı.")
    else:
       print("Pozitif ve tek bir sayı.")

meyveler=["armut","elma","cilek"]

for i in meyveler:
    print(i)

for i in range(6):
    print(i)

for i in range(2,10,2):
    print(i)

for indeks,meyve in enumerate(meyveler):
    print(f"{indeks}. meyve:{meyve}")

x=0
while x<5:
    print(x)
    x+=1

for sayi in range(12):
    if sayi % 2 == 0:
        continue
    print(sayi)

sayi_listesi = [3, 7, 12, 9, 5, 18]

for sayi in sayi_listesi:
    if sayi % 3 == 0:
        print(f"{sayi}, 3'e tam bölünür.")
    else:
        print(f"{sayi}, 3'e tam bölünmez.")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
