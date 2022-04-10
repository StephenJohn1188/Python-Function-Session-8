#!/usr/bin/env python
# coding: utf-8

# Variable Number of Arguments

# In[2]:


def plus(*args):
    return sum(args)


# In[3]:


plus(2,3,5,7,8)


# In[6]:


def mu(*al):
    return max(al)


# In[7]:


mu(387,434,233,4343)


# In[8]:


def mu(*al):
    return min(al)


# In[9]:


mu(387,434,233,4343)


# In[14]:


def sumfunc(*number):
    s=0
    for n in number:
        s+=n
    return s


# In[15]:


print(sumfunc(1,2,3))


# In[16]:


print(sumfunc(3,42,12))


# Anonyumous Function Lambda

# In[17]:


test = lambda var1:var1*2
test(5)


# In[18]:


test2 = lambda x,y:x+y
test2(6,7)


# In[21]:


test3 = lambda x,y,z:x+y+z
test3(35,354,3456)


# In[23]:


square = lambda x:x**2
square(12)


# In[24]:


sqroot = lambda x:x**(1/2)
sqroot(9)


# In[26]:


cube = lambda x:x**3
cube(9)


# In[27]:


curoot = lambda x:x**(1/3)
curoot(27)


# In[28]:


add = lambda x,y:x+y
print("Total Value: ", add(5,10))
print("Total Value:", add(45,56))


# In[29]:


def FH(T):
    return((9/5)*T+32)


# In[31]:


F=FH(55)
F


# In[36]:


def CEL(T):
    return ((5)/9)*(T-32)


# In[37]:


C=CEL(131)
C


# In[38]:


FH = lambda x:(9/5)*x+32
FH(55)


# In[40]:


CEL = lambda x:(5/9)*(x-32)
CEL(131)


# In[41]:


mylist=[1,2,3,4]


# In[ ]:





# In[ ]:




