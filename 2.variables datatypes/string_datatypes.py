# 기본 문자열
s2 = 'Hello, KeiEsem!'
print(s2)
S2 = "Hello, KeiEsem!"
print(S2)
s6 = '''Hello, KeiEsem!'''
print(s6)
S6 = '""Hello,KeiEsem!""'
print(S6)

# 이스케이프 코드
# \n(줄바꿈)  \t(탭 누르기) \\(백슬래시 자체 누르기) \' \"
longtest1 = """hello, KeiEsem!
My Name Is KeiEsem Slave."""
print(longtest1)
# 따옴표가 하나일 때는 내가 직접 줄바꿈하면 신택스에러? 가 뜬다. 그러니 이스케이프코드 사용   
longtest2 = 'hello, KeiEsem!\nMy Name Is KeiEsem Slave.'
print(longtest2)

# String Interpolation (문자열로 만들어서 출력한대)
a = 123
new_q = f'{a}' # 중괄호 써라 좀!  
print(new_q)

# 문자열 옛날 방식. 결과가 나오긴 하지만 많이 불편했었음
print(f'%s %s' % ('one', 'two'))

# 발전형-pyformat 이건 중괄호 안에 뭐든 넣어도 인식됨
print( '{} {} '. format('one', 'two'))

# f-string (강사님이 혁신이라고, 개쩐다고 하시는데 난 잘 모르겠다~)
a, b = 'one', 'two'
print(f'{a} {b}')
print(f'{b} {a}')

# example
name = "케이에셈"
eng_name = "KeiEsem"
print("안녕하세요, {1}입니다. My name is {0}".format(eng_name, name))
print(f'안녕하세요. {name}입니다')

# 문자열 인덱싱
a = 'Hello, KeiEsem!'
print(a[1]) #1

# 문자열 슬라이싱
a = 'Hello, KeiEsem!'
print(a[4:9]) # 공백을 포함해서 o, Ke 가 나올것

# 문자열의 길이를 구하는 len()
print(len(a))

# 문자열의 최대, 최소를 구하는 max(), min() 
# 아스키코드 -> 
a = '312'
b = 'bac'
print(min(a))
print(max(a))
print(min(b))
print(max(b))
print(min(a+b)) # a+b = "312bac" 이니까. 여기서 최소값은 1이라고 뜨네요

# 소문자, 대문자로 변환해주는 lower(), upper()
a = 'This is Apple'
print(a.upper())
print(a.lower())

# 문자열을 구분자에 따라 나누는 split()
a = "안녕,나는,김현묵이야"
print(a.split(sep=',')) # , 를 기준으로 나눈다
b = "안녕 나는 김현묵이야"
print(b.split()) # 위와 결과는 같지만, split 안을 비어있게 둔다면 이는 공백에 따라 나눈것

# 여러 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '김현묵이야']
mystring = '_'. join(mylist)
print(mystring)