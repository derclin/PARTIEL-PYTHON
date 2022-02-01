#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#c) Implémenter la suite de Fibonnaci 
"""Python : Suite de Fibonacci. """

n = int(input("Entrer un entier supérieur à 1:"))  #  Par exemple, 4


fibo = [0]*(n)

fibo[0] = 0

fibo[1] = 1


for i in range(2,n):

  fibo[i] = fibo[i-1] + fibo[i-2]


print(fibo)

