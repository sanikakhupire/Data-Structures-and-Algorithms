
li = list(map(int, input().split()))
n = len(li)-1
def BubbleSort(li,n):
    while n>0:
        for i in range(n):
            if li[i]>li[i+1]:
                li[i],li[i+1] = li[i+1], li[i]
        n-=1
    return li

print("Bubble Sort Rest: ", BubbleSort(li,n))

