def print_list(n):
    for i in range(n): #time complextity is O(n)
        print(i)

    for j in range(n): #time complextity is O(n)
        print(j)

print_list(10)

# n + n = 2n --> O(2n)
# But the rules says we have to drop the constant... so the time compelxity will be O(n)