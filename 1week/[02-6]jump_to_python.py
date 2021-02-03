# 02-6
def next():
    print("\n")
"""
집합 자료형
"""
s1 = set([1,2,3])
print(s1)
s1 = set("Hello")
print(s1)
next()
# 집합형 자료형 set키워드
# 그런데 뭔가 이상하다.
# set은 중복을 허용하지 않고 순서가 없다.
# 따라서 인덱싱이 불가능하다.

s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])
next()
# 따라서 위와 같이 인덱싱을 위해서는 튜플이나 리스트로 변환해야 한다.


"""
교집합, 합집합, 차집합 구하기
set 자료형을 쓰는 이유는 이러한 것들을 구할 수 있기 때문이다.
"""

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))
# set의 교집합

print(s1 | s2)
print(s1.union(s2))
# set의 합집합

print(s1 - s2)
print(s1.difference(s2))
# set의 차집합
next()


"집합 자료형 관련 함수들"

s1 = set([1,2,3])
s1.add(4)
print(s1)
# 값 1개 추가하기 add

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
# 값 여러개 추가하기 update

s1 = set([1,2,3])
s1.remove(2)
print(s1)
# 특정 값 제거하기 remove