#!/usr/bin/env python
# coding: utf-8

# # **04-1 함수**

# In[33]:


def add(a,b):
    return a+b


# In[34]:


a = 3
b = 4
c = add(a,b)
print(c)


# In[35]:


print(add(3,4))


# ### 입력값이 없는 함수

# In[47]:


def say():
    return "HI"


# In[48]:


a = say()


# In[49]:


print(a)


# ### 결괏값이 없는 함수

# In[44]:


def adde(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))


# In[45]:


adde(3,4)


# In[46]:


a = adde(3,4)
print(a)


# 위 형식은 print(a)에 adde함수의 결괏값이 없기 때문에 오류가 발생한 결과이다.

# ### 입력값도 결괏값도 없는 함수

# In[50]:


def say():
    print('Hi')


# In[51]:


say()


# ### 매개변수 지정하여 호출하기

# In[52]:


def add(a,b):
    return a+b


# In[53]:


result = add(a=3,b=7)
print(result)


# In[54]:


result = add(b=4,a=4)
print(result)


# 위와 같이 순서에도 상관이 없다.

# ### 입력값이 몇 개가 될지 모를 때는?

# In[55]:


def add_many(*args):
    result = 0
    for i in args:
        result = result +i
    return result


# *을 붙이면 입력값을 전부 모아서 튜플로 만들어준다 즉, add_many(1,2,3)에서 args = (1,2,3)이 된다

# In[56]:


result = add_many(1,2,3)
print(result)


# In[58]:


result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


# In[77]:


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


# In[78]:


result = add_mul("add", 1,2,3,4,5)
print(result)


# In[79]:


result = add_mul("mul", 1,2,3,4,5)
print(result)


# ### 키워드 파라미터 kwargs

# In[80]:


def print_kwargs(**kwargs):
    print(kwargs)


# In[81]:


print_kwargs(a=1)


# In[82]:


print_kwargs(name='foo',age=3)


# 위처럼 a=1이나 name='foo',age=3이 모두 딕셔너리로 만들어진다. 이처럼 매개변수 앞에 **을 넣으면 딕셔너리가 된다.

# ### 함수의 결괏값은 언제나 하나이다.

# In[83]:


def add_and_mul(a,b):
    return a+b, a*b


# In[87]:


result = add_and_mul(3,5)
print(result)


# 이처럼 만약 return a,b로 한다면 결괏값은 튜플이 되어 나온다.

# In[89]:


def add_and_mul(a,b):
    return a+b
    return a*b


# In[90]:


result = add_and_mul(3,5)
print(result)


# 이처럼 만약 return문을 두개 사용한다면 하나만 나오게 된다.

# ### return의 또 다른 쓰임새

# In[92]:


def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다" %nick)


# In[93]:


say_nick('야호')


# In[94]:


say_nick('바보')


# **이처럼 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 아주 자주 사용한다.**

# ### 매개변수에 초깃값 미리 설정하기

# In[96]:


def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# In[97]:


say_myself("박응용",27)


# In[98]:


say_myself("박응용",27,False)


# In[100]:


def say_myself2(name, man=True, old): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old)
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")


# 이처럼 매개변수의 순서를 바꾸게 되면 초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정하지 않은 매개변수는 사용할 수 없다는 오류가 발생하게 된다.

# 항상 초기화하고 싶은 매개변수를 뒤쪽에 놓는 것을 잊지 말자.

# ### 함수 안에서 선언한 변수의 효력 범위

# In[101]:


a = 1
def vartest(a):
    a=a+1

vartest(a)
print(a)


# 위 결과는 2가 아닌 1 이다. 그 이유는 함수 안에서는 a가 2가 되지만 함수를 호출하고 난 뒤에는 print(a)가 받아야 하는 a 변수가 없기 때문에 원래의 a가 나오게 되는 것이다. 이처럼 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 밖에서는 사용되지 않는다.

# ### 함수 안에서 함수 밖의 변수를 변경하는 방법

# In[107]:


a = 1
def vartest(a):
    a = a+1
    return a

a = vartest2(a)
print(a)


# In[108]:


a = 1
def vartest():
    global a
    a = a+1
    
vartest()
print(a)


# return문과 global명령어를 사용하면 위처럼 함수 안에서 밖의 변수를 변경 할 수 있다.

# ### lambda

# In[109]:


add = lambda a,b:a+b
result = add(3,4)
print(result)


# In[111]:


def add(a,b):
    return a+b

result = add(3,4)
print(result)


# 위 두 함수는 같은 함수이다. lambda함수를 사용해도 동일한 효과를 낼 수 있다.
