#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1-Write a Python program to print the following string in a specific format (see the output).
"""Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

print('Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are')


# In[8]:


# 2. Write a Python program to find out what version of Python you are using.

import sys
print("Python Version ")
print(sys.version)
print("Python Info")
print(sys.version_info)


# In[19]:


# 3. Write a Python program to display the current date and time.

import datetime
now=datetime.datetime.now()
print("the current date and time:")
print('   ',now)


# In[23]:


# 4-Write a Python program that calculates the area of a circle based on the radius entered by the user

from math import pi
r=float(input("enter the radius of the circle: "))
area=pi*r**2
print('the area of acircle =' + str(area))


# In[25]:


# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them

fname=input("enter your first name : ")
lname=input("enter your last name : ")
print('Hallo' +" "+fname+" "+ lname)


# In[28]:


# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers

values=input("some comma separated nubers: ")
list1=values.split(",")
tuple1=tuple(list1)
print("list: ",list1 )
print("tuple : ", tuple1)


# In[31]:


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
filename=input("input a filename : ")
f_extns=filename.split(".")
print("the extension of the file: " +f_extns[-1])


# In[33]:


# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print("the first color: "+ color_list[0])
print('the last color :'+ color_list[-1])


# In[35]:


# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

exam_st_date = (11, 12, 2014)
print('The examination will start from : %i/%i/%i'%exam_st_date)


# In[57]:





# In[ ]:




