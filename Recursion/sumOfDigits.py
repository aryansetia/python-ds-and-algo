def sumOfDigits(n):
    assert n>=0 and int(n) == n, "Please enter a positive integer value!"
    if n==0:
        return 0
    else:
        return int(n%10) + sumOfDigits(n//10)

print(sumOfDigits(123))