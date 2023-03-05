from collections import Counter
import numpy as np
from prettytable import PrettyTable
import math
import matplotlib.pyplot as plt

lis = [4, 28, 4, 5, 6, 8, 7, 6, 5, 43, 43, 1, 3, 5, 7, 9, 0, 6, 4, 3, 22, 11, 18, 4, 46, 12, 38, 1, 1, 2, 34, 2, 7, 8,
       6, 4, 3, 19, 1, -2, 8, 5, 4, 2, 5, 6, 7, 4, 3, 2, 5, 6, -2, 9, -2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 7, 11, 2, 1, 3, 4,
       5, 6, 5, 4, 3, 2, 7, 8, 4, 12, 12, 2, 3, 32, 22, 23, 9, -3, -1, 7, 3, 5, 7, 8, 6, 4, 3, 5, 8, 9]
lis.sort()
print(lis)
n = int(len(lis))
print("n=", n)
dic = {}
dic = Counter(lis)
list_dic_k = list((dic.keys()))
dic2 = {}
list1 = []
list2 = []
for i in list_dic_k:
    list2.append(dic[i])
################################################
print("---Частотна табличка---")
print("| xi | ni |")
sum = 0
for i in list_dic_k:
    print('|', i, "| ", dic[i], "|")
    sum += dic[i]
    dic2[i] = dic[i]
    list1.append(i)
print("m", sum)
#################################################
print("\n---Функція розподулу F(x)---")
res = 0
fx1 = []
x2 = []
print("| ", 0, "|\t", "x<", list_dic_k[0])
for i in list_dic_k:
    if i != list_dic_k[-1]:
        res += dic[i] / sum
        print("| ", round(res, 3), "|\t", i, "<=x<", i + 1)
    else:
        res += dic[i] / sum
        print("| ", round(res, 3), "|\t", i, "<=x")
    x2.append(i)
    fx1.append(res)
fx1.insert(0, 0)
fx1.insert(0, 0)
x2.append(60)
x2.insert(0, -10)
print("----------------------------")
######################################################
plt.close()
plt.step(x2, fx1, color="g")
plt.savefig("Функція розподілу")
#######################################################
plt.bar(dic2.keys(), dic2.values(), color="g")
plt.savefig("Діаграма частот")
plt.close()
x = dic2.keys()
y = dic2.values()
plt.plot(x, y)
plt.savefig("Полігон частот")
################################################
max_val = max(dic2.values())
for i in list_dic_k:
    if (dic[i] == max_val):
        print("Мода: Mo=", i)
################################################
suma = 0
for i in list_dic_k:
    suma += (i * dic2[i])
arithmetic_mean = (1 / n) * (suma)
print("Середнє арефметичне: X=", arithmetic_mean)
################################################
if (n % 2 != 0):
    middle = int((n / 2))
else:
    middle = int((n / 2))
for i in range(n):
    if i == middle:
        if (n % 2 != 0):
            print("Медіана: Me=", lis[i])
        else:
            print("Медіана: Me=", (lis[i] + lis[i + 1]) / 2)
#################################################
sum = 0
n = int(len(lis))
g = len(list_dic_k)
sub1 = []
sub2 = []
sub3 = []
sub4 = []
div1 = []
div2 = []
div3 = []
div4 = []
start1 = []
start2 = []
start3 = []
start4 = []
deviation = 0
b = len(list_dic_k)
for i in list_dic_k:
    sub = i - arithmetic_mean
    sub1.append(round(sub, 3))
    sub2.append(round(pow(sub, 2), 3))
    sub3.append(round(pow(sub, 3), 3))
    sub4.append(round(pow(sub, 4), 3))
    div1.append(round(pow(sub, 1) * dic[i], 3))
    div2.append(round(pow(sub, 2) * dic[i], 3))
    div3.append(round(pow(sub, 3) * dic[i], 3))
    div4.append(round(pow(sub, 4) * dic[i], 3))
    start1.append(round(pow(i, 1) * dic[i], 3))
    start2.append(round(pow(i, 2) * dic[i], 3))
    start3.append(round(pow(i, 3) * dic[i], 3))
    start4.append(round(pow(i, 4) * dic[i], 3))
for i in range(len(dic)):
    deviation += div2[i]
