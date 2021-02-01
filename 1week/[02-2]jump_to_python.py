# 02-2
# 파이썬에서 문자열을 만드는 방법은 총 4가지가 있다.
def next():
    print("\n")
# 1. 큰 따옴표 (")로 양쪽 둘러싸기
"Hello World"
# 2. 작은 따옴표(')로 양쪽 둘러싸기
'Python is fun'
# 3. 큰 따옴표 (""")으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
# 4. 작은 따옴표(''')으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''


"""
Why? 4가지 방법이 있을까?
문자열 안에 작은따옴표와 큰따옴표가 들어 있어야 할 경우가 있다. 이 때는 좀 더 특별한 기술이 필요하다.
"""

# 1. 문자열 안에 작은따옴표 (')포함시키기
food = "Python's favorite food is perl"
# 2. 문자열 안에 큰따옴표 (")포함시키기
say = '"Python is very easy." he says.'
# 3. 백슬래시\ 를 사용해서 작은따옴표(') 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy. \" he says."
print(food)
next()


"여러줄인 문자열을 변수에 대입하고 싶을 때"

# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline1 = "Life is too short\nYou need python"
# 2. 연속된 작은따옴표 3개(''')또는 큰따옴표 3개("""")사용하기
multiline2 = '''
Life is too short
You need python
'''
multiline3 = """
Life is too short
You need python
"""
print(multiline3)
next()


"문자열 연산하기"

head = "Python"
tail = " is fun!"
print(head + tail)
next()
# 문자열 더해서 연결하기

a = "python"
print(a*2)
next()
# 문자열 곱하기

print("=" * 50)
print("My Program")
print("=" * 50)
next()
# 문자열 곱하기 응용

a = "Life is too short"
print(len(a))
next()
# 문자열 길이 구하기


"문자열 인덱싱과 슬라이드"

a = "Life is too short, You need Python"
print(a[3],a[-1],a[-5])
next()
# 문자열 인덱싱

b = a[0] + a[1] + a[2] + a[3]
print(b)
next()
print(a[0:4])
next()
# 문자열 슬라이싱

a = "20200201Ranny"
data = a[:8]
weather = a[8:]
year = a[:4]
day = a[4:8]
print(data)
print(weather)
next()
# 슬라이싱으로 문자열 나누기


"""
문자열 포매팅
포매팅이란 문자열 안에 어떤 값을 삽입하는 방법이다.
"""

print("I eat %d apples." %3)
# 숫자 바로 대입

print("I eat %s apples." %"five")
# 문자열 바로 대입

number = 3
print("I eat %d apples." %number)
next()
# 숫자 값을 나타내는 변수로 대입

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number,day))
# 2개 이상의 값 넣기

print("I have %s apples" %3.213)
# %s의 경우 재밌게도 어떤 형태의 값이든 문자열로 넣을수 있게된다

#print("error is %d%" %98)
print("error is %d%%" %98)
#위 예시는 잘못된 포매팅 연산이다. %를 사용하고 싶다면 %%와 같이 두개를 사용해야 한다.


"""
포맷 코드와 숫자 함께 사용하기
%d, %s 등의 포맷 코드는 문자열 안에 어떤 값을 삽입하기 위함이다. 하지만 포맷 코드를 숫자와 함께 사용하면 더 유용하게 사용할 수 있다.
"""

print("%10s" %"hi")
# 전체길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞은 공백

print("%-10sjane." % 'hi')
# 전체길이가 10개인 문자열 공간에서 대입되는 값을 왼쪽으로 정렬

print("%0.2f" % 3.42134234)
# 소수점 네번째 자리까지만 표시

print("%10.4f" % 4.2134234)
# 소수점 네번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬


"format 함수를 사용한 포매팅"

print("I eat {0} apples" .format(3))
print("I eat {0} apples" .format("five"))
number = 3
print("I eat {0} apples" .format(number))
next()
# format 함수를 사용해서 포매팅을 한 예시

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))
# 2개 이상의 값 넣기

print("I ate {number} apples. so I was sick for {day} days." .format(number=10,day=3))
# 이름으로 넣기 {name}의 경우 반드시 name=value와 같은 형태의 입력이어야 한다.

print("I ate {0} apples. so I was sick for{day} days." .format(10, day=3))
next()
# 이렇게 혼용해서 사용해도 가능하다.

print("{0:<10}" .format("hi"))
# 왼쪽 정렬하고 총 자릿수를 10으로 맞추기

print("{0:>10}" .format("hi"))
# 오른쪽 정렬하고 총 자릿수를 10으로 맞추기

print("{0:^10}" .format("hi"))
# 가운데 정렬하고 총 자릿수를 10으로 맞추기

print("{0:=^10}" .format("hi"))
# 공백 채우기 =기호는 다른 기호로 대체 가능

y=3.423142
print("{0:10.4f}" .format(y))
# 소수점 표현하기

print("{{and}}" .format())
# format 함수를 사용해 문자열 포매팅을 할 경우 {}와 같은 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우 


"""
f 문자열 포매팅
이 기능은 파이썬 3.6 버전 이하는 사용할 수 없으니 버전 관리에 주의
"""

name = '홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
# 이처럼 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.

print(f"나의 이름은 {name}입니다. 나이는 {age-3}입니다.")
next()
# 딕셔너리는 f 문자열 포매팅에서 다음과같이 사용 가능하다.

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
next()
# 정렬은 다음과 같이 사용이 가능하다.

print(f'{"hi":=<10}')
print(f'{"hi":!>10}')
print(f'{"hi":%^10}')
next()
# 공백 채우기는 다음과 같이 할 수 있다.

print(f'{y:0.4f}')
# 소수점은 다음과 같이 사용이 가능하다.

print(f'{{and}}')
next()
# f문자열 포매팅을 사용한 {}괄호 사용


"""
문자열 관련 함수들
"""

a = "hobby"
print(a.count('b'))
# 문자 개수 세기 count

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
# 문자 위치 알려주기1 find 문자열중 처음으로 나온 위치를, 없다면 -1을 반환한다

a = "Life is too short"
print(a.index('t'))
next()
# 문자 위치 알려주기2 index 문자열중 처음으로 나온 위치를 반환하지만 없다면 오류가 발생한다.

print(",".join('abcd'))
print(",".join(['a','b','c','d']))
next()
# 문자열 삽입 join 앞으로 사용할 일이 많다.

a ="hi"
print(a.upper())
# 소문자를 대문자로 바꾸기 upper

a ="HI"
print(a.lower())
next()
# 대문자를 소문자로 바꾸기 lower

a = " hi "
print(a.strip())
# 양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life","Your leg"))
next()
# 문자열 바꾸기

a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))
# 문자열 나누기