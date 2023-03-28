#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Student :
    __name = __kor = __eng = __math = __tot = __avg = __grade = None
    def __init__(self, name, kor, eng, math):  
        """Student class의 Constructor"""
        Student.__name = name
        Student.__kor = kor
        Student.__eng = eng
        Student.__math = math
        
    @property
    def name(self): return Student.__name
    @property
    def kor(self):return Student.__kor
    @property
    def eng (self):return Student.__eng
    @property
    def math (self):return Student.__math
    @property
    def tot(self):return Student.__tot
    @property
    def avg(self):return Student.__avg
    @property
    def grade(self):return Student.__grade
    @tot.setter
    def tot(self, tot): Student.__tot = tot
    @avg.setter
    def avg(self, avg): Student.__avg = avg
    @grade.setter
    def grade(self, grade): Student.__grade = grade

