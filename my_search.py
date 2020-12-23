
def sequential_search(elem,alist):
    length = len(alist)
    i=0
    while i<length:
        if alist[i]==elem:
            return i
        i+=1
    return -1    
        
def binary_search(elem,alist):
    last = len(alist)-1
    first = 0
    middle = int((first+last)/2)
    while first<=last:
        if elem>alist[middle]:
            first = middle+1
            middle = int((first+last)/2)
        elif elem==alist[middle]:
            return middle
        else:
            last = middle-1
            middle = int((first+last)/2)
    return -1        

