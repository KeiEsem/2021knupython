# for문 무작정 따라해보기
for i in range(5, 20) : # 뒷자리 숫자는 빼고 실행된다
    if (i%2 == 0):
     print(i,"은/는 짝수입니다.")
    else:
     print(i, "은/는 홀수입니다.")

# for문의 구조
# for i in 범위:
#     반복할 명령어1
#     반복할 명령어2

#for문 with list
mylist = ['강정우', '정유경', '김동우']
for i in mylist:
    print(i)
print("반복 끝")

# print list with range
print(range(1,11)) # start 기본값은 0
print(list(range(1,11))) # step 기본값은 1
print(list(range(1,20,3))) # 3칸씩 띄어서 프린트한다
print(list(range(20,0,-3))) # -3씩 줄어들어서 프린트한다

# for문 with range
for i in range(1,11):
 print(i, end= " ") # space 를 넣는 것
print("반복 끝")