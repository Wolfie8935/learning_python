from random import *

def throw_dice():
    dice_1 = randint(1,6)
    dice_2 = randint(1,6)
    return dice_1, dice_2
    
def roll_result(dice_1,dice_2):
    if dice_1+dice_2 <= 6:
        return "The sum of your dice is {}. Unfortunate".format(dice_1+dice_2)
    elif dice_1+dice_2 >6 and dice_1+dice_2<10:
        return "The sum of your dice is {}. You have a good chance".format(dice_1+dice_2)
    else:
        return "The sum of your dice is {}. It looks like a winning roll".format(dice_1+dice_2)

num1, num2 = throw_dice()
res = roll_result(num1, num2)
print(res)