def reduce_list(numbers):
    new_list = list(set(numbers))
    max = 0
    for i in new_list:
        if max<i:
            max = i
        else:
            continue
    new_list.remove(max)
    return new_list

def average(list):
    sum = 0
    for i in list:
        sum += i
    
    avrg = float(sum/len(list))
    return avrg
    
numbers = [1,2,15,7,2]
new_numbers = reduce_list(numbers)
avg = average(new_numbers)
print(avg)