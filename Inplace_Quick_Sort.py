import time
import sys
sys.setrecursionlimit(2000)
try:
    from global_var import numbers
    from global_var import input_size
except:
    print ("Please run the code 'randm.py' and enter the input size, then run this #again(Because we want the same dataset for all 4 sort techniques)")
    exit()
def quick_Sort(the_list):   #Function for sorting numbers
    if len(the_list) <= 1:   #If list has 1 number or less it will return it
        return the_list
    return divide(the_list,0,len(the_list)-1)   #passing the call to divide function

def divide(the_list,start_of_list,end_of_list):   
    pivot = the_list[end_of_list]   #last element is considered as the pivot
    partition = start_of_list
    if start_of_list < end_of_list:  
        for i in range(start_of_list,end_of_list+1):   #loops through
            if the_list[i] <= pivot:
                the_list[partition], the_list[i] = the_list[i], the_list[partition]
                if i != end_of_list:
                    partition += 1
        divide(the_list,start_of_list,partition-1)   #recursion until list is sorted
        divide(the_list,partition+1,end_of_list)     
    return the_list        

def main():
    the_list = numbers
    print ("The " + str(input_size) + " Randomly generated numbers are ")
    print(numbers)
    start=time.time()   #For Calculating the time taken by the Inplace Quick Sort Algorithm
    quick_Sort(the_list)   #Feeds the values to the function
    end = time.time()
    print("The List of numbers after being sorted is as follows ")
    print(the_list)   #sorted list
    print ("The numbers were sorted using Inplace Quick Sort in " + str((end-start) * 1000)  + " ms time.")
    reverse_list = the_list[::-1]   #reverses the list
    print(reverse_list)

    print("\nSpecial Case 'a': Already Sorted Array")
    start = time.time()
    quick_Sort(the_list)  # Feeds the values to the function
    end = time.time()
    print(the_list)
    print ("Already Sorted : The numbers were sorted using Inplace Quick Sort in " + str(
        (end - start) * 1000) + " ms time.\n")
    print("Special Case 'b': Reverse Sorted array")
    the_list = the_list[::-1]   #Reverses the list
    print (the_list)
    start = time.time()
    quick_Sort(the_list)
    end = time.time()
    print (the_list)
    print ("Reverse Sorted : The numbers were sorted using Inplace Quick Sort in " + str(
        (end - start) * 1000) + " ms time.")
main() 

