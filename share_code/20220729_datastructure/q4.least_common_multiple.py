
# arr = map(int, input('리스트 값 입력:'))
arr = [2, 6, 8, 14]     # test1
# arr = [1, 2, 3]         # test2
least = 0


def lcm(a, b):
    return a*b/gcd(a, b)
    
    
def gcd(a, b):
    if a > b:
        return b if a%b == 0 else gcd(a%b, b)
    elif a < b:
        return a if b%a == 0 else gcd(a, b%a)
    else:
        return a


if len(arr) > 2:
    least = lcm(arr[0], arr[1])
    
    for i in arr[2:]:
        least = lcm(least, i)
        
''' # 리스트의 원소개수가 2개 이하인 경우
elif len(arr) == 2:
    least = lcm(arr[0], arr[1])
    
else:
    least = arr[-1]
''' 
print(f'result:{int(least)}')