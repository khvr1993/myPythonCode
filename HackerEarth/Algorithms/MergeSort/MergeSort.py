def Merge(array1 :list ,array2 : list,arr1 : list) -> list:
	"""Merge combines 2 sorted arrays and
	returns a sorted array.
	1. Initiatlise 3 variables i,j,k = 0
	2. Compare Array[i] with Array[j]. Which ever is less append to NewArray and increment k
	3. If A[i] is less increment i and if A[j] is less increment j. In both cases increment j
	4. Carry this on as long as i and j are less than the respective lengths passed
	5. After that insert the remaining elements and return the array
	"""
	print(f"Merge Called with Sorting array1  {array1} and array2 is {array2} with input array {arr}")
	len_array1 = len(array1)
	len_array2 = len(array2)

	i,j,k = 0,0,0

	while (i< len_array1) and (j<len_array2):
		# print(f"Value of i is {i} and j is {j} and arrray values are {array1[i]} and {array2[j]} and k is {k} ")

		# compare the respective elements
		if array1[i] <= array2[j]:
			# insert into sorted array
			# increment i
			arr1[k] = array1[i]
			i += 1
		else:
			arr1[k] = array2[j]
			j += 1
		k += 1

	# print(f"Before inserting the remaining values Value of i is {i} and j is {j} and k is {k}")

	# insert the remaining elements from array 1
	for index in range(i,len_array1):
		# From the value of k insert into the aray
		arr1[k]= array1[index]
		k += 1

	# insert the remaining elements from array 2
	for index in range(j,len_array2):
		# From the value of k insert into the aray
		arr1[k]= array2[index]
		k += 1
	print(arr1)


def MergeSort(arr1,low,high):
	"""Merge Sort recursively calls the
		MergeSort and  sorts the array
		DIVIDE AND CONQUER
		1. divide the array into smaller problems until you reach element of size.
		2. Element of size 1 is always sorted.
		3. When you reach element of Size 1 call the Merge function
	"""
	if len(arr1) > 1:
		mid = int(len(arr1)/2)
		print(f"Merge Sort called with parameters arr1 {arr1} , low  {low}  high {high}")
		print(f"low = {low} high = {high} mid = {mid}")
		L = arr1[:mid]
		H = arr1[mid:]
		print(f"Left Hand Array {L} Right Hand Array {H}")

		MergeSort(L,low,mid)
		MergeSort(H,mid,high)
		Merge(L,H,arr1) # in python a[0:0] is returning empty array


arr = [12, 15, 13, 5, 6, 7]
MergeSort(arr,0,len(arr))
print(arr)
