#1
with open('example.txt', 'r') as file:
    print("0 - чтение всего файла | 1 - построчное чтение файла")
    m = int(input())
    if m == 0:
        content = file.read()
        print(content)
    elif m == 1:
        for line in file:
            print(line)

#2
with open('user_input', 'a') as file:
    text = input()
    file.write('\n' + text)

#3
try:
    with open('example.txt', 'r') as file:
        print("0 - чтение всего файла | 1 - построчное чтение файла")
        m = int(input())
        if m == 0:
            content = file.read()
            print(content)
        elif m == 1:
            for line in file:
                print(line)
except FileNotFoundError:
    print("файл не найден")
