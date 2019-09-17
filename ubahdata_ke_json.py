#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import json


# In[34]:


data1 = pd.read_csv("film_manakah_yang_anda_suka.csv")
data1 = data1.drop(['Timestamp'], axis=1)
data1 = data1.fillna(0)


# In[35]:


data2 = {}
daftar_film = ['Ada Apa dengan Cinta 2', 'Gundala', 'Dilan 1991',
       'Bumi Manusia ', 'Dua Garis Biru', 'Avengers: End Game',
       'The Lion King', 'Aladdin', 'Spiderman: Far From Home',
       'Captain Marvel']
for nama in data1['Nama Anda'].values:
    dummy = {}
    for film in daftar_film:
        dummy[film] = data1[data1['Nama Anda']==nama][film].values[0]
    data2[nama] = dummy


# In[36]:

with open('output_data_film.JSON', 'w') as file:
     file.write(json.dumps(data2)) # use `json.loads` to do the reverse

