# SHORTCUT METHOD
# def min_value(sample):
#     return(min(sample.values()))

# METHOD 2
def min_value(sample):
    min_ = float('inf')
    for key in sample.keys():
        if sample[key] < min_:
            min_ = sample[key]
    return min_




if __name__ == '__main__':
    sample = {'physics':88,
              'maths':75,
              'chemistry':72,
              'basic_electrical':89}
    print(min_value(sample))





