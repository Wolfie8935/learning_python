name = "Beth"

def personal_numbers(name,*args):
    sum_numbers = sum(args)
    return "{}, the sum of your numbers is {}".format(name,sum_numbers)
    
print(personal_numbers(name,1,2,3,4,55))