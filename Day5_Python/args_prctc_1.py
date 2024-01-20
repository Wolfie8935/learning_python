def sum_squares(*args):
    k=0
    for i in args:
       k+=i**2
    
    return k

ans = sum_squares(1,2,3,4,5,6,7,8)
print(ans)