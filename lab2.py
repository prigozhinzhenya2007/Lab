#1.1
def greet(name):
    return("привет,", name)

n11 = str(input())
print(greet(n11))

#1.2
def square(number):
    return(number**2)

n12 = int(input())
print(square(n12))

#1.3
def max_of_two(x, y):
    if x > y:
        return(x)
    elif x < y:
        return(y)
    else:
        return("=")

x = int(input())
y = int(input())
print(max_of_two(x, y))

#2
def describe_person(name, age):
    return("имя -", name, ", возраст -", age)

n2 = str(input())
print(describe_person(n2, 30))

#3
def is_prime(number):
    c = 0
    for i in range(2, number):
        if number%i == 0:
            c += 1
    if c > 0:
        return("false")
    else:
        return("true")

n3 = int(input())
print(is_prime(n3))