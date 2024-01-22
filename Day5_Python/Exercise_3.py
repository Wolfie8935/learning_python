# Write a function that requires an indefinite number of
# arguments. What this function must do is return True if at any
# time the number zero has been entered twice consecutively.
# For example:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def check(*args):
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False

print(check(5,6,1,0,9,0,3,5))
