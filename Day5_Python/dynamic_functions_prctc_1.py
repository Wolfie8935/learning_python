def all_positives(numbers):
    new_num = []
    for i in numbers:
        if i < 0:
            return False
        else:
            new_num.append(i)
    
    for i in new_num:
        if i<0:
            return False
        else:
            return True
    
numbers = [-1,0,1]