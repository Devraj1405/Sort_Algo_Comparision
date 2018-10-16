import time
import sys
sys.setrecursionlimit(2000)
try:
    from global_var import numbers
    from global_var import input_size
except:
    print ("Please run the code 'randm.py' and enter the input size, then run this #again(Because we want the same dataset for all 4 sort techniques)")
    exit()
    
def quick_Sort(the_list):   #the list is passed in the function from main
   recursive_quick_Sort(the_list,0,len(the_list)-1)

def recursive_quick_Sort(the_list,ele_first,ele_last):   #Recursively calls the funstion to sort 
   if ele_first<ele_last:

       divide_here = divided(the_list,ele_first,ele_last)

       recursive_quick_Sort(the_list,ele_first,divide_here-1)   #to sort the left side from partition
       recursive_quick_Sort(the_list,divide_here+1,ele_last)   #to sort the right side from partition

def divided(the_list,ele_first,ele_last):   #For dividing 
   index_of_pivot = median_decider(the_list, ele_first, ele_last, (ele_first + ele_last) // 2)   #used to decide the median
   the_list[ele_first], the_list[index_of_pivot] = the_list[index_of_pivot], the_list[ele_first]
   value_of_pivot = the_list[ele_first]

   l_s = ele_first
   r_s = ele_last
   
   done = False
   while not done:

       while l_s <= r_s and the_list[l_s] <= value_of_pivot:   #Check if it's less than the pivot                
           l_s = l_s + 1

       while the_list[r_s] >= value_of_pivot and r_s >= l_s:   #check if it's greater than the pivot
           r_s = r_s -1

       if r_s < l_s:
           done = True
       else:
           var_t = the_list[l_s]
           the_list[l_s] = the_list[r_s]
           the_list[r_s] = var_t

   var_t = value_of_pivot
   the_list[the_list.index(value_of_pivot)] = the_list[r_s]
   the_list[r_s] = var_t

   return r_s

def median_decider(a, i, j, b):   #Function for median
  if a[i] < a[j]:
    return j if a[j] < a[b] else b
  else:
    return i if a[i] < a[b] else b


def insertion_Sort(the_list):   #If the input size is less than or equal to 10 insertion sort will be called/used
   for index in range(1,len(the_list)):

     cv = the_list[index]
     index_pos = index

     while index_pos>0 and the_list[index_pos-1]>cv:   #comparing values
         the_list[index_pos]=the_list[index_pos-1]
         index_pos = index_pos-1

     the_list[index_pos]=cv
    
the_list = []   #Define an empty list
the_list = numbers
print ("The " + str(input_size) + " Randomly generated numbers are ")
print(numbers)
if(int(input_size)<=10):   #If input size is less than 10 it will use insertion sort
    print("Insertion Sort is used to sort numbers of input size less than or equal to 10")
    insertion_Sort(the_list)
else:
    print("Quick Sort is used to sort numbers of input size greater than or equal to 10")
start=time.time()   #Calculates the time
quick_Sort(the_list)

end=time.time()
print(the_list)
print ("The numbers were sorted in " + str((end-start) * 1000)  + " ms time.")



print("\nSpecial Case 'a': Already Sorted Array")
start = time.time()
quick_Sort(the_list)  # Feeds the values to the function

end = time.time()
print(the_list)
print ("Already Sorted : The numbers were sorted using Modified Quick Sort in " + str(
    (end - start) * 1000) + " ms time.\n")
print("Special Case 'b': Reverse Sorted array")
the_list = the_list[::-1]   #It reverses the list
print (the_list)
start = time.time()
quick_Sort(the_list)
end = time.time()
print (the_list)
print ("Reverse Sorted : The numbers were sorted using Modified Quick Sort in " + str(
    (end - start) * 1000) + " ms time.")
