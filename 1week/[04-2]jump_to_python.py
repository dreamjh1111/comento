#!/usr/bin/env python
# coding: utf-8

# # 04-2 사용자 입력과 출력

# ## 사용자 입력

# ### input의 사용

# In[1]:


a = input()


# In[3]:


a


# ### 프롬프트를 띄워서 사용자 입력 받기

# In[4]:


number = input("숫자를 입력하세요: ")


# ### print 자세히 알기

# In[5]:


a = 123
print(a)


# In[6]:


a = 'python'


# In[7]:


print(a)


# In[8]:


a = [1,2,3]


# In[9]:


print(a)


# ### 큰 따옴표로 둘러싸인 문자열은 +연산과 동일하다.

# In[10]:


print("life" "is" "too short")


# In[11]:


print("life"+"is"+"too short")


# ### 문자열 띄어쓰기는 콤마로 한다.

# In[12]:


print("life", "is", "too short")


# ### 한 줄에 결괏값 출력하기

# In[13]:


for i in range(10):
    print(i,end='')
    


# 03-3에서 for문을 배울 때 만들었던 구구단 프로그램에서 보았듯이 한 줄에 결괏값을 계속 출력하려면 매개변수 end를 사용하면 문자 뒤에 오는 값을 정할 수 있다.
