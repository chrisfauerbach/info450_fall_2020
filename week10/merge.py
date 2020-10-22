import random

def merge_sort(inbound): 
    if len(inbound) >1: 
        mid = len(inbound)//2 # Finding the mid of the array 
        left_array = inbound[:mid] # Dividing the array elements  
        right_array = inbound[mid:] # into 2 halves 
  
        merge_sort(left_array) # Sorting the first half 
        merge_sort(right_array) # Sorting the second half 
  
        i = j = k = 0 
          
        # Copy data to temp arrays left_array[] and right_array[] 
        while i < len(left_array) and j < len(right_array): 
            if left_array[i] < right_array[j]: 
                inbound[k] = left_array[i] 
                i+= 1
            else: 
                inbound[k] = right_array[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(left_array): 
            inbound[k] = left_array[i] 
            i+= 1
            k+= 1
          
        while j < len(right_array): 
            inbound[k] = right_array[j] 
            j+= 1
            k+= 1
  
if __name__ == '__main__': 
    my_list = []
    for x in range(20):
        my_list.append(random.randint(0, 1000))
    print(my_list)

    merge_sort(my_list) 

    print(my_list) 
  

