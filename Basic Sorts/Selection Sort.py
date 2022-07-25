def selection_sort(arr):
	for i in range(len(arr)-1): #for(int i=0; i<n-1; i++)
		min_index = i
		for j in range(i+1, len(arr)):
		  	if arr[j] < arr[min_index]:
		  		min_index = j
		if i != min_index:
			arr[i], arr[min_index] = arr[min_index], arr[i]

	return arr


print(selection_sort([4,10,6,5,1,3]))		

