"""
Karakter Frekansı
Kullanıcıdan bir cümle alın ve her harfin kaç kez geçtiğini gösteren bir sözlük döndürün.
Beklenen Çıktı:

Girdi: "merhaba"
Çıktı: {"m": 1, "e": 1, "r": 1, "h": 1, "a": 2, "b": 1}
"""

#Basit Bir Şifreleme Algoritması
#Bir fonksiyon yaz:
#Kullanıcıdan bir metin al.
#Metindeki her harfi bir sonraki harfe çevirir (ör. 'a' -> 'b', 'z' -> 'a').
#Sayılar ve özel karakterler değişmeden bırak.
#Beklenen Çıktı:

#Metni girin: python
#Şifrelenmiş metin: qzuipo


#change = ord("q") + 1
#print(chr(change))

#charac ="Z"
#print(if charac == "Z": # If Z encountered change to A
 #  print(chr(ord(charac)-25))

#print(charac.isalpha())



def harf_frekansi(metin):
   frekans = {}
   for a in metin:
       if a.isalpha():
               if a in frekans:
                frekans[a] += 1
               else:
                frekans[a] = 1
   return frekans


print(harf_frekansi("merhaba"))
