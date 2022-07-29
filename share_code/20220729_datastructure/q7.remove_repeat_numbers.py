arr = [1, 1, 3, 3, 0, 1, 1]
idx = 0
answer = [arr[0]]

for i, val in enumerate(arr):
    if arr[idx] != val:
        idx = i
        answer.append(val)

print(answer)