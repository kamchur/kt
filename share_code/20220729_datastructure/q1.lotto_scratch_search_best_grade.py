
lotto = [x for x in range(1, 45)]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

count = 0

def grade(cnt):
    grade = 6
    if cnt == 6:
        grade = 1
    elif cnt == 5:
        grade = 2
    elif cnt == 4:
        grade = 3
    elif cnt == 3:
        grade = 4
    elif cnt == 2:
        grade = 5
    else:
        grade = 6
    return grade

zero_cnt = 0

for i in lottos:
    if i == 0:
        zero_cnt += 1
    elif i in win_nums:
        count += 1

print(f'{zero_cnt + count}개 번호 일치, {grade(zero_cnt + count)}등')
print(f'{count}개 번호 일치, {grade(count)}등')