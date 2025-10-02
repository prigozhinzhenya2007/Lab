#4/дз
#№1
n = int(input())
for i in range(1, n+1):
    print(i)

#№2
n1 = int(input("Введите первое число:"))
n2 = int(input("Введите второе число:"))
if n1 > n2:
    print("Большее число:", n1)
elif n2 > n1:
    print("Большее число:", n2)
else:
    print("Числа равны")