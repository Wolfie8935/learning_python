def count_even(numbers):
    count=0
    for i in numbers:
        if i%2==0:
            count+=1
    return count
    
numbers=[1,3,5,7,8,9,7,6,5]