def split_list(list_):
    sep = len(list_)
    list_.sort(key = lambda x:x%2)
    for i in range(len(list_)):
        if list_[i]&1 == 1:
            sep = i
            break
    even = list_[:sep]
    list_ = list_[sep:]
    return even,list_


if __name__ == '__main__':
    ele = int(input('Enter the number of element in list'))
    a = []
    for i in range(ele):
        a.append(int(input()))
    even,odd = split_list(a)
    print('even :')
    for i in range(len(even)):
        print(even[i],end = " ")
    print("\n Odd:")
    for i in range(len(odd)):
        print(odd[i],end = " ")