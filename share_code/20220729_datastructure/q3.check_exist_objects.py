# store = map(int, input('store 값 입력 :'))
# customer = map(int, input('customer 값 입력:'))
store = [2, 3, 7, 8, 9]
customer = [7, 5, 9]

answer = []

for i in customer:
    if i in store:
        answer.append('yes')
    else:
        answer.append('no')
    
print(answer)