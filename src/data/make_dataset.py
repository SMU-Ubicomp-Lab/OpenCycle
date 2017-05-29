# -*- coding: utf-8 -*-
# In[1]:

from os import path

import numpy as np
import pandas as pd


# In[2]:

try:
    file = path.join("data", "raw", "london.csv")
except OSError:
    print("This repository does not host the data. "
          "Put the csv in ../data/raw/")
    raise
df = pd.read_csv(file, na_values=0)


# Rename Italian columns to English.

# In[3]:

df.rename(columns={'DONNA': 'ID',
                   'P_SPEZZ': 'SEGMENT_ID',
                   'P_CICLO': 'CYCLE_ID',
                   'ANNO_NAS': 'BIRTH_YR',
                   'DATA': 'BEGIN_DATE',
                   'T_SPEZZ': 'N_SEGMENTS',
                   'T_CICLI': 'N_CYCLES',
                   'QUALIFI': 'DESC',
                   'TIPOTEMP': 'TEMP_SCALE',
                   'L_CICLO': 'L_CYCLE',
                   'L_PREOV': 'L_PREOVULATION',
                   'L_PERIOD': 'L_PERIOD',
                   'FIGLI': 'CHILDREN'
                   },
          inplace=True)


# We delete the cycles (rows) where the `L_PREOV` is missing (NA), because this data is unusable - we don't have the variable we seek to predict. **Ex:** If row 100 is deleted, the index would be $..., 98, 99, 101, 102, ...$
#
# After these rows are dropped, there are holes created in the index of the data frame. We would like the index numbers to be consecutive, so we use the `reset_index` function.

# In[4]:

df.dropna(subset=['L_PREOVULATION'], inplace=True)


# Delete those where DESC != 1 because those are flawed entries.

# In[5]:

df = df[df.DESC == 1]
df.drop('DESC', 1, inplace=True)


# # Process Temperature Readings
# 
# Decode temperatures to obtain *real* BBT values. Then, convert all celsius values to fahrenheit. The coding is described in [this file](../references/BBTProcessing.txt).

# In[6]:

FAHR = 1
CELS = 2
for i in range (1,100):
    df.loc[df.TEMP_SCALE == FAHR, 'TEMP' + str(i)] =  90 + df.loc[df.TEMP_SCALE == FAHR, 'TEMP' + str(i)]/10
    df.loc[df.TEMP_SCALE == CELS, 'TEMP' + str(i)] =  30 + df.loc[df.TEMP_SCALE == CELS , 'TEMP' + str(i)]/10
    #Convert celsius temps to fahrenheit
    df.loc[df.TEMP_SCALE == CELS, 'TEMP' + str(i)] =  32 + ((9/5) *  df.loc[df.TEMP_SCALE == CELS , 'TEMP' + str(i)])

#Display medians one at a time    
#df[df.TEMP_SCALE==FAHR].median()
#df[df.TEMP_SCALE==CELS].median()


# Create an age measurement for each cycle, computed from the birth year and measurement date.

# In[7]:

#NEED TO FIX SO THAT WE HAVE ONE AGE PER ID NOT CYCLE
df['AGE'] = (df.BEGIN_DATE.apply(lambda s: int(s.split('/')[-1]) % 100 if isinstance(s, str) else s) - df.BIRTH_YR)


# In[8]:

destination = ["data", "interim"]
df.to_csv(path.join(*destination, "df.csv"))
