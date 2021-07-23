# 홍길동씨 개인정보 
name = "홍길동"
age = 25
height = 184.6
print(type(name))
print(type(age))
print(type(height))

# 변수 이름 짓는 규칙
# 1. 영문자(대소문자 구분), 숫자, 언더바, 한글 사용 가능
# age, Age, age3, 나이, 나이3 ...
# 2. 첫 자리에는 숫자 안된다.
# 3. 파이썬에서 자체적으로 사용하는 단어(예약어) 사용 불가
# True, If, While

# Convention, 파이썬 PEP-8
# 변수 이름 짓는 조직 내부의 룰
# 1. 한 단어로 된 변수는 소문자로
# age, good, name
# 2. 두 단어 이상의 변수는 언더바로
# my_name, my_frieind_name

# 3. 예약어와 충돌하는 경우에는 뒤에 언더바
# if_, time_

# 4. 상수의 경우 대문자와 언더바를 혼용하여 쓴다
# TOTAL, MAX_NUM, AVG