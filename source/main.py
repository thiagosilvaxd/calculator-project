a = input("+ or - or * or / ")

b = input('Digite um número: ')

c = input('Digite outro número: ')

if a == '+':
    print(float(b) + float(c))
elif a == '-':
    print(float(b) - float(c))
elif a == '*':
    print(float(b) * float(c))
elif a == '/':
    print(float(b) / float(c))
