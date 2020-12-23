import random
from my_sort import insertion_sort
from my_search import sequential_search
from my_search import binary_search
from my_sort import merge_sort      
#导入所需模块

alist = []
for i in range(100):
    a = random.randint(0,100)
    alist.append(a)
print(alist)
#生成包含100个值的列表并打印

b = int(input('请输入一个两位或一位整数：'))
#要求用户输入

c = sequential_search(b,alist)
if c ==-1:
    print('Not found!')
else:
    print('Found %d' %b,'in the position %d.' %c)
#调用顺序查找直接找位置
    
alist = insertion_sort(alist)
print(alist)
#调用插入排序法进行排序并打印排序后列表
d = binary_search(b,alist)
if d ==-1:
    print('Not found!')
else:
    print('Found %d' %b,'in the position %d.' %d)
#调用二分搜索进行查找    

alist = merge_sort(alist)
print(alist)
#调用归并排序进行排序并打印
e = binary_search(b,alist)
if e ==-1:
    print('Not found!')
else:
    print('Found %d' %b,'in the position %d.' %e)
#调用二分搜索进行查找

