def outer2(sum):
    return sum + 5
def outer1(a,b):
    def inner(a,b):
        a += b
        x = outer2(a)
        return x
    final_ = inner(a,b)
    return final_

if __name__ == '__main__':
    a = int(input('Enter 1st number'))
    b = int(input('Enter 2nd number'))
    print(outer1(a,b))
