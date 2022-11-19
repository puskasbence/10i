'''  végtelen ciklus
while True:
    print("ismét")
    print("2. sor")
print("ciklus után")
'''

from tkinter import E


while False:
    print("ismét")
print("ciklus után")

folytat=True
folytat=False
while folytat:
    valasz=input("Folytatod ? (i/n)")
    if valasz == 'i':
        folytat=True
    else:
        folytat=False

ciklusValtozo=0
while ciklusValtozo < 10:
    print(ciklusValtozo,end=" ")
    ciklusValtozo +=1
print()
...
...
print("ciklus után")

#print("\nciklus után")

ciklusValtozo=1
while ciklusValtozo < 11:
    print(ciklusValtozo,ciklusValtozo**2,sep="\t")
    ciklusValtozo +=1
print()
print("ciklus után")


ciklusValtozo=100
while ciklusValtozo >=50 :
    print(ciklusValtozo,end=",")
    ciklusValtozo -=2
print('\b','\b')
print("ciklus után")



a1=1
a2=1
a3=1
while a3 < 1000:
    a3=a1+a2
    a1=a2
    a2=a3
    print(a3,end="\n")

x=1/7
while x < 1:
    x = x + 1/7
    print(x)





