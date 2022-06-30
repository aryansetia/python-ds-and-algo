def print_list(n):
    for i in range(n): # n
        for j in range(n): # n
            print(i,j)


print_list(10)

# here we are running loop inside a loop, so time complexity we get multiplied --> n*n = O(n^2)
# if we put the third loop inside the 2nd the time complexity will be O(n^3) but we write everything above O(n^2) as O(n^2) only.