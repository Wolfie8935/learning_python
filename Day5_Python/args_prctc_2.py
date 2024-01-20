def absolute_sum(*args):
    s=0
    for i in args:
        s+=abs(i)
    return s

print(absolute_sum(2,3,5,-7))