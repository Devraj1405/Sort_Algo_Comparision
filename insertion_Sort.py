import time
import sys
sys.setrecursionlimit(2000)
try:
    from global_var import numbers
    from global_var import input_size
except:
    print ("Please run the code 'randm.py' and enter the input size, then run this #again(Because we want the same dataset for all 4 sort techniques)")
    exit()
# print input_size
# print numbers
def insertion_Sort(the_list):   #Function for sorting numbers 
   for index in range(1,len(the_list)):

     cv = the_list[index]
     cp = index

     while cp>0 and the_list[cp-1]>cv:   #while loop for comparing values
         the_list[cp]=the_list[cp-1]
         cp = cp-1

     the_list[cp]=cv

the_list = []   #Define an empty list
the_list = numbers
print ("The " + str(input_size) + " Randomly generated numbers are ")
print(numbers)
start=time.time()   #For Calculating the time taken by the Insertion Sort Algorithm
insertion_Sort(the_list)   #Feeds the values to the function
end=time.time()
print("The List of numbers after being sorted is as follows ")
print(the_list)

print ("The numbers were sorted using Insertion Sort in " + str((end-start) * 1000)  + " ms time.")
print("\nSpecial Case 'a': Already Sorted Array")
start=time.time()
insertion_Sort(the_list)   #Feeds the values to the function
end=time.time()
print(the_list)
print ("Already Sorted : The numbers were sorted using Insertion Sort in " + str((end-start) * 1000)  + " ms time.\n")
print("Special Case 'b': Reverse Sorted array")
the_list = the_list[::-1]   #This reverses the list
print (the_list)
start=time.time()
insertion_Sort(the_list)   #Enters the list in the loop
end= time.time()
print (the_list)
print ("Reverse Sorted : The numbers were sorted using Insertion Sort in " + str((end-start) * 1000)  + " ms time.")