print("Девіація: ", deviation)
print("___________________________________________________________________________")
p = max(lis) - min(lis)
print("Розмах вибірки: p=", p)
print("Варіанса: s^2=", deviation / (n - 1))
s = math.sqrt(deviation / (n - 1))
print("Стандарт: s=", s)
print("Варіація: v=", s / arithmetic_mean)
print("Десперсія: D=", deviation / n)
print("___________________________________________________________________________")
print("Статестичний момент k-го порядку Mk(a): ")
d1 = 0
d3 = 0
d4 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
for i in range(len(dic)):
    d1 += div1[i]
    d3 += div3[i]
    d4 += div4[i]
    s1 += start1[i]
    s2 += start2[i]
    s3 += start3[i]
    s4 += start4[i]
M1 = d1 / n
M2 = deviation / n
M3 = d3 / n
M4 = d4 / n
m1 = s1 / n
m2 = s2 / n
m3 = s3 / n
m4 = s4 / n
print("Центрального моменту:  M1=", M1, "\tM2=", M2, "\tM3=", M3, "\tM4=", M4)
print("Початкового моменту:  m1=", m1, "\tm2=", m2, "\tm3=", m3, "\tm4=", m4)
print("___________________________________________________________________________")
ac = M3 / pow(M2, (3 / 2))
print("Асиметрія: ", ac)
if ac == 0:
    print("Cтатистичний матеріал семетричний")
elif ac > 0:
    print("Cтатистичний матеріал скошений вправо")
elif ac < 0:
    print("Cтатистичний матеріал скошений вліво")
ec = (M4 / pow(M2, 2)) - 3
print("\nЕксцес: ", ec)
if ec == 0:
    print("Cтатистичний матеріал середньовершинний")
elif ec > 0:
    print("Cтатистичний матеріал високовершинний")
elif ec < 0:
    print("Cтатистичний матеріал низьковершинний")
print("___________________________________________________________________________")
print("-----Квантилі-----")
Q1 = 0
Q2 = 0
Q3 = 0
for i in range(n):
    if i == 25:
        Q1 = lis[i]
    elif i == 50:
        Q2 = lis[i]
    elif i == 75:
        Q3 = lis[i]
print("Квартилі:")
qua = []
for i in range(1, 4):
    if (n % 4) == 0:
        qua.append(int(n * i / 4))

for i in range(len(lis)):
    for j in qua:
        if int(i) == int(j):
            print("Q= ", int(lis[i]))
print("Інтерквартитильні широти: ", Q3 - Q1)
print("Децилі:")
dec = []
for i in range(1, 10):
    if (n % 10) == 0:
        dec.append(int(n * i / 10))
for i in range(len(lis)):
    for j in dec:
        if int(i) == int(j):
            print("D= ", int(lis[i]))
print("Центилі:")
cen = []
for i in range(1, 100):
    if (n % 100) != 0:
        cen.append(int(n * i / 100))
for i in range(len(lis)):
    for j in cen:
        if int(i) == int(j):
            print("C= ", int(lis[i]))
mil = []
for i in range(1, 1000):
    if (n % 1000) != 0:
        mil.append(int(n * i / 1000))
for i in range(len(lis)):
    for j in mil:
        if int(i) == int(j):
            print("M= ", int(lis[i]))
print("___________________________________________________________________________")
table = PrettyTable()
table.add_column("xi", list1)
table.add_column("ni", list2)
table.add_column("xi-xсер", sub1)
table.add_column("(xi-xсер)^1*n", div1)
table.add_column("(xi-0)^1*n", start1)
table.add_column("(xi-xсер)^2", sub2)
table.add_column("(xi-xсер)^2*n", div2)
table.add_column("(xi-0)^2*n", start2)
table.add_column("(xi-xсер)^3", sub3)
table.add_column("(xi-xсер)^3*n", div3)
table.add_column("(xi-0)^3*n", start3)
table.add_column("(xi-xсер)^4", sub4)
table.add_column("(xi-xсер)^4*n", div4)
table.add_column("(xi-0)^4*n", start4)
print(table)
###############################################################################################
print("\n\n--------------------Неперервна величина--------------------\n")
r = 0
for i in range(20):
    if n <= pow(2, i):
        r = i
        break
