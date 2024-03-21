
# coding: utf-8

# In[13]:


## primitive datatype


# In[14]:


age =int(input("Enter your age"))


# In[15]:


print(age)


# In[1]:


fnum = float(input("Enter a decimal number"))


# In[2]:


print(fnum)


# In[3]:


Bolean = bool(input("Enter true or false"))


# In[4]:


print(type(Bolean))


# ################### usage of String functions ###########

# In[5]:


name ="my name is Anil kumar#67140"


# In[7]:


## 1 capitalize() function
print("capitalize function:- " +name.capitalize())
## 2 count() function
print("count():- "+str(name.count("m")))
## 3 find() function
print("find() :- "+ str(name.find("#")))
## 4 index() function
print("index() :- "+ str(name.index("#")))


# In[12]:


## 5 isalnum()
print("isalnum():- "+str(name.isalnum()))
##6  isalpha()
print("isalpha():- "+str(name.isalpha()))
## 7is decimal()
print("isdecimal:- "+str(name.isdecimal()))
## 8  isdigit()
print("isdigit():- "+str(name.isdigit()))
## 9 lower()
print("lower():-"+name.lower())
## 10 upper()
print("upper():- "+ name.upper())
##
print("swapcase():- "+ name.swapcase())


# In[9]:


#### string slicing extraction , indexcing
print("print first two letters :- "+name[0:2])
print("print by  skippping to letters:-  " +name[0: :2])
print("print in reverse order:-  " +name[-1::-1])


# In[10]:


##### split method
print("split method:- "+ str( name.split("#")))

