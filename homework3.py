import random
import pandas as pd 
file = "https://d3c33hcgiwev3.cloudfront.net/_32387ba40b36359a38625cbb397eee65_QuickSort.txt?Expires=1512518400&Signature=Rw1c9gP0Fa1XQfSb6nYf6GIQn-VYVjRC8nkspf5cqry89YQQs3HSJgiXR2Tfr-OiIjNUNhwSpCz0IeQRKfl0iPiSFNH0hgCgZB0~r5v48yn50haGC-80pgd3VZ0RkZb7xVVMwkJlyQq~cCWMr2JyaBAMcaSrAs3mb05G6L7jxo8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
df = pd.read_csv(file, header = None)

unsorted_list = df.ix[:,0].tolist()

comp_count = 0

def partition_array(list_, start_val, end_val, pivot_val):
    list_[pivot_val] = list_[end_val]
    list_[end_val] = list_[pivot_val]
    
    global comp_count
    
    store_index = start_val
    for i in range(start_val, end_val):
        if list_[i] < list_[end_val]:
            list_[i], list_[store_index] = list_[store_index], list_[i]
            store_index += 1
            comp_count += 1
    list_[store_index], list_[end_val] = list_[end_val], list_[store_index]
    return store_index


    def quick_sort(list_, start_val, end_val):
    if start_val >= end_val:
        return list_
    pivot_val = random.randrange(start_val, end_val + 1)
    new_pivot = partition_array(list_, start_val, end_val, pivot_val)
    quick_sort(list_, start_val, new_pivot - 1)
    quick_sort(list_, new_pivot + 1, end_val)

    def sort(list_):
    quick_sort(list_, 0, len(list_) - 1)
    return list_