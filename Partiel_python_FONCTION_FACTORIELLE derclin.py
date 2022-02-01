#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as np
import pandas as pd
from math import sqrt


# In[ ]:


def factorielle(n):
    """"la fonction récursive trouve la factorielle du nombre donné"""
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)
# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre: "))
if n < 0:
    print("Factoriel ne peut être trouvé pour les nombres négatifs")
elif n == 0:
    print("Factorielle de 0 est 1")
    
else:
  print("Factorielle de", n, "est: ", factorielle(n))
    

