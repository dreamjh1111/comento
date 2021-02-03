"""
Q1 문자열 바꾸기
다음과 같은 문자열이 있다.
a:b:c:d
문자열의 split와 join함수를 사용하여 위 문자열을 다음과 같이 고쳐라
a#b#c#d


Q2 리스트 총합 구하기
다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총 합을 구하시오.
A=[20,55,67,82,45,33,90,87,100,25]

Q3 피보나치 함수
첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.
0,1,1,2,3,5,8,13,.....
입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
"""

# Q1
a = "a:b:c:d"
print(a)
a = "#".join(a.split(':'))
print(a)


# Q2
A = [20,55,67,82,45,33,90,87,100,25]
sum = 0
for score in A:
    if score >= 50:
        sum = sum+score
    else:
        continue
print(sum)


# Q3
a = int(input())
fir_num = 0
sec_num = 1
print(fir_num, end=", ")
print(sec_num, end=", ")
while True:
    Fibonacci = fir_num + sec_num
    if Fibonacci > a:
        break
    print(Fibonacci,end = ', ')
    fir_num = sec_num
    sec_num = Fibonacci

