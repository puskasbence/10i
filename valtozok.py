from pickle import FALSE, TRUE
from tkinter import E


szam=12
print(szam)
szam=szam+6
print(szam)
szam = szam * szam
print(szam)
szam=1
szam = szam +1
print(szam)
szam  +=1  # szam++ 
print(szam)

szam  +=10  
print(szam)

szam  -=1  # szam--
print(szam)

szam  *=10  
print(szam, type(szam))
szam  /=10  
print(szam, type(szam))

szam="szam"
print(szam, type(szam))


szam=TRUE
print(szam, type(szam))
szam=True
print(szam, type(szam))

szam=FALSE
print(szam, type(szam))
szam=False
print(szam, type(szam))

print(1 == 1)
print(1 == 2)

szam=True
print(szam == TRUE)
print(szam == True)

szam=(1,2,3)
print(szam,type(szam))

lista=[1,2,3]
print(lista,type(lista))

halmaz={ 1,2,3 }
print(halmaz,type(halmaz))


a,b = 1,2

print(a)
print(b)

# a,b=12 hibás
a,b = 12,44
print("a = ",a,", b = ",b)
print("a = ",a,", b = ",b,sep="")
print("a=",a,", b=",b,sep="")

szoveg="Szia"
nev="Pista"
koszones= szoveg+" "+nev
print(koszones)

koszones= szoveg+" "+nev+"!"
print(koszones)

print('-'*32)
koszones= szoveg+" "+nev+"!"*3
print(koszones)
print('-'*32)

koszones= (szoveg+" ")*5+" "+nev+"!"*3
print(koszones)

szam=12
# print(szoveg+szam) hiba
print(szoveg*szam)

# print(szoveg/szam) hiba
# print(szoveg-szam)

#print(szoveg*koszones)

szam=2
print(szoveg*szam)
print(szam*szoveg)


egesz=12
print("egész: ", egesz)
tort =1.2

#szam=float(input("Kérek egy számot"))
szam=int(input("Kérek egy számot"))
szerencse=szam+1
