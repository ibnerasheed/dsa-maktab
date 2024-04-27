from dsa.common.util import is_lessthan, negation

def bubble_sort(iterable, lb = 0, ub = None, key = lambda obj:obj, reverse = False):
    if ub is None:  
        ub = len(iterable) 

    if lb > ub:
        return iterable

    length = ub - lb

    comparator = is_lessthan
    if reverse:
        comparator = negation(comparator)

    for sweep in range(length):
        swapped = False
        for offset in range(length - sweep - 1):
            index = lb + offset
            val1 = key(iterable[index + 1])
            val2 = key(iterable[ index])
            
            if comparator(val1,val2):
                iterable[ index], iterable[ index+1] = iterable[ index+1], iterable[ index]
                swapped = True
        if not swapped:
            break
    return iterable  
    


def selection_sort(iterable, lb = 0, ub = None, reverse = False):
    if ub is None:  
        ub = len(iterable) 

    if lb > ub:
        return iterable
    
    comparator = is_lessthan
    if reverse:
        comparator = negation(is_lessthan)

    length = ub - lb - 1
    for sweep_number in range(length):
        min_index = lb + sweep_number
        for j in range(min_index + 1, ub):
            if comparator(iterable[j], iterable[min_index]):
                min_index = j
            
        if comparator(iterable[min_index], iterable[lb + sweep_number]):
            iterable[min_index],iterable[lb + sweep_number] = iterable[lb + sweep_number],iterable[min_index]

    return iterable        

              
    
    
   
        

















                