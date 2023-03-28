#!/usr/bin/env python
# coding: utf-8

# In[1]:


def student_output(student):
    print(f"{student.name:<10s}\t", end='')
    print(f"{student.kor:5d}\t", end='')
    print(f"{student.eng:5d}\t", end='')
    print(f"{student.math:5d}\t", end='')
    print(f"{student.tot:10d}\t", end='')
    print(f"{student.avg:10.2f}\t", end='')
    print(f"{student.grade:10s}")

