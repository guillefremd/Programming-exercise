import random
import matplotlib.pyplot as plt
import time
import math


#Phase 1: MyHealthcare device: Vital signs simulator
def myHealthcare(n):
    m = 8
    table = [[0] * m for i in range(n)]
    random.seed(109)
    for i in range(len(table)):
        table[i][0]=i
        table[i][1]=random.randint(36, 39)
        table[i][2]=random.randint(55, 100)
        table[i][3]=random.randint(55, 100)
        table[i][4]=random.randint(120, 121)
        table[i][5]=random.randint(11, 17)
        table[i][6]=random.randint(93, 100)
        table[i][7]=round(random.uniform(7.1,7.6), 1)
    return (table)


#Phase 2: Run analytics
#a) Find abnormal values for pulse
def AbnormalPulseAnalytics_basic(table):
    random.seed(109)
    sample = []
    sample = random.sample(table, 50)
    sample.sort() #in this "basic" version of the function  I am using Python's sort. In the function AbnormalPulseAnalytics2 I use my owns merge sorting.
    abnormals=[]
    for i in sample:
        if i[3]<60 or i[3]>99:  #This is a linear search algorithm. Thus, its cost is O(n) 
            values=[i[0],i[3]]
            abnormals.append(values)

    amount=len(abnormals)
    output=["abnormal_pulse_count", amount, abnormals]

    return (output)


def AbnormalPulseAnalytics2(table):
    #this function uses  binary search algorithms to identify the abnormal values.
    #I coded two separate algorithms: one to identify those values that are abnormally high, and one for those abnormally low. Subsequently, I merge both subsets
    #However, both algorithms follow the same logic.
    #Given that it is a binary search, its computational cost is O(Log n)
    random.seed(109)
    sample = random.sample(table, 50)
    sortedLoL=mergesortLoL(sample,3)
    resultleft = binarySearchExtremelow(sortedLoL, 0, len(sortedLoL)-1, 60, 3)# function binarySearchExtremelows identifies one element with pulse value less than 60 
    subsetleft=leftside(sortedLoL,resultleft,3,60) #function leftside returns a subset with all records with pulse values less than 60
    resultright = binarySearchExtremeHigh(sortedLoL, 0, len(sortedLoL)-1, 99, 3)# function binarySearchExtremeHigh identifies one element with pulse value higher than 99
    subsetright=rightside(sortedLoL,resultright,3,99) #function rightside returns a subset with all records with pulse values 100 or more    
    abnormalsComplete=subsetleft+subsetright# Then, I merge the extreme low and the extreme high values
    abnormals=[]
    for i in abnormalsComplete:
        values=[i[0],i[3]]
        abnormals.append(values)
    amount=len(abnormals)
    output=["abnormal_pulse_count", amount, abnormals]
    return (output)


#b) Present a frequency histogram of pulse rates.


def frequencyAnalytics(table):
    random.seed(109)
    sample = []
    sample = random.sample(table, 50)
    hist = {}
    for record in sample: #This is a linear search algorithm. Thus, its cost is O(n)
        if record[3] in hist: 
            hist[record[3]]+=1
        else:
            hist[record[3]]=1
    histogram=[]
    for i in hist:
        histogram.append([i, hist[i]])
    return  (histogram)


#c) Plot the results for 2a and 2b

def plot_AbnormalPulseAnalytics(data):
    abnormals_amount=[data[1],50-data[1]]
    label_abnormal="Abnormal values: " + str(int(data[1]/50*100)) + "%" + "\n" + str(data[1]) + " out of 50"
    label_normal="Normal values: " + str(int((50-data[1])/50*100)) + "%"+ "\n" + str(50-data[1]) + " out of 50"
    plt.pie(abnormals_amount, labels=[label_abnormal, label_normal], explode=(0.1,0))
    plt.annotate(xy=[-1.2,-1.2], s="Abnormal values:\n " + str(data[2]))
    plt.title("Percentege of abnormal pulse values")
    

    plt.show()


def plot_frequencyAnalysis(data):
    value, number_of_cases= [*zip(*data)]
    plt.bar(value,number_of_cases)
    plt.xlabel("Pulse rate values")
    plt.ylabel("Frequency")
    plt.title("Histogram: pulse rate values frequency")
    yint = []
    locs, labels = plt.yticks()
    for each in locs:
        yint.append(int(each))
    plt.yticks(yint)
    plt.xticks(range(55,101,1))

    
    plt.show()


#Phase 3: Search for heart rates using the HealthAnalyzer

#a) Design a solution to search for a particular pulse rate value

def healthAnalyzer_basic(table,value, column):
    matches=[]
    for i in table:
        if i[column]==value:  #This is a linear search algorithm. Thus, its cost is O(n) 
            matches.append(i)
    return matches

def healthAnalyzer2(LoL,value,column):

    sortedLoL=(mergesortLoL(LoL, column))  #to perform a binary search, before searching, we need to sort records according to the column where we will then search
    result = binarySearchLoL(sortedLoL, 0, len(sortedLoL)-1, value, column)# function binarySearchLoL searches, with merge sort method, one record that matches the searched value 
    subset=(LookLeftRight(sortedLoL,result,column)) #once such value was identified with binarySearchLoL, function LookLeftRight searches to the left and to the right of such records all the "neighbour" records that have the same value
    return mergesortLoL(subset,0)       #Finally, I re-sort again (with mergesort) according to the first column, in order to present the results sorted by its timestamp. 


#c) Plot the heart rate values for records having pulse rate 56.
def plot_healthAnalyzer(data):
    heart_rates=[]
    for i in data:
        heart_rates.append(i[2])

    plt.hist(heart_rates,bins=10, color = "skyblue", ec="blue")
    plt.title("Heart rate values for records having pulse rate 56")
    plt.xlabel("Heart rate values")
    plt.ylabel("Frequency")
    plt.xticks(range(56,101,2))

    plt.show()

#Phase 4: Testing scalability of your algorithm (20 marks)
#Benchmark the MyHealthData application simulating n = 1000, 2500, 5000, 7500 and 10000 records from phase 1

def benchmarking(myHealthcare):
    timeskeeping = {}
    for a in [1000, 2500, 5000, 7500, 10000]:
        timebegin=float(time.time())
        myHealthcare(a)
        timeskeeping[a]=time.time()-timebegin
    return timeskeeping



def plotbench(timeskeeping):

    plt.plot(list(timeskeeping.keys()), list(timeskeeping.values()), 'ro')
    plt.title("Function benchmarking\n Vital signs simulator")
    plt.xlabel("Number of records analised")
    plt.ylabel("Time consumed")
    plt.show()


def bench_healthAnalyzer():

    timeskeeping = []
    for a in [1000, 2500, 5000, 7500, 10000]:
        
        data=myHealthcare(a)
        timebegin=time.time()
        healthAnalyzer_basic(data,56,3)
        timebasic=time.time()-timebegin

        timebegin=time.time()
        healthAnalyzer2(data,56,3)
        timeadvanced=time.time()-timebegin
        timeskeeping.append([a,timebasic,timeadvanced])
        
        
    return timeskeeping

def plot_bench_healthAnalyzer(timeskeeping):
    
    number, timebasic,timeadvanced= [*zip(*timeskeeping)]#
    plt.plot(number, timebasic, label="Function with linear search")
    plt.plot(number,timeadvanced, label="Function with merge-sort and binary search")
    plt.xlabel("Number of records created")
    plt.ylabel("Time consumed")
    plt.title("Benchmarking of two healthAnalyzer functions")
    plt.legend()
    plt.show()

def benchmarch(): #This function triggers the benchmarching functions and their plotings
    plotbench(benchmarking(myHealthcare))
    plot_bench_healthAnalyzer(bench_healthAnalyzer())
    


def main():

    simulated_data=myHealthcare(1000)
    abnormal=AbnormalPulseAnalytics2(simulated_data)
    frequency=frequencyAnalytics(simulated_data)
    pulse59= healthAnalyzer_basic(simulated_data,59,3)
    pulse56= healthAnalyzer2(simulated_data,56,3)
    

    print("Basic Abnormal Pulse Analytics function:\n")
    print (abnormal)
    print("\n")
    print("Advanced Abnormal Pulse Analytics function:\n")
    print (abnormal)
    print("\n")
    print("Frequency Analytics function:\n")
    print(frequency)
    print("\n")
    print("Basic Health Analyzer function, for pulse value 59:\n")
    print(pulse59)
    print("\n")
    print("Advanced Health Analyzer function, for pulse value 56:\n")
    print(pulse56)
    print("\n")

    plot_frequencyAnalysis(frequency)
    plot_AbnormalPulseAnalytics(abnormal)
    plot_healthAnalyzer (pulse56)
    benchmarch()


#Below are coded the algorithms for merge sort and binary search, both for list and for list of lists.
    

def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break
	return result

def mergesort(list):
	if len(list) < 2:
		return list
	middle = len(list)//2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])
	return merge(left, right)

def mergeLoL(left, right, column): #this function is used to merge sort list of lists
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        
        if left[i][column] < right[j][column]:    
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if j == len(right) or i == len(left):
            result.extend(left[i:] or right[j:])
            break
    return result

def mergesortLoL(list, column): #this function is used to merge-sort a list of lists, according to one of the columns.
    if len(list) < 2:
        return list
    
    middle = len(list)//2
    left = mergesortLoL(list[:middle], column)
    right = mergesortLoL(list[middle:], column)
    return mergeLoL(left, right, column)
    
def binarySearchLoL (lol, left, right, x, column):

    if right >= left:
        mid = left + (right - left) // 2
        if lol[mid][column] == x:
            return mid 
        elif lol[mid][column] > x:
            return binarySearchLoL(lol, left, mid-left, x, column) 
        else: 
            return binarySearchLoL(lol, left+mid, right, x, column) 
    else:  
        return -1
	    
def LookLeftRight(arr,found,column):

    if found==-1: return ("Element is not present in array")
    allValues=[arr[found]]
    leftlimit=found
    rightlimit=found
    while arr[leftlimit-1][column]==arr[found][column]:
        if leftlimit==1:
            leftlimit=0
            break
        else:
            leftlimit-=1
    while arr[rightlimit+1][column]==arr[found][column]:
        if rightlimit+1==len(arr)-1:
            rightlimit+=1
            break
        else:
            rightlimit+=1
    return arr[leftlimit:rightlimit]

def binarySearchExtremelow (lol, left, right, x, column):

    if right >= left:
        mid = left + (right - left) // 2
        if lol[mid][column]< x:
            return mid
        
	 
        elif lol[mid][column] >= x:

            return binarySearchExtremelow(lol, left, mid-left, x, column) 
		 
        else: 
            return binarySearchExtremelow(lol, left+mid, right, x, column) 
    else:  
        return -1

def binarySearchExtremeHigh (lol, left, right, x, column):

    if right >= left:
        mid = left + (right - left) // 2
        if lol[mid][column]> x:
            return mid 
	 
        elif lol[mid][column] <= x:
            return binarySearchExtremeHigh(lol, mid, right, x, column)

    else:  
        return -1

def leftside(arr,found,column,leftlimit):

    if found==-1: return ("Element is not present in array")
    
    rightlimit=found
    
    while arr[rightlimit+1][column]<leftlimit:
        if rightlimit+1==len(arr)-1:
            rightlimit+=1
            break
        else:
            rightlimit+=1
    print("arr[:rightlimit]")
    return arr[:rightlimit+1]

def rightside(arr,found,column,rightlimit):

    if found==-1: return ("Element is not present in array")
    
    leftlimit=found
    
    while arr[leftlimit-1][column]>rightlimit:
        
        if leftlimit==1:
            leftlimit=0
            break
        else:
            leftlimit-=1

    
    return arr[leftlimit:]

if __name__ == "__main__":
    main()
