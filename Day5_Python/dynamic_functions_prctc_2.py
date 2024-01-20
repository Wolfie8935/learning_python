def sum_less(numbers):
    sum=0
    for i in numbers:
        if i>0 and i<1000:
            sum+=i
        else:
            continue
    
    return sum

numbers=[-9,8,787,444,34567,78]