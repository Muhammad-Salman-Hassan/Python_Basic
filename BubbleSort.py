def bsort(arr):
    
    
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)-i):
            if arr[j]<arr[j-1]:
                swap(arr,j,j-1)

def swap(arr,index_1,index_2):
    temp=arr[index_1]
    arr[index_1]=arr[index_2]
    arr[index_2]=temp

arr=[25,1,3,4,5]
bsort(arr)

for i in range(len(arr)):
    print(arr[i])
            
