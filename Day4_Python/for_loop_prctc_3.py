list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for i in list_numbers:
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(sum_even)
print(sum_odd)