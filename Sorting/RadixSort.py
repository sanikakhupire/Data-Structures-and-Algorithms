from collections import deque

num = [170, 45, 75, 90, 802, 24, 2, 66]

li = [0]*10
for i in range(len(li)):
    li[i] = deque()

max_digits = len(str(max(num)))
for j in range(max_digits):
    for i in num:
        n = i//(10**j)
        digit = n%10
        li[digit].append(i)

    num = []
    for i in li:
        while i:
            num.append(i.popleft())    

print(num)


# Optimal 
def optimal_radix_sort(num_list):
    if not num_list:
        return num_list
        
    # Standard Python lists are faster than deques for mass flattening
    buckets = [[] for _ in range(10)]
    max_digits = len(str(max(num_list)))
    
    for j in range(max_digits):
        divisor = 10**j  # Pre-calculate to avoid repeating math
        
        for i in num_list:
            # OPTIMIZATION: Use integer floor division (//)
            digit = (i // divisor) % 10
            buckets[digit].append(i)
    
        # OPTIMIZATION: Use list.extend() instead of popping elements one-by-one
        num_list = []
        for b in buckets:
            num_list.extend(b)
            b.clear() # Clear the bucket for the next pass
                
    return num_list
