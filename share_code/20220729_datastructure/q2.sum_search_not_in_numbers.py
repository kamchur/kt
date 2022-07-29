
# numbers = [1,2,3,4,6,7,8,0]   # test1
numbers = [5,8,4,0,6,7,9]   #test2
sum = 0
for i in range(1, 10):
    if i not in numbers:
        sum += i
        
print(sum)