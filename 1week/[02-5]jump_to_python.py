# 02-5
def next():
    print("\n")
"""
딕셔너리란?
key와 value로 이루어진 연관 배열 또는 Hash

{Key1:Value1, Key2:Value2, Key3:Value3, ...}
이것이 딕셔너리의 모습이다.
"""

dic = {'name':'honghyuck', 'phone':'01040403848', 'birth':'0908' }
# 실제 딕셔너리의 예 이며 Value에 리스트또한 넣을 수 있다.

a = {1:'hi'}
a = {'a':[1,2,3]}
# 위 예처럼 Value에 리스트도 넣을 수 있다.


"딕셔너리 쌍 추가, 삭제하기"

a = {1:'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)
# 딕셔너리 쌍 추가 (list)도 추가 가능하다.
next()

del a[1]
print(a)
# 딕셔너리 요소 삭제하기 del 사용
next()


"딕셔너리에서 Key 사용해 Value 얻기"

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a',2:'b'}
print(a[1],a[2])
# 딕셔너리에서 key를 사용해 value를 불러오는 모습
# 주의할 점은 key로 list사용 불가, key를 중첩사용 불가 라는 것이다.
next()


"""
딕셔너리 관련 함수들

python 2.7 까지는 a.keys() 함수를 호출시 
반환값으로dick_keys가 아닌 리스트를 돌려준다.
이 경우 메모리 낭비가 발생하는데 3.0이후 버전에서는 메모리 낭비를 줄이기 위해
dick_keys 객체를 돌려준다.
"""
a = {'name':'honghyuck', 'phone':'01040403848', 'birth':'0908' }
for k in a.keys():
    print(k)
next()
# dict_keys는 위처럼 사용 가능. 리스트와 비슷하지만 리스트 고유 함수 사용 불가.

print(list(a.keys()))
next()
# 만약 dict_keys 객체를 리스트로 변환하고자 하면 이렇게 하면 된다.

print(a.values())
# key값이 아닌 value들의 값을 알고 싶다면 이렇게 하면 된다.

print(a.items())
print(a)
next()
# key, value값들을 모두 알고 싶다면 이렇게 하면 된다.

a.clear()
print(a)
next()
# key : value값 쌍으로 모두 지우기

a = {'name':'honghyuck', 'phone':'01040403848', 'birth':'0908' }
print(a.get('name'))
print(a.get('phone'))
# key로 Value 얻기(get)
# 단, 존재하지 않는 키를 가져올때 a['nokey']는 Key 오류를 발생시키고
# a.get('nokey')는 None을 돌려준다는 차이가 있다.

print(a.get('foo','default'))
next()
# get함수 사용시 이처럼 none대신 다른 값이 디폴트로 오도록 설정 가능하다.


print('name' in a)
print('email' in a)
# 해당 key가 딕셔너리 안에 있는지 조사하기 in