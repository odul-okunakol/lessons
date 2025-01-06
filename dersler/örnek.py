import math

liste=[1,2,3,4,5]

def sayi(liste):
    cifsayilar=[]
    for sayi in liste:
        if sayi %2==0:
            cifsayilar.append(sayi)
    return cifsayilar

cifler= list(filter(lambda x: x%2==0 ,liste))


karesi=list(map(lambda x:int(math.pow(x,2)),liste))
print(karesi)



