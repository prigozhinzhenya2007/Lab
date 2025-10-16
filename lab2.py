#1.1
def greet(name):
    print("привет,", name)

n11 = str(input())
greet(n11)

#1.2
def square(number):
    print(number**2)

n12 = int(input())
square(n12)

#1.3
def max_of_two(x, y):
    if x > y:
        print(x)
    elif x < y:
        print(y)
    else:
        print("=")

x = int(input())
y = int(input())
max_of_two(x, y)

#2
def describe_person(name, age):
    print("имя -", name, ", возраст -", age)

n2 = str(input())
describe_person(n2, 30)

#3
def is_prime(number):
    c = 0
    for i in range(2, number):
        if number%i == 0:
            c += 1
    if c > 0:
        print("false")
    else:
        print("true")

n3 = int(input())
is_prime(n3)
