# O(1) is also called the constant as it takes constant time and it is most efficient Big O

def add_items(n):
    return n+n
    # here the value of n could be in millions but the operation we are performing that is addition (+) is a single operation 
    # so the time complexity in this case will be O(1)
    # n + n + n --> same with this case it would not be O(2) but O(1)

print(add_items(10))