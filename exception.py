#!/usr/bin/env python
# coding: utf-8

# In[5]:


#GESTION DES EXCEPTIONS

int(input("Entrez la valeur de x : "))
def polynome(x):
    return x**3 -1.5*x**2-6*x+5
             
print("Le résultat est de :",polynome(x) )

        try:
            x = int(input ("entrez la valeur de x"))
             while (x in range (0,1)):
                raise Exception("la valeur de x trop petite !")
        except :


# La valeur est trés grand

int(input("Entrez la valeur de x : "))
def polynome(x):
    return x**3 -1.5*x**2-6*x+5
        try:
          x = int(input ("entrez la valeur de x "))
            while (x in range (0,10000)):
                raise Exception("la valeur de x très grande !")
        except :


# In[ ]:





# In[ ]:




