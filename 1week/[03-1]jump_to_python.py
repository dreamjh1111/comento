# 03-1
def next():
    print("\n")

    
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
next()
# if조건문의 예시

money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
next()
# if조건문의 예시2

money = 2000
card = True
if money >3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
next()
# if조건문의 예시3


"""리스트와 튜플을 사용한 예시"""

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
next()


"""다양한 조건을 판단하는 elif"""

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")