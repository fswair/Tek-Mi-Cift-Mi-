import time
a = int(input("Sayı-1:"))
b = int(input("Sayı-2:"))
c = int(input("Sayı-3:"))
d = int(input("Sayı-4:"))
e = int(input("Sayı-5:"))
teksayilar = []
ciftsayilar = []
if (a % 2 == 0):
    ciftsayilar.append(a)
elif a % 2 == 1:
    teksayilar.append(a)
if (b % 2 == 0):
    ciftsayilar.append(b)
elif b % 2 == 1:
    teksayilar.append(b)
if (c  % 2 == 0):
    ciftsayilar.append(c)
elif c % 2 == 1:
    teksayilar.append(c)
if (d % 2 == 0):
    ciftsayilar.append(d)
elif d % 2 == 1:
    teksayilar.append(d)
if (e % 2 == 0):
    ciftsayilar.append(e)
elif e % 2 == 1:
    teksayilar.append(e)
print("Çift olma durumları:",ciftsayilar,"Tek olma durumları:",teksayilar)
print("Çift toplamı.:",sum(ciftsayilar),"/","Tek toplamı.:",sum(teksayilar))
time.sleep(50)
