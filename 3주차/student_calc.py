#!/usr/bin/env python
# coding: utf-8

# In[1]:


def student_calc(student):
    student.tot = student.kor + student.eng + student.math
    student.avg = student.tot / 3.
    if 90 <= student.avg <= 100 : student.grade = 'A'
    elif 80 <= student.avg < 90 : student.grade = 'B'
    elif 70 <= student.avg < 80 : student.grade = 'C'
    elif 60 <= student.avg < 70 : student.grade = 'D'
    else : student.grade = 'F'

