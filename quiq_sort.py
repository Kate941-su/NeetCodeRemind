from preset_data.module import random_list

def quick_sort(array):
  if (len(array) < 2): # Basic case
    return array 
  else:
    pivot = array[0]
    
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater)
  
print(quick_sort(random_list))