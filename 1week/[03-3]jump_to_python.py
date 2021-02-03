#!/usr/bin/env python
# coding: utf-8

# # for문 시작
# 

# In[7]:


def next():
    print("\n")


# In[8]:


test_list = ['one','two','three']
for i in test_list:
    print(i)


# In[15]:


a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)


# In[18]:


marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark >=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격 입니다."%number)


# In[19]:


marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)


# ## for문과 함께 자주 사용하는 range 함수

# In[26]:


a = range(0,10)


# In[27]:


a


# In[28]:


a = range(1,11)
a


# range(시작 숫자, 끝 숫자)에 형태에서 *끝숫자* 는 포함하지 않는다.

# In[30]:


add = 0
for i in range(1,11):
    add = add+i
print(add)


# In[31]:


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# In[37]:


for i in range(2,10):
    for j in range(1,10):
        print(i*j,end="/")
    print("")


# end=""을 넣어준 이유는 결괏값을 출력시 다음줄로 넘기지 않고 그 줄에 계속 출력하기 위해서이다.

# ## 리스트 내포 사용하기

# In[38]:


a=[1,2,3,4]
result = []
for num in a :
    result.append(num*3)
    
print(result)


# In[39]:


a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


# In[40]:


a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 ==0]
print(result)


# In[41]:


result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)


# In[ ]:




