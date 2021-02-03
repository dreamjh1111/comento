# 02-8
def next():
    print("\n")
"""
변수는 어떻게 만들까?
"""
a = 1
b = "python"
c = [1,2,3]
# 이처럼 변수는 = 기호를 사용한다.

print(id(a))
# id함수는 변수의 메모리 주소이다.

a = [1,2,3]
b = a
# b변수에 a를 대입하면 
print(id(a))
print(id(b))
# 이처럼 주소는 동일하지만 a가 가리키는 대상과 b의 대상이 동일해진다.

a[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))
# a리스트의 두번째 요소를 바꾸더라도 b까지 바뀌게 된다.


"""변수를 복사하지만 다른 주소를 가리키도록 만드는 방법"""

a = [1,2,3]
b = a[:]
a[1] = 4
print(a,b)
# [:]를 이용한 방법

from copy import copy
b = copy(a)
# b = copy(a)는 b=a[:]와 동일하다.
next()


