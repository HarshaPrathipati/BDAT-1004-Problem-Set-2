#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# # Question 1

# In[2]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2


# In[3]:


b()


# In[4]:


b()


# In[5]:


b()


# In[6]:


a


# Value displayed is 6. Since we have executed 'b()' method/function, it calls the function 'c()' and increments the value of 'a' by 2. So, after we call the function 'b()' 3 times, the value of 'a' becomes 2+2+2 i.e, 6. 

# # Question 2

# In[64]:


def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        print(len(contents))
        file.close()
    except FileNotFoundError:
        print("File" +" "+ file_name +" "+"not found")
   
   


# In[65]:


file_length(r"C:\Users\Haritasa\Downloads\FurnitureProblem2.py")


# In[66]:


file_length(r"C:\Users\Haritasa\Downloads\FurnitureProblem24.py")


# # Question 3 

# In[113]:


class Marsupial(object):
    def __init__(self):
        self.pouch_contents = []
    
    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)
    
    def __str__(self):
        return self.pouch_contents
    


# In[114]:


m = Marsupial()


# In[115]:


m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')


# In[116]:


m.pouch_contents


# In[ ]:


class Kangaroo(Marsupial):
    


# # Question 4

# In[60]:


def collatz(x):
    print(x)
    while x>1:
        if x % 2 == 0:
            print(x//2)
            x = x //2
        elif x % 2 ==1:
            print(3*x+1)
            x = 3*x+1
        else:
            print(x)
collatz(1)
print('------------')
collatz(10)


# # Question 5

# In[13]:


l=[]
def binary(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    binary(b//2)
a=int(input("Enter a number: "))
binary(a)
print("Binary equivalent:")
for i in l:
    print(i,end="")


# # Question 6

# In[64]:


from html.parser import HTMLParser
class HeadingParser(HTMLParser):
    def handle_data(self, data):
            print(data)


# In[65]:


parser= HeadingParser()
parser.feed('<!DOCTYPE html><html lang="en"><head><meta name="description" content="Webpage description goes here" /><meta charset="utf-8"><title>Change_me</title><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="author" content=""><link rel="stylesheet" href="css/style.css"></head><body><h1>W3C Mission</h1><h2>Principles</h2></body></html>')


# # Question 8
# 

# In[ ]:


a) Select Temperature from table;
b) Select Distinct City from table;
c) Select * from table where Country='India';
d) Select Rainfall from table;
e) Select City, Country, Season from table where Rainfall BETWEEN 200 AND 400;
f) Select City, Country from table where AVG(Temperature)>20;
g) Select SUM(Rainfall) from table where City='Cairo';
h) Select Season, SUM(Rainfall) from table GROUP BY Season;


# # Question 9

# In[14]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']


# In[18]:


list1= [i.upper() for i in words]
print(list1)


# In[20]:


list2=[i.lower() for i in words]
print(list2)


# In[21]:


list3= [len(i) for i in words]
print(list3)


# In[37]:


list4= [[i.upper(),i.lower(),len(i)] for i in words]
print(list4)


# In[29]:


list5= [i for i in words if len(i)>=4]
print(list5)

