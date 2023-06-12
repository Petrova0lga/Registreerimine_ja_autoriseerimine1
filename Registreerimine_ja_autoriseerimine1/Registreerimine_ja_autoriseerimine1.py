from itertools import filterfalse
from pickle import FALSE
from mymodule import *
l=["user1","user2", "user3"]
p=["Parool1","Parool2","Parool3"]
sisse=str(input("Kas olete juba registreerinud? 0-ei, 1-jah => "))
if sisse=="1":
    while True:
            kasutaja=input("Sisesta kasutajanimi: ")
            if (l==["user1","user2", "user3"]):
                print("Kasutajanimi on õige")
            else:
                print("Kasutajanimi on vale")
            password=input("Sisesta salasõna: ")
            if (p==["Parool1","Parool2","Parool3"]):
                print("Salasõna on õige")
            else:
                print("Salasõna on vale")
print("Olete edukalt sisseloginud!")
if sisse=="0":
    reg=input("Kas soovite registreeruda? 0-ei, 1-jah => ")
if reg=="1":
    kasut=input("Loo kasutajanimi: ")
    parool=input("Kas soovite, et salasõna oli meie poolt välja mõeldud? 0-ei, 1-jah =>")
    if parool=="1":
        sala=salasona(10)
        print("Teie salasõna on ", sala)
        print("Nüüd olete registreerinud!")
    if parool=="0":
        while True:
            parool=input("Sisestage salasõna: ")
            s=list(parool)
            tupper=False
            tdigit=False
            for i in s:
                if(i.isupper()):
                    tupper=True
                if(i.isdigit()):
                    tdigit=True
            if tupper and tdigit: 
                print("Salasõna on korrektne!")
            else:
                print("Liiga lihtne salasõna!")



            
    #    while True:
    #        parool = input("Sisesta parool: ")
    #a=True
    #if len(parool)<10:
    #    a=False
    #    print("Liiga lühike salasõna!")
    #if "123" in parool:
    #    a = False
    #    print("Liiga lihtne salasõna!")
    #if a:
    #    break
if reg=="0":
    print("Head aega!")
