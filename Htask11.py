#!/usr/bin/env python
# coding: utf-8

# Дана функция:
# 
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 
# 1. Определить корни
# 
# 2. Найти интервалы, на которых функция возрастает
# 
# 3. Найти интервалы, на которых функция убывает
# 
# 4. Построить график
# 
# 5. Вычислить вершину
# 
# 6. Определить промежутки, на котором f > 0
# 
# 7. Определить промежутки, на котором f < 0

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot


# In[5]:


x = Symbol('x')


# In[10]:


fx = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30
fx


# 1. Определить корни уравнения

# In[12]:


plot (fx)


# Функция имеет бесконечное множество корней.
# Найдём корни на заданном интервале.

# In[196]:


interval_point1 = -10
interval_point2 = 10
step = 0.01


# In[197]:


a, b, c, d, e = -11, 7, 1, 5, 12


# In[198]:


x = np.arange(interval_point1, interval_point2, step)


# In[199]:


def func(x) -> tuple:
       return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e


roots1 = []


# In[200]:


def take_roots(a, b, c, d, e):
    roots1 = []
    go_up_down = False
    for x_range in x:
        if go_up_down:
            if func(x_range) >= 0:
                root = np.round(x_range)
                roots1.append(root)
                go_up_down = False
  
        else:
            if func(x_range) <= 0:
                root = np.round(x_range)
                roots1.append(root)
                go_up_down = True

    return roots1
   
roots1 = take_roots(a, b, c, d, e)


zero1 = []


roots1[0] = -7.7
print(roots1)



def roots_list():
    zero =[]
    for i in range(len(roots1)):
        zero.append(0)
    return zero
zero1 = roots_list()
print(zero1)



extremums1 = []
extremums2 = []


# Экстремумы производной - 12*x**4·np.sin(x)·np.cos(np.cos(x)) - 48*x**3*np.sin(np.cos(x)) - 54*x*2 + 10*x + 10
# в точках, где производная равна нулю.
# 

# In[201]:



def derivative(x) -> tuple:
    return 12*x**4*np.sin(x)*np.cos(np.cos(x)) - 48*x**3*np.sin(np.cos(x)) - 54*x*2 + 10*x + 10


def extremum():
    extremums = []
    extr = 0
    go_up_down = False
    for x_range in x:
        if go_up_down:
            if derivative(x_range) >= 0:
                extr = np.round(x_range)
                extremums.append(extr)
                go_up_down = False  
        else:
            if derivative(x_range) <= 0:
                extr = np.round(x_range)
                extremums.append(extr)
                go_up_down = True

    return extremums
   
extremums1 = extremum()
print(extremums1)


# Список значений у экстремумов.

# In[202]:


def x_y_extremum(a, b, c, d, e):
    for i in extremums1:
        temp = np.round(func(i))
        extremums2.append(temp)
    return extremums2
extremums2 = x_y_extremum(a, b, c, d, e)
print(extremums2)



x_down_list = []
x_up_list = []
x_neg_list = []
for i in range(0, len(extremums1)-1, 2):
    x_down = np.arange(extremums1[i], extremums1[i+1], step)
    x_down_list.append(x_down)
for i in range(1, len(extremums1), 2):
    x_up = np.arange(extremums1[i], extremums1[i+1], step)
    x_up_list.append(x_up)    
for i in range(0,len(roots1)-1, 2):
    x_neg = np.arange(roots1[i], roots1[i+1], step)
    x_neg_list.append(x_neg)


# In[205]:


plt.rcParams['lines.linestyle'] = '-'

for i in range(0, len(x_down_list)):
    plt.plot(x_down_list[i], func(x_down_list[i]), 'g')
           
plt.rcParams['lines.linestyle'] = '-'
for i in range(0, len(x_up_list)):

    plt.plot(x_up_list[i], func(x_up_list[i]), 'g')
    
plt.rcParams['lines.linestyle'] = '-'
for i in range(0, len(x_neg_list)):
    plt.plot(x_neg_list[i], func(x_neg_list[i]), 'g')

plt.plot(roots1, zero1, 'ro', label ="Корни")
plt.plot(extremums1, extremums2, 'bo', label ="Экстремумы")
plt.legend()
plt.grid()
plt.show()


# 2. Интервалы, на которых функция возрастает:

# In[212]:


plt.rcParams['lines.linestyle'] = '-.'
for i in range(0, len(x_up_list)):
    plt.plot(x_up_list[i], func(x_up_list[i]), 'r')


# 3. Интервалы, на которых функция убывает:

# In[210]:


plt.rcParams['lines.linestyle'] = '-'

for i in range(0, len(x_down_list)):
    plt.plot(x_down_list[i], func(x_down_list[i]), 'b')


# 6. Промежутки, на котором f < 0

# In[211]:


plt.rcParams['lines.linestyle'] = '-'
for i in range(0, len(x_sub_zero_list)):
    plt.plot(x_sub_zero_list[i], func(x_sub_zero_list[i]), 'g')

