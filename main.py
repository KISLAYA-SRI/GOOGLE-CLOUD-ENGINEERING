from flask import Flask, request, jsonify

app = Flask(__name__)

# Function 'hello_world' which is the entry point in the code
def hello_world(request) : 

	# Extracting the json payload using get_json() method
	array = request.get_json()
	
	# Extracting both the arrays 
	arr1 = array['a']
	arr2 = array['b']
	
	# Calling mergeArray function to sort, merge and return the resultant array
	arr3 = mergeArray(arr1, arr2)
	js = { "c" : arr3 }
	
	# jsonify function will convert the array in json format
	return jsonify(js)
	
	
def mergeArray(arr1, arr2) :
	
	# First sorting both the array individually and then merging them using 
	# 'Merge Sort' algorthim to reduce the time complexity of the overall process.
	arr1.sort()
	arr2.sort()
	n1 = len(arr1)
	n2 = len(arr2)
	
	# Declaring an empty array of size equal to the sum of sizes of both the arrays.
	arr3 = [None] * (n1 + n2)
	i=0
	j=0
	k=0
	
	# Running loop to traverse both the arrays 
	while i < n1 and j < n2 :
	
		# Checking if current element of first array is smaller than current 
		# element of second array.
		if arr1[i] < arr2[j] :
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else :
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	
	# Storing remaining elements of first array.
	while i < n1 :
		arr3[k] = arr1[i]
		k = k + 1
		i = i + 1
		
	# Storing remaining elements of second array.
	while j < n2 :
		arr3[k] = arr2[j]
		k = k + 1
		j = j + 1
		
	return arr3
