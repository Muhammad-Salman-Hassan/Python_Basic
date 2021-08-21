####DIvide and Conquer Method first divide and then conquer

def merge(arr):
    if len(arr)>1:
        #dividing
        mid=len(arr)//2
        #left
        L=arr[:mid]
        #right
        R=arr[mid:]
        #sort left
        merge(L)
        #sort right
        merge(R)
        
        #i controll index
        i=j=k=0
        
        while i < len(L) and j < len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
        
arr=[44,6,9,7,1]
merge(arr)
printlist(arr)
