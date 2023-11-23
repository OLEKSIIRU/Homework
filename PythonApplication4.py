from math import * #matematelised funktsionid

print("Hi stranger!") #Ülesanne 1

print(input(3+8/(4-2)*4))#Ülesanne 2
print(input(3+8/4-2*4))# Без скобок
print(input((3+8)/(4-2)*4))# Каждое действте в скобках

print(input((3+3)**2))# Площадь квадрата
print(input((3+3)*4))# периметр квадрата
print(input((pi*3)**2))# площадь курга
print(input((pi*3)*2))# длина окружности

a=float(6378e+9)
b=float(25.75)
print(input(((2*3.14*a))/b))#окружность земли по экватору в монетах


print("kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll") #Ülesanne 3

print("Поезд ехал тух-тьфу,")
print("подглядывающая утка была машинистом поезда.")
print("Колеса сделали колесо тат таа,")
print("колесо тат таа и тат тат таа.")
print("Но там, в поезде,")
print("ты знаешь, кто там был?")

print("Поезд шел «тук-тук»,")
print("подглядывающая утка была машинистом.")
print("Колеса пошли: убей колл колл,")
print("убей колл колл и убей колл убей.")

a=input("Длина стороны А прямоугольника")
b=input("Длина стороны B прямоугольника")
print((a+b)*2)

A=input("Кол-во залитого топлива")
B=input("Пройденные километры")
print("Средний раскход топлива на 100км"+(B/(A/100)))

Ф=29.9
print("Путь который проходит конькобежец за минуту"+Ф*16.655)

Т = int(input("Введите время в минутах: "))
часы = Т//60
минуты = Т%60
print(f"Время: {часы}:{минуты:02d}")
