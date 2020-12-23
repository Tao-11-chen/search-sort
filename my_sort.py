def maopao_sort(alist):
    for j in range (len(alist)):
        for i in range (j):
            if alist[i]>=alist[j]:
                alist[i],alist[j] = alist[j],alist[i]  #多写了个冒泡排序法
    return alist
def insertion_sort(alist):
    length = len(alist)
    for i in range (1,length):
        j = i-1
        a = alist[i]
        while j>=0:
            if alist[j]>a:
                alist[j+1]=alist[j]
                alist[j]=a
            j = j-1
    return alist
    
def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle = int(len(alist)/2)
    l = merge_sort(alist[:middle])  #递归，自己调用自己用于拆分
    r = merge_sort(alist[middle:])
    return merge(l,r)

def merge(a,b):
    c = []
    h=j=0
    while j<len(a) and h<len(b):   #调用递归中分出的列表来合并成有序列表
        if a[j]<b[h]:
            c.append(a[j])
            j+=1
        else:
            c.append(b[h])
            h+=1
    if j==len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c
                    
    

