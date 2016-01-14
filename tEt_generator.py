from itertools import product,combinations
# interval vector calculator, input: a string of 1/0, 
# output:
# a array of length n-tEt, 
# each index i+1 is the interval name, i.e array [0]=3 means there are 3 1-intervals
# element at each index is number of intervals that appears in the set(the Input String in this case)
def interval_vector_calc(bracelet):
	array=[0 for i in range(len(bracelet)/2+1)]
	a=bracelet+bracelet
	for i in range (0,len(bracelet)):
		for y in range(i+1,i+6):
			if bracelet[i]==a[y] and bracelet[i]=='1':
				array[y-i-1]+=1
	return array

#this gets you the prime set,
#but this works when you have an input bracelet, that is ALREADY LEFT_PACKED by output-all-permutation and inversions_cancelation
def prime_set(bracelet):
	a=bracelet+bracelet
	#array to return
	array=[0]
	count=0
	for i in range(1,len(bracelet)):
		if bracelet[i]=='1':
			array.append(i)
	return array

# main generator,
# input: numOf of equal temperament and cardinality
# output: array of set classes of the cardinality within the temperament
def tEt_generator(numOf_tEt,cardinality):
	#array to return
	array=[[]]
	#temp for temporary usage
	temp=[]
	for x in range(1,numOf_tEt):
		print

#check for rotation
def ifrotate(a,b):
	a=a+a;
	if b in a:
		return 1
	else:
		return 0

#cancel existent inversions/ bracelets that are in rotation with existed bracelet
def inversions_cancelation(array):
	bigArray=array
	i=0
	while (i<len(bigArray)):
		x=i+1
		while (x<len(bigArray)):
			if ifrotate(bigArray[i],bigArray[x])==1:
				bigArray.pop(x)
				x-=1
			x+=1
		i+=1
	return bigArray

# random brutal force print function to play around
def output_all_permutation(numOf_tEt,cardinality):
	array=[]
	string=''.join(str(i) for i in range(numOf_tEt))
	for project in [''.join(i) for i in combinations(string, cardinality)]:
		temp=[0 for i in range(numOf_tEt)]
		for i in range(len(project)):
			temp[int(project[i])]='1'
		array.append(''.join(str(temp[i]) for i in range(len(temp))))
	print (array)
	print (inversions_cancelation(array))
	set_of_interval_vector=[]
	set_of_prime_set=[]
	for project in inversions_cancelation(array):
		set_of_interval_vector.append(interval_vector_calc(project))
		set_of_prime_set.append(prime_set(project))
	print (set_of_prime_set)
	print (set_of_interval_vector)
output_all_permutation(12,5)
