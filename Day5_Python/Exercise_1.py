# Create a function called return_distincts() that receives 3
# integers as parameters.
# If the sum of the 3 numbers is greater than 15, it must return
# the highest number.
# If the sum of the 3 numbers is less than 10, it must return the
# lowest number.
# If the sum of the 3 numbers is a value between 10 and 15
# (included), then it must return the number with the
# intermediate value.


def return_distincts(num1,num2,num3):
    num_sum = num1+num2+num3
    if num_sum>15:
        if num1>=num2 and num1>=num3:
            return num1
        elif num2>=num1 and num2>=num3:
            return num2
        else:
            return num3
    elif num_sum<10:
        if num1<=num2 and num1<=num3:
            return num1
        elif num2<=num1 and num2<=num3:
            return num2
        else:
            return num3
    else:
        k=[num1,num2,num3]
        k.sort()
        return k[1]

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
print(return_distincts(num1,num2,num3))