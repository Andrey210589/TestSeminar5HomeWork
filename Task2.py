# Задача 28: Вводится десятичное число. 
# Реализовать алгоритм его перевода 
# в двоичную систему счисления через рекурсию. 
# Нельзя использовать функцию bin()


# *Пример:*
#     10
#     *Вывод:*
#     1010

# a=10
# b=""
# while a>0:
#     b = (f"{b} {a%2}")
#     a=a//2
# b=b[::-1]
# print(b)
 
def Convert(a, b):
    if a == 0:
        return b[::-1]
    else:
        b = f"{b}{a%2}"
        return Convert(a//2, b)

a = 10
a = int(input("Input decimal number "))
b = ""
print(f"A decimal number {a} converted to binary form is {Convert(a,b)}")