d = int((p + 1) / r)
print("елем в одному інтервалі d= ", d)
args = [iter(range(lis[0], lis[-1]))] * r
mas = [list(t) for t in list(zip(*args))]
summ = 0
ff = 0
nni = []
zi = []
for k in range(d):
    for j in range(r):
        for i in range(100):
            if mas[k][j] == lis[i]:
                ff = ff + 1
    nni.append(ff)
    ff = 0
for i in range(100):
    if lis[-1] == lis[i]:
        nni[-1] += 1
rew = 0
u = 0
for k in range(d):
    for j in range(r):
        rew += mas[k][j]
        if j == r - 1:
            u += mas[k][j]
    zi.append((rew + u + 1) / (r + 1))
    rew = 0
    u = 0
str1 = []
for k in range(d):
    if (k + 1) != d:
        str1.append(str("[" + str(mas[k][0]) + ";" + str(mas[k][-1] + 1) + ")"))
    else:
        str1.append(str("[" + str(mas[k][0]) + ";" + str(mas[k][-1] + 1) + "]"))
#############################################################
index = 0
max_val = max(nni)
for i in range(len(nni)):
    if nni[i] == max_val:
        index = i
print("Мода: Mo=", zi[index])
##########################################
if (n % 2 != 0):
    middle = int((n / 2))
else:
    middle = int((n / 2))
for i in range(n):
    if i == middle:
        if (n % 2 != 0):
            print("Медіана: Me=", lis[i])
        else:
            print("Медіана: Me=", (lis[i] + lis[i + 1]) / 2)
################################################
suma = 0
for i in range(len(zi)):
    suma += (nni[i] * zi[i])
arithmetic_mean = (1 / n) * (suma)
print("Середнє арефметичне: X=", arithmetic_mean)
################################################
if (n % 2 != 0):
    middle = int((n / 2))
else:
    middle = int((n / 2))
############################################################
sub21 = []
sub22 = []
sub23 = []
sub24 = []
div21 = []
div22 = []
div23 = []
div24 = []
start21 = []
start22 = []
start23 = []
start24 = []
deviation = 0
for i in range(len(zi)):
    sub = zi[i] - arithmetic_mean
    sub21.append(round(sub, 3))
    sub22.append(round(pow(sub, 2), 3))
    sub23.append(round(pow(sub, 3), 3))
    sub24.append(round(pow(sub, 4), 3))
    div21.append(round(pow(sub, 1) * nni[i], 3))
    div22.append(round(pow(sub, 2) * nni[i], 3))
    div23.append(round(pow(sub, 3) * nni[i], 3))
    div24.append(round(pow(sub, 4) * nni[i], 3))
    start21.append(round(pow(zi[i], 1) * nni[i], 3))
    start22.append(round(pow(zi[i], 2) * nni[i], 3))
    start23.append(round(pow(zi[i], 3) * nni[i], 3))
    start24.append(round(pow(zi[i], 4) * nni[i], 3))
for i in range(len(zi)):
    deviation += div22[i]
print("Девіація: ", deviation)
print("___________________________________________________________________________")
p = max(lis) - min(lis)
print("Розмах вибірки: p=", p)
print("Варіанса: s^2=", deviation / (n - 1))
s = math.sqrt(deviation / (n - 1))
print("Стандарт: s=", s)
print("Варіація: v=", s / arithmetic_mean)
print("Десперсія: D=", deviation / n)
print("___________________________________________________________________________")
print("Статестичний момент k-го порядку Mk(a): ")
d1 = 0
d3 = 0
d4 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
for i in range(len(zi)):
    d1 += div21[i]
    d3 += div23[i]
    d4 += div24[i]
    s1 += start21[i]
    s2 += start22[i]
    s3 += start23[i]
    s4 += start24[i]
M1 = d1 / n
M2 = deviation / n
M3 = d3 / n
M4 = d4 / n
m1 = s1 / n
m2 = s2 / n
m3 = s3 / n
m4 = s4 / n
print("Центрального моменту:  M1=", M1, "\tM2=", M2, "\tM3=", M3, "\tM4=", M4)
print("Початкового моменту:  m1=", m1, "\tm2=", m2, "\tm3=", m3, "\tm4=", m4)
print("___________________________________________________________________________")
ac = M3 / pow(M2, (3 / 2))
print("Асиметрія: ", ac)
if ac == 0:
    print("Cтатистичний матеріал семетричний")
elif ac > 0:
    print("Cтатистичний матеріал скошений вправо")
elif ac < 0:
    print("Cтатистичний матеріал скошений вліво")
ec = (M4 / pow(M2, 2)) - 3
print("\nЕксцес: ", ec)
if ec == 0:
    print("Cтатистичний матеріал середньовершинний")
elif ec > 0:
    print("Cтатистичний матеріал високовершинний")
elif ec < 0:
    print("Cтатистичний матеріал низьковершинний")
print("___________________________________________________________________________")
print("-----Квантилі-----")
Q1 = 0
Q2 = 0
Q3 = 0
for i in range(n):
    if i == 25:
        Q1 = lis[i]
    elif i == 50:
        Q2 = lis[i]
    elif i == 75:
        Q3 = lis[i]
print("Квартилі:")
qua = []
for i in range(1, 4):
    if (n % 4) == 0:
        qua.append(int(n * i / 4))
for i in range(len(lis)):
    for j in qua:
        if int(i) == int(j):
            print("Q= ", int(lis[i]))
print("Інтерквартитильні широти: ", Q3 - Q1)
print("Децилі:")
dec = []
for i in range(1, 10):
    if (n % 10) == 0:
        dec.append(int(n * i / 10))

for i in range(len(lis)):
    for j in dec:
        if int(i) == int(j):
            print("D= ", int(lis[i]))
print("Центилі:")
cen = []
for i in range(1, 100):
    if (n % 100) == 0:
        cen.append(int(n * i / 100))
for i in range(len(lis)):
    for j in cen:
        if int(i) == int(j):
            print("C= ", int(lis[i]))
mil = []
for i in range(1, 1000):
    if (n % 1000) == 0:
        mil.append(int(n * i / 1000))
for i in range(len(lis)):
    for j in mil:
        if int(i) == int(j):
            print("M= ", int(lis[i]))
print("___________________________________________________________________________")
#############################################################
table2 = PrettyTable()
table2.add_column("[x1;x(i+1)]", str1)
table2.add_column("ni", nni)
table2.add_column("zi", zi)
table2.add_column("zi-xсер", sub21)
table2.add_column("(zi-xсер)^1*n", div21)
table2.add_column("(zi-0)^1*n", start21)
table2.add_column("(zi-xсер)^2", sub22)
table2.add_column("(zi-xсер)^2*n", div22)
table2.add_column("(zi-0)^2*n", start22)
table2.add_column("(zi-xсер)^3", sub23)
table2.add_column("(zi-xсер)^3*n", div23)
table2.add_column("(zi-0)^3*n", start23)
table2.add_column("(zi-xсер)^4", sub24)
table2.add_column("(zi-xсер)^4*n", div24)
table2.add_column("(zi-0)^4*n", start24)
print(table2)
############################################################
#################################################
print("\n---Функція розподулу F(x)---")
res = 0
sum = 100
print("| ", 0, "|\t", "x<", zi[0])
dicn = {}
for i in range(len(zi)):
    key = zi[i]
    value = nni[i]
    dicn[key] = (value)
fx = []
fx.append(0)
notcor = zi[0]
for i in zi:
    if i != notcor:
        print(i)
    if i != zi[-1]:
        res += dicn[i] / sum
        print("| ", round(res, 3), "|\t", i, "<=x<", end=" ")
    else:
        res += dicn[i] / sum
        print("| ", round(res, 3), "|\t", i, "<=x")
    fx.append(res)
print("----------------------------")
#######################################################
plt.close()
plt.bar(zi, nni, color="g", width=6)
plt.savefig("Гістограма")
############################################################
plt.close()
plt.bar(zi, nni, color="r")
plt.savefig("Діаграма частотдля (для неперервної)")
############################################################
plt.close()
x = zi
y = nni
plt.plot(x, y)
plt.savefig("Полігон частот(для неперервної)")
#####################################
fx.insert(0, 0)
zi.append(60)
zi.insert(0, -10)
plt.close()
plt.step(zi, fx, color="g")
plt.savefig("Функція розподілу (для неперервної)")
