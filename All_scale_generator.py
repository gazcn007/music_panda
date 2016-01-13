from itertools import product
#correctOrder if true returns 1
def correctOrder(project):
	if (not(project[6]=='#' and project[0]=='b')) and (not(project[2]=='#' and project[3]=='b')):
		return 1;
	else:
		return 0;

#sameNote returns true if no same note happens
def noSameNote(project):
	checker=1;
	for i in range(0,7):
		if i==2:
			if project[i]=='#' and project[i+1]!='#':
				checker=0;
				break;
			elif project[i]=='0' and project[i+1]=='b':
				checker=0;
				break;
		elif i==6:
			if project[i]=='#' and project[0]!='#':
				checker=0;
				break;
			elif project[i]=='0' and project[0]=='b':
				checker=0;
				break;
		else:
			if project[i]=='#' and project[i+1]=="b":
				checker=0;
				break;
	return checker;
#this mapFunction maps a string of sharp/natural/flats to certain value among 1-12
def mapFunction(project):
	array=[]
	for i in range(0,7):
		if i<3:
			if project[i]=='0':
				array.append(int(i*2+1))
			if project[i]=='#':
				array.append(int(i*2+2))
			if project[i]=="b":
				array.append(int(i*2))
		elif i>=3:
			if project[i]=='0':
				array.append(int(i*2))
			if project[i]=='#':
				array.append(int(i*2+1))
			if project[i]=="b":
				array.append(int(i*2-1))
	return array
#given an array, finds the interval between each element	
def intervalArray(array):
	array1=''
	for i in range(0,6):
		array1=array1+str(array[i+1]-array[i])
	array1=array1+str((array[0])+12-(array[6]))
	return array1

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


#check for rotation
def ifrotate(a,b):
	a=a+a;
	if b in a:
		return 1
	else:
		return 0


bigArray=['']
def output_correctOrder_and_noSameNote():
	incrementer=0;
	count=0;
	count1=0;
	count2=0;
	for project in [''.join(i) for i in product("#0b",repeat=7)]:
		print project
		incrementer+=1;
		if correctOrder(project)==1:
			count=count+1;
		if noSameNote(project)==1:
			count1=count1+1;
			bigArray.append(intervalArray(mapFunction(project)))
		#print intervalArray(mapFunction(project))
	print count1
	print count


def output_transpositionable_scales(bigArray):
	transpositionCount=[];
	temp=[]
	i=1
	while (i<len(bigArray)):
		x=i+1
		count=1
		while (x<len(bigArray)):
			if ifrotate(bigArray[i],bigArray[x])==1:
				count+=1
				bigArray.pop(x)
				x-=1
			x+=1
		i+=1
		transpositionCount.append(count)
		
