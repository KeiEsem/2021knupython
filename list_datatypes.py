# 리스트
# 리스트_이름 = [요소1, 요소2, 요소3 ...]

# KeiEsem Project
Keiesem_character = ["강정우", "정유경", "최현도", "아케인", "김동우"]

# 빈 리스트
mylist = []
print(mylist)

# 파이썬 리스트 특징 = 요소들의 자료형을 통일 안해도 됨
mylist = [1, 2, "강정우", True, ['a', 'b', 'c']]
print(mylist)

# 리스트 인덱싱 (콤퓨타는 앞에서부터 자리를 0,1,2... 순으로 센다)
a = [1,2,3,4,5,6,7,8,9,10]
# 그럼 위의 리스트는 0부터 9까지 있는것
print(a[0]) #1
print(a[5]) #6
print(a[9]) #10

# 음수 인덱싱
print(a[-1]) #10
print(a[-5]) #6

# 리스트 슬라이싱
print(a[0:3]) #1,2,3
print(a[1:3]) #2,3
print(a[:3]) # 3번째 밑으로 다 가져와 (1,2,3)
print(a[7:]) #7번째부터 다 가져와 (8,9,10)
print(a[:]) # 다가져와 (전부)
print(a[-4:-2]) # -4번째이후부터 -2번째까지 (7,8)
# 잘라서 썼지만 a 리스트는 변하지 않는다

# 리스트 수정
a[0] = 100
print(a)
# 맨위의 리스트는 변하지 않아도, 내가 중간에 적은 글 하나때매 변했다.

# 리스트 삭제
del a[0]
print(a)
# 역시 맨위의 리스트는 불변
del a[3:] #3번째 이후를 다 지우는 걸까? 맞다!
print(a)

# 리스트 길이를 구하는 len()
a = [1,2,3,4]
print(len(a)) #4

# 리스트 값을 추가하는 append()
mylist = ['a', 'b', 'c', 'd']
mylist.append('e')
print(mylist)

# 리스트의 값을 정렬해주는 sort()
mylist = [4,2,3,1]
mylist.sort()
print(mylist) #1,2,3,4가 된다!
mylist.sort(reverse=True)
print(mylist)