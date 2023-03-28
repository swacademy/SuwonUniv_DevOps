#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('jupyter nbconvert Student.ipynb --to script')


# In[6]:


import Student
def student_input():
    name = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    math = int(input('수학 : '))
    student = Student.Student(name, kor, eng, math)
    return student

