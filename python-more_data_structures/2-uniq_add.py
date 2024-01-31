#!/usr/bin/python3
def uniq_add(my_list=[]):
    res_set = set()
    result = 0
    
    for item in my_list:
        if item not in res_set:
            res_set.add(item)
            result += item
            
    return result
