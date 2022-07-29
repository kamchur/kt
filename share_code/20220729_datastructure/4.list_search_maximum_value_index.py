

a = [4, 67, 33, 1, 10, 777,51]

idx = 0
max = a[idx]

for i in range(1, len(a)):
    if max < a[i]:
        max = a[i]
        idx = i
        
print(f'최대값:{max}, 인덱스:{idx}')
        