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



def sifreleme(metin):
   sifrelenmis_metin=""
   for a in metin:
       if a.isalpha():
           if a=="z":
               sifrelenmis_metin+=chr(ord(a) - 25)
           else:
               sifrelenmis_metin+=chr(ord(a) + 1)
       else:
          sifrelenmis_metin+= a
   return sifrelenmis_metin


print(sifreleme("deniz#"))
