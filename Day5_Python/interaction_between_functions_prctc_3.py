from random import *

secret_codes = [1,4,2,3,6,7,1]

def toss_coin():
    toss = randint(1,2)
    if toss == 1:
        return "Heads"
    else:
        return "Tails"
        
def luck(toss, secret_codes):
    if toss == "Tails":
        print("List will self-destruct")
        secret_codes = []
        return secret_codes
    else:
        print("List was saved")
        return secret_codes
        

toss = toss_coin()
ans = luck(toss,secret_codes)