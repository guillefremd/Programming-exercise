
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


arr = [[0, 38, 69, 84, 121, 15, 93, 7.2], [1, 39, 74, 91, 120, 17, 96, 7.3], [2, 38, 82, 97, 120, 13, 98, 7.1], [3, 37, 95, 55, 121, 15, 96, 7.2], [4, 37, 80, 97, 121, 12, 99, 7.3], [5, 37, 57, 99, 120, 14, 99, 7.4], [6, 36, 72, 99, 120, 17, 100, 7.4], [7, 36, 97, 58, 121, 14, 98, 7.4], [8, 39, 56, 58, 121, 11, 100, 7.3], [9, 37, 78, 80, 120, 15, 97, 7.3], [10, 39, 87, 81, 121, 15, 96, 7.4], [11, 36, 76, 62, 120, 15, 96, 7.1], [12, 38, 91, 64, 121, 12, 97, 7.4], [13, 38, 82, 84, 121, 14, 96, 7.5], [14, 36, 71, 100, 121, 16, 94, 7.1], [15, 36, 67, 63, 121, 14, 94, 7.1], [16, 37, 96, 55, 121, 12, 94, 7.2], [17, 37, 62, 99, 120, 11, 100, 7.3], [18, 37, 76, 56, 121, 12, 95, 7.1], [19, 38, 97, 58, 120, 17, 99, 7.2], [20, 36, 99, 96, 120, 13, 96, 7.2], [21, 38, 71, 58, 121, 16, 96, 7.2], [22, 39, 95, 59, 120, 12, 98, 7.4], [23, 39, 96, 62, 120, 12, 94, 7.4], [24, 38, 96, 91, 120, 15, 94, 7.3], [25, 39, 85, 56, 120, 13, 93, 7.1], [26, 38, 87, 89, 121, 11, 97, 7.4], [27, 36, 65, 70, 120, 13, 98, 7.1], [28, 36, 100, 99, 121, 16, 93, 7.1], [29, 36, 70, 87, 121, 17, 97, 7.1], [30, 39, 100, 57, 120, 13, 99, 7.5], [31, 39, 65, 59, 120, 16, 96, 7.4], [32, 38, 91, 82, 120, 15, 97, 7.2], [33, 38, 94, 82, 121, 14, 97, 7.3], [34, 36, 92, 68, 121, 16, 94, 7.5], [35, 38, 59, 92, 120, 12, 93, 7.1], [36, 38, 71, 96, 121, 14, 97, 7.4], [37, 38, 62, 73, 121, 12, 97, 7.4], [38, 36, 61, 89, 121, 15, 94, 7.2], [39, 38, 67, 93, 120, 16, 94, 7.1], [40, 36, 77, 83, 120, 16, 95, 7.1], [41, 36, 68, 89, 120, 13, 94, 7.5], [42, 37, 97, 79, 121, 15, 94, 7.2], [43, 39, 83, 67, 121, 13, 95, 7.1], [44, 37, 96, 87, 120, 15, 95, 7.3], [45, 39, 75, 66, 121, 12, 99, 7.3], [46, 39, 69, 90, 121, 16, 93, 7.3], [47, 39, 99, 91, 121, 13, 95, 7.2], [48, 39, 67, 58, 120, 13, 95, 7.6], [49, 38, 70, 57, 121, 14, 93, 7.2], [50, 36, 76, 76, 121, 14, 96, 7.6], [51, 36, 86, 72, 121, 15, 95, 7.6], [52, 37, 66, 76, 121, 13, 95, 7.2], [53, 39, 79, 76, 120, 11, 97, 7.4], [54, 38, 65, 74, 121, 14, 98, 7.4], [55, 39, 74, 58, 121, 16, 95, 7.3], [56, 36, 79, 57, 121, 13, 97, 7.2], [57, 39, 77, 60, 121, 13, 93, 7.6], [58, 38, 61, 76, 121, 16, 96, 7.4], [59, 38, 92, 91, 121, 13, 95, 7.5], [60, 36, 93, 96, 121, 12, 96, 7.5], [61, 36, 68, 96, 121, 15, 96, 7.5], [62, 38, 92, 71, 120, 12, 100, 7.4], [63, 39, 57, 69, 120, 15, 100, 7.5], [64, 37, 95, 100, 121, 16, 95, 7.1], [65, 39, 68, 77, 121, 13, 98, 7.3], [66, 37, 55, 82, 120, 17, 94, 7.6], [67, 37, 86, 57, 120, 17, 94, 7.6], [68, 38, 84, 88, 121, 12, 94, 7.2], [69, 39, 71, 64, 121, 15, 95, 7.5], [70, 38, 86, 71, 120, 11, 96, 7.4], [71, 37, 87, 63, 120, 13, 94, 7.2], [72, 37, 63, 72, 121, 17, 98, 7.2], [73, 38, 63, 91, 121, 17, 98, 7.5], [74, 36, 57, 80, 121, 16, 99, 7.5], [75, 36, 90, 55, 121, 13, 100, 7.6], [76, 36, 69, 85, 120, 15, 96, 7.5], [77, 38, 64, 96, 120, 12, 97, 7.3], [78, 37, 67, 100, 120, 12, 98, 7.2], [79, 38, 90, 66, 121, 12, 93, 7.3], [80, 39, 63, 87, 120, 12, 97, 7.5], [81, 38, 96, 72, 120, 11, 93, 7.3], [82, 37, 84, 57, 121, 16, 97, 7.3], [83, 39, 94, 77, 120, 16, 97, 7.5], [84, 37, 62, 80, 120, 17, 95, 7.5], [85, 39, 87, 93, 121, 12, 98, 7.5], [86, 36, 57, 61, 121, 15, 99, 7.4], [87, 38, 93, 58, 121, 12, 97, 7.2], [88, 36, 73, 64, 121, 15, 100, 7.1], [89, 37, 98, 89, 120, 17, 100, 7.4], [90, 37, 74, 57, 120, 14, 95, 7.2], [91, 39, 75, 76, 120, 17, 96, 7.2], [92, 36, 69, 86, 120, 12, 100, 7.3], [93, 38, 74, 56, 121, 11, 94, 7.4], [94, 37, 99, 58, 121, 11, 100, 7.1], [95, 38, 100, 97, 121, 13, 100, 7.1], [96, 38, 92, 65, 121, 14, 100, 7.3], [97, 37, 64, 64, 121, 15, 95, 7.5], [98, 37, 88, 88, 121, 12, 97, 7.2], [99, 36, 58, 85, 120, 14, 93, 7.2]]
x =56

result = binarySearchLoL(arr, 0, len(arr)-1, x, 3)
print(LookLeftRight(arr,result,3))

#if result != -1: 
	#print (LookLeftRight(arr,result,3)) 
#else: 
	#print ("Element is not present in array") 