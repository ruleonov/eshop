from random import randint

def toss(n):
    log0 = 0
    log1 = 0
    for i in range(n):
        x = randint(0,1)
        if x == 0:
            log0 += 1
        else:
            log1 += 1
    return log0, log1

print(toss(100))