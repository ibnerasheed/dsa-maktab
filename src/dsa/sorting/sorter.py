def bubble_sort(iterable, lb = None, ub = None):
    for sweep in range(len(iterable)):
        swap = False
        for index in range(len(iterable) - sweep - 1):
            if iterable[index] > iterable[index + 1]:
                iterable[index],iterable[index+1] = iterable[index+1], iterable[index]
                swap = True
        if not swap:
            break 
    return iterable  



















                