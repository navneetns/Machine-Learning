#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


X = np.arange(10)
Y = (X-5)**2
print(X,Y)


# In[3]:


Goal Given a Function f(x), we want to find the value of x that minimizes f.

Visualisation


# In[4]:



plt.style.use("seaborn")
plt.plot(X,Y)
plt.ylabel("F(X)")
plt.xlabel("X")
plt.show()


# In[5]:


x = 0
lr = 0.1
error = []
# 50 steps in the downhill direction
plt.plot(X,Y)

for i in range(50):
    grad = 2*(x-5)
    x = x - lr*grad
    y = (x-5)**2
    error.append(y)
    plt.scatter(x,y)
    print(x)


# In[6]:


# Plot the values of error

plt.plot(error)
plt.show()


# In[ ]:




