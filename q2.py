def split_charater(string):
    string = list(string)
    lower_chr = []
    upper_chr = []
    for i in string:
        if ord(i) in range(65,91):
             upper_chr.append(i)
        else:
            lower_chr.append(i)
    string = lower_chr + upper_chr
    return "".join(string)


if __name__ == '__main__':

    string = input('Enter  string')
    print(split_charater(string))