#Kelime Uzunluğu Bulma
#Bir fonksiyon yaz:
#Bir liste içerisindeki kelimelerin uzunluklarını döndürsün.
#Beklenen Çıktı:

#Kelimeler: ['Python', 'Java', 'C++', 'Rust']
#Uzunluklar: [6, 4, 3, 4]

def uzun_bulma(i):
    uzunluk = [len(i) for i in Kelimeler]
    return uzunluk

Kelimeler= ['Python', 'Java', 'C++', 'Rust']

uzunluk = uzun_bulma(Kelimeler)
print(f"Uzunluklar: {uzunluk}")

def uzunluk_bulma2(j):
    liste=[]
    for a in j:
        liste.append(len(a))
    return liste

print(uzunluk_bulma2(Kelimeler))