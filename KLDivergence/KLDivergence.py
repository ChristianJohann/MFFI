#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def kl_divergence(p, q, base=None):
    output = np.sum(np.where(p != 0, p * np.log(p / q), 0))
    if base is not None:
        output /= np.log(base)
    return output

