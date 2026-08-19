li = list(map(int, input().split()))

def InsertionSort(li):
    for i in range(1, len(li)):
        
        j = i-1
        if li[i]<li[j]:
            temp = li[i]
            while temp < li[j] and j>=0:
                li[j+1] = li[j]
                j-=1

            if j >= 0:
                li[j+1]=temp
            else:
                li[0] = temp
    return li

print("Insertion Sort Result: ", InsertionSort(li))  