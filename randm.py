import random,os
# #def return_random_list():
print("Enter your desired input size")
input_size=input()
numbers = random.sample(range(1, 100000), int(input_size))
print (numbers)
with open('global_var.py', 'w') as f:
    f.write("input_size=%s\n" % input_size)
    f.write("numbers=%s" % numbers)


# the_list = numbers
# os.system("python insertion_Sort.py {0}".format(the_list))
#  #a =return_random_list()
# #print a

