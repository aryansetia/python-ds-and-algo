def print_list(n):
    for i in range(n): # n
        for j in range(n): # n --> the complexity of these 2 loops will be n*n --> O(n^2)
            print(i,j)

    for k in range(n): # n
        print(k)

print_list(10)

# so here the total time complexity will be O(n^2 + n) but here n is non dominant and n^2 is dominant so we will drop n and 
# the final time complexity will be O(n^2)  