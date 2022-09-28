#!/usr/bin/env python3

def print_hi(name):
    print(f'Hi, {name}')

import math
def distance(p1, p2):
    # d=√((x_2-x_1)²+(y_2-y_1)²)
    #NEM JO ERTEKET AD VISSZA
    # TODO...
    d = math.sqrt(((p1[1]-p1[0])*(p1[1]-p1[0]))+((p2[1]-p2[0])*(p2[1]-p2[0])))
    return d

def get_movie_info():
    #adat lekerese egy adatbazisbol
    return ("Total Recall", 1990, 7.5)

#############################################################
def main():

    for i in range(5):
        print("B")

    li1 = list(range(22,37))
    li2 = list(range(45,32,-1))

## STRINGBUFFER ERTELME ES ALKALMAZASA
##naiv megkozelites:
## koltseges mert egy annyi resz stringet hoz letre ahanyszor lefut = koltseges minden teren (memoria, szamitasi kapacitas)
res = ""
for i in range(1,15+1):
    res += str(i)

print(res)

##stringbuffer
##letrehoz egy tombot amibe elkezdi osszegyujteni, majd ezt konkatanalja egy string-e
parts = []

for i in range(1,15+1):
    parts.append(str(i))

res = "".join(parts)
print(res)

t = (3, 7, 2, 9)

print(t[0])

t = (True, 3.14, 42)

print(t[0])

## 1 elemu tuple-nel kell a vesszo!!!
single = ("hi",) ##<---------- VESSZO
print(type(single))
print(single)


##elhagyhato a zarojel pl: x, y = 3, 5 DE ezt nem kell hasznalni
(x, y) = (3, 5)

print(x)
print(y)

x, y = y, x
print(x)
print(y)

pont = (1, 2)
point = (6, 5)
print('A ket pont kozti tavolsag:', distance(pont, point))


t = get_movie_info()
title = t[0]
date = t[1]
imdb = t[2]
print(title, date, imdb)

title, date, imdb = get_movie_info()
print(title, date, imdb)

#########LIST COMPREHENSION
nums = [1, 2, 3, 4]
squares = [n*n for n in nums]
print(squares)

##altalanosan: [expr for var in list]

##opcionalisan if is lehet benne
nums = [8, 3, 2, 1, 5, 9, 2]
small = [n for n in nums if n <=2]
print(small)

##EXERCIZING

######1

li = ['auto', 'villamos', 'metro']
result = [s.upper()+'!' for s in li]
print(result)

######2

li = ['aladar', 'bela', 'cecil']
result = [s.capitalize() for s in li]
print(result)

######3

li = [0 for i in range(10)]
print(li)

######4

li = list(range(1, 10+1))
result = [n*2 for n in li]
print(result)
li = list(range(2, 20+1, 2))
print(li)

######5

li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
result = [int(s) for s in li]
print(result)

######6

li = "1234567"
result = [int(s) for s in li]
print(result)

######7

li = 'The quick brown fox jumps over the lazy dog'
result = [len(s) for s in li.split()]
print(result)

######8

li = "python is an awesome language"
result = [s[0] for s in li.split()]
print(result)

######9

li = 'The quick brown fox jumps over the lazy dog'
result = [(s, len(s)) for s in li.split()]
print(result)

######10

li = list(range(0, 10, 2))
print(li)

######11

li = list(range(20))
result = [n*n for n in li if n*n % 2 == 0]
print(result)

######12

li = list(range(20))
result = [n*n for n in li if (repr(n*n)[-1:] == '4')]
print(result)

######13

li = [chr(n).capitalize() for n in list(range(65, 91))]
parts = []
for i in range(len(li)):
    parts.append(li[i])

result = "".join(parts)
print(result)

######14

li = [' apple ', ' banana ', ' kiwi']
result = [s.strip() for s in li]
print(result)

######15

li = [1, 0, 1, 1, 0, 1, 0, 0]
parts = []
for i in range(len(li)):
    parts.append(str(li[i]))

result = "".join(parts)
print(result)
print(type(result))

#########LIST COMPREHENSION ENDS



#############################################################
if __name__ == '__main__':
    print_hi('PyCharm')
