def is_prime(x):
    for n in range((x-1),1,-1):
        if x % n == 0:
            return False
            break
    else:
        if x < 2:
            return False
        else:
            return True

number = raw_input("Enter number to check")
print "%s is a prime " % (number), is_prime(int(number))