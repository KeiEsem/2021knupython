# ㄹfor와 while의 차이
# for문은 정해진 횟수만큼 돌린다
# while문은 정해진 목표까지 돌린다. -> 조건이 참인 경우

# while문 기초
it = 0
while it < 5 :
    it +=1
    print(it)

# while문 구조
# while 조건:
#   반복할 명령어 1
#   반복할 명령어 2

# while 무한루프 (overflow) (잠깐 #으로 비활성화 시켰다)
# it = 0
# while True :
#    it += 1
#    print(it) #무한루프는 ctrl + c 눌러서 멈춰라. 놔두면은 터질때까지 반복한다.

# while 무한루프 + break
it = 0
while True :
    it += 1
    print(it)
    if it > 500 :
        break # 500을 넘으니까 스스로 멈춘다. 기가 막힌다!
