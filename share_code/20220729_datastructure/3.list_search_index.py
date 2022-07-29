
a = [4, 67, 33, 1, 10, 777,51]
s = int(input()) or '찾을 인덱스가 입력되지 않았습니다'


def search_index(n, target):
    for i in range(len(n)):
        if n[i] == target:
            return i
    return -1
    
print(search_index(a, s))