# 02-3
def next():
    print("\n")

"""
리스트는 어떻게 만들고 사용할까?
"""

odd = [1,3,5,7,9]
#리스트를 만들 때는 위처럼 대괄호로 감싸주고 쉼표로 구분한다

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
# 리스트는 리스트자체, 문자열, 숫자 모두 요솟값으로 가질 수 있다.

a = list()
# 빈 리스트는 이처럼 생성이 가능하다


"리스트의 인덱싱과 슬라이싱"

a = [1,2,3]
print(a)
next()
print(a[0],a[1],a[-1])
# 리스트의 인덱싱

print(a[1]+a[2])
# 리스트 인덱싱 연산

a = [1,2,3,['a','b','c']]
print(a[-1],a[1])
# 중첩 리스트

print(a[-1][2])
next()
# 중첩 리스트 요소 뽑기

a = [1,2,3,4,5]
print(a[0:2])
# 리스트의 슬라이싱

a = "12345"
print(a[0:2])
# 이는 문자열의 슬라이싱과 동일하다

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])
next()
# 중첩된 리스트에서 슬라이싱 하기


"리스트 연산하기"

a = [1,2,3]
b = [4,5,6]
print(a+b)
# 리스트 더하기

print(a*3)
# 리스트 반복하기

print(len(a))
# 리스트 길이 구하기
next()


"리스트의 수정과 삭제"

a = [1,2,3]
a[2] = 4
print(a)
# 리스트에서 값 수정하기

del a[1]
print(a)
# del 함수 사용해 리스트 요소 삭제하기

del a[:2]
print(a)
# del 함수 사용해 리스트 요소들 삭제하기
next()


"리스트 관련 함수"

a = [1,2,3]
a.append(4)
print(a)
# 리스트에 요소 추가 append
a.append([5,6])
# 리스트에 다시 리스트를 추가
print(a)
next()

a = [1,3,2,5,4]
a.sort()
print(a)
next()
# 리스트 정렬 sort

a = ['a','c','b']
a.reverse()
print(a)
next()
# 리스트 뒤집기 reverce

a = [1,2,3]
print(a.index(3))
# 위치 반환 index
# 리스트에 x 값이 있으면 x의 위치 값을 돌려준다
"print(a.index(k))"
next()
# 하지만 리스트에 값이 존재하지 않으면 오류가 발생한다.


a = [1,2,3]
a.insert(0,4)
print(a)
next()
# 리스트의 a번째 위치에 b값을 삽입하는 함수 insert

a = [1,2,3,4,5,6,7]
a.remove(4)
print(a)
next()
# 리스트의 요소를 지우는 함수. 만약 리스트에 요소가 복수개이면 첫번째 요소만 제거

a = [1,2,3]
print(a.pop())
print(a)
next()
# 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다 pop

a = [1,2,3]
print(a.pop(1))
print(a)
next()
# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.

a = [1,2,3,1]
print(a.count(1))
next()
# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수

a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)
# extend(x)에서 x는 리스트만 올 수 있으며 원래의 a리스트에 x리스트를 더하게 된다.

