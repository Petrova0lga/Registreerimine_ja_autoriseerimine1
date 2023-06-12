from math import *
from random import *
from re import T

import string

login=[]
password=[]
def salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    return sala


def isesalasona (sona):
    s=list(sona)
    tupper=False
    tdigit=False
    for i in s:
        if i.isupper():
            tupper=True
        if i.isdigit():
            tdigit=True
    if tupper==True and tdigit==True and len(s)>5:
        print("Sinu salasona :", sona)
    else:
        print("Teie salasona on liiga nõrk, kirjutage üks ülemine täht ja number")
