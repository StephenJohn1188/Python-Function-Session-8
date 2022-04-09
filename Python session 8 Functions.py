#!/usr/bin/env python
# coding: utf-8

# In[1]:


help()


# In[2]:


p=[20,33,54,234,4532,234]


# In[4]:


min(p)


# In[5]:


max(p)


# Functions in Python

# User Defined Functions

# In[6]:


def funtionname():
    print("I am learning Python")
    


# In[7]:


funtionname()


# In[12]:


def function1():
    print("123456")
    


# In[13]:


function1()


# In[14]:


def function2():
    print("I love python")


# In[15]:


function2()


# In[21]:


def add():
    a=20
    b=30
    c=a+b
    print("Sum = ",c)


# In[22]:


add()


# In[24]:


def multiply():
    a=20
    b=30
    c=a*b
    print("Multiply = ",c)


# In[25]:


multiply()


# In[26]:


def area():
    length=1121
    breadth=1232
    area=length*breadth
    print("Area of rectangle= ",area)
    print('Area of rectangle with lenght=',length,'and breadth= ',breadth, 'is', area)


# In[27]:


area()


# In[28]:


def triangle():
    base=568
    height=8484
    area=(1/2)*base*height
    print("Area of triangle is= ", area)
    


# In[29]:


triangle()


# In[30]:


def circle():
    pi=3.14
    radius=1232
    area=pi*radius**2
    print("Area of circle is= ", area)


# In[31]:


circle()


# In[32]:


def add():
    a=int(input("Enter the value of A= "))
    b=int(input("Enter the value of B= "))
    C=a+b
    print("Sum = ",C)


# In[34]:


add()


# In[35]:


def add():
    a=20
    b=30
    c=a+b
    return c


# In[36]:


add()


# In[39]:


p=add()


# In[40]:


p


# In[38]:


add()


# In[46]:


def loop():
    for i in [12,13,14,15,16]:
        print(i)


# In[47]:


loop()


# In[49]:


def append():
    list1=[]
    for i in [100,200,300,400,500,600]:
        list1.append(i)
        print(list1)
    print("Final list= ",list1)
        


# In[51]:


append()


# In[53]:


def looop():
    j=0
    while(j<5):
        print(j)
        j=j+1


# In[54]:


looop()


# In[58]:


def add(a,b):
    c=a+b
    print(c)


# In[60]:


add(30,15)


# In[61]:


add(30,34)

