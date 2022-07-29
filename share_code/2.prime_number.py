arr = []

def is_prime_number(n):
    result = True
    start = 2
    end = n//2 + 1
    
    for i in range(start, end):
        if n % i == 0:
            result = False
            break
    
    return result

for i in range(2, 1000+1):
    if is_prime_number(i):
        arr.append(i)
         
print(arr)
print(len(arr))