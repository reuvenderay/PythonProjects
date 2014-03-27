__author__ = 'Reuven'
def is_prime(x):
    # checks if a number is prime
    #returns True if yes and False if not
    if x <= 1:
        return False
    else:
        flag = 1
        for num in range(2, x):
           if x % num == 0:
            flag += 1
        if flag == 1:
            return True
        else:
            return False

print filter(lambda x: is_prime(x) == True, range(-1000, 1000))