#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[33]:


import sys
from solid import *
from solid.utils import * 

a = cube([80,60,25])

b = translate((60,50,5))(
    cube([10,15,10]))
c = translate((40,30,20))(
    cylinder(h=60,r=20))
d = translate((0,0,5))(
    cube([20,60,30]))
fotic = a+b+c+d
print(scad_render(fotic))


# In[ ]:





# In[ ]:




