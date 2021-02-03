#!/usr/bin/env python
# coding: utf-8

# # 04-3 파일 읽고 쓰기

# ### 파일 생성하기

# In[2]:


f = open("새파일.txt", 'w')
f.close()


# 파일을 생성하기 위해 open 함수 사용. 그후 r = 읽기모드 w = 쓰기모드 a = 추가모드(파일의 마지막에 새로운 내용을 추가)

# In[3]:


f = open("C:/doit/새파일.txt",'w')
f.close()


# 위처럼 경로를 사용하여 원하는 곳에 파일을 만들 수 있다. 또한 f.close()는 열려있는 파일 객체를 닫아준다. 하지만 생략해도 파이썬 프로그램을 닫으면 자동으로 파일의 객체를 닫아준다.

# ### 파일을 쓰기 모드로 열어 출력값 적기

# In[9]:


f = open("새파일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n"%i
    f.write(data)
f.close()


# ## 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

# ### readline 함수 이용하기

# In[8]:


f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()


# ### read 함수 사용하기

# In[5]:


f = open("새파일.txt",'r')
data = f.read()
print(data)
f.close()


# ## 파일에 새로운 내용 추가하기

# In[10]:


f = open("새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()


# ## with문과 함께 사용하기

# In[11]:


with open("새파일.txt", "w") as f:
    f.write("Life is too short, you need python")


# ### sys모듈로 매개변수 주기

# In[12]:


import sys

args = sys.argv[1:]
for i in args:
    print(i)


# In[ ]:




