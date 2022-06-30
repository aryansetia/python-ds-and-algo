def power(n,p):
    assert n >= 0 and int(n) == n and int(p) == p,"Please enter integer values in parameters!"
    if p<=0:
        return 1
    else:
        return n * power(n,p-1)

print(power(5,2))