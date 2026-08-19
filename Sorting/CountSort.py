li = [1,4,1,2,7,5,2]
counter = [0]*10
for i in li:
    counter[i] += 1

for i in range(1,len(counter)):
    counter[i] = counter[i]+counter[i-1]

places = [0]*len(li)
for i in li:
    places[counter[i]-1]= i
    counter[i] -= 1

print(places)

