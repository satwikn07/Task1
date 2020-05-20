def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def default():
    return "wrong input"

if __name__ == '__main__':
    a = int(input('enter first number'))
    b = int(input('enter second number'))
    op = int(input('operation:\n1:add\n2:subtract\n3:multiply\n4:divide\n'))
    if op not in range(0,5):
        print(default())
    elif op == 1:
        print(add(a,b))
    elif op == 2:
        print(sub(a,b))
    elif op == 3:
        print(multiply(a,b))
    elif op == 4:
        print(divide(a,b))


