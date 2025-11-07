import math
import datetime
import my_module

#1
num = int(input())
print(math.sqrt(num))
print(datetime.datetime.now())

#2, 3
n1 = int(input())
n2 = int(input())
print(my_module.plus(n1, n2), my_module.minus(n1, n2), my_module.multiply(n1, n2), my_module.divide(n1, n2))
