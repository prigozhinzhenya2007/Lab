#1
def f1(m):
    with open('example.txt', 'r') as file:
        if m == 0:
            content = file.read()
            print(content)
        elif m == 1:
            for line in file:
                print(line)

print("0 - чтение всего файла | 1 - построчное чтение файла")
n = int(input())
f1(n)

#2
with open('user_input', 'a') as file:
    text = input()
    file.write('\n' + text)

#3
def f2(m)
    try:
        with open('example.txt', 'r') as file:
            if m == 0:
                content = file.read()
                print(content)
            elif m == 1:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print("файл не найден")

print("0 - чтение всего файла | 1 - построчное чтение файла")
n = int(input())
f2(n)
