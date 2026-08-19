li = list(map(int, input().split()))

def SelectionSort(li):

    for i in range(len(li)):
        min_index = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_index]:
                min_index = j

        li[i], li[min_index] = li[min_index], li[i]
    return li

print("Selection Sort Result: ", SelectionSort(li))