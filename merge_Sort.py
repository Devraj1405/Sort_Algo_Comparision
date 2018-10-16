import time
import sys
sys.setrecursionlimit(2000)
try:
    from global_var import numbers
    from global_var import input_size
except:
    print ("Please run the code 'randm.py' and enter the input size, then run this #again(Because we want the same dataset for all 4 sort techniques)")
    exit()

def merge_Sort(the_list):   #Function for sorting numbers
    #print("Split ",the_list)
    if len(the_list)>1:
        mid = len(the_list)//2   #Floor Division
        leftside = the_list[:mid]   #All elements on the left of mid
        rightside = the_list[mid:]   #All elements on the right of mid
        merge_Sort(leftside)
        merge_Sort(rightside)

        i=0   #Index for the Left Array  
        j=0   #Index for the Right Array
        k=0   #Index for the Merged Array
        while i < len(leftside) and j < len(rightside):   #Comparing the elements of both sides
            if leftside[i] < rightside[j]:
                the_list[k]=leftside[i]
                i=i+1
            else:
                the_list[k]=rightside[j]
                j=j+1
            k=k+1

        while i < len(leftside):   #Copy the remaining elements of left Side
            the_list[k]=leftside[i]
            i=i+1
            k=k+1

        while j < len(rightside):   #Copy the remaining elements of Right Side
            the_list[k]=rightside[j]
            j=j+1
            k=k+1
    #print("Merge ",the_list)

the_list = numbers
print ("The " + str(input_size) + " Randomly generated numbers are ")
print(numbers)
start=time.time()   #For Calculating the time taken by the Insertion Sort Algorithm

merge_Sort(the_list)   #Feeds the values to the function
print("The List of numbers after being sorted is as follows ")
end=time.time()
print(the_list)
print ("The numbers were sorted using Merge Sort in " + str((end-start) * 1000)  + " ms time.")

print("\nSpecial Case 'a': Already Sorted Array")
start=time.time()
merge_Sort(the_list)   #Feeds the values to the function

end=time.time()
print(the_list)
print ("Already Sorted : The numbers were sorted using Merge Sort in " + str((end-start) * 1000)  + " ms time.\n")
print("Special Case 'b': Reverse Sorted array")
the_list = the_list[::-1]   #Reverses the list 
print (the_list)
start_1=time.time()
merge_Sort(the_list)
end_1= time.time()
print (the_list)
print ("Reverse Sorted : The numbers were sorted using Merge Sort in " + str((end_1-start_1) * 1000)  + " ms time.")