#!/usr/bin/env python
# coding: utf-8

'''
Authors: Divine Okanume & Cameron Ogiugo

This program is used to create two probability plots, and then take a user input and return the most probable language.
After runnning the program you will be prompted for an input, and after running the program will return the most probable language.



'''

# In[1]:


import numpy as np      # import numpy as np for later use
import matplotlib.pyplot as plt # import matplotlib for plotting probability distributions
import matplotlib.colors as colors
import unidecode # import unidecode to normalize input by converting accented characters


# In[2]:

english_list = []   
new_english_list = []
english_map = {}

spanish_list = []   
new_spanish_list = []
spanish_map = {}

def create_dict(l, m , n, o): #l=text file #m=englishlist n= newenglishlist o=englishmap
 
    with open(l, 'r',) as f:  # Open text file and convert to text
        for line in f:
            m.append(line[17:len(line)-1])     # This loop iterates through each line, storing it in a new list, whilst only selecting the numbers 
                                                         
    for x in m:     # This loop converts the list to a new numpy array which will make it easier to create a dictionary, allowing us to have a float array.
        n.append(x)  
    n = np.array(n, dtype=float) # Converts list of probability to numpy arrays and converts them from string to float values          


    i = 97
    while i < 123:    #Iterates through unicode (alphabet a-z) and adds each letter to dictionary along with respective position in array, with a being 0
        o[(f"{chr(i)}")] = n[i-97]
        i = i + 1

create_dict('G109Phase1_English.txt', english_list, new_english_list, english_map)  # Creates english dictionary as english_map
create_dict('G109Phase1_Spanish.txt', spanish_list, new_spanish_list, spanish_map)  # Creates spanish dictionary as spanish_map


# In[3]:


names = list(spanish_map.keys())  
values = list(spanish_map.values())
fig2 = plt.figure(figsize=(8,6))  # Creates figure for us to plot distribution
plt.ylabel('Probability', fontsize=14)  # Labels the y-axis
plt.xlabel('Letter', fontsize=14)       # Labels the x-axis
plt.title('Probability Distribution for Spanish', weight='bold')
plt.bar(range(len(english_map)), values, tick_label=names, facecolor = 'teal', edgecolor='orange', width = 1, linewidth=1.5 )  # Plots a bar chart
plt.show()
fig2.savefig('probabilitydistspanish.svg', bbox_inches='tight') # Save image as an svg file


# In[4]:


names = list(english_map.keys())
values = list(english_map.values())
fig1 = plt.figure(figsize=(8,6))   # Creates figure for us to plot distribution
plt.ylabel('Probability', fontsize=14)  # Labels the y-axis
plt.xlabel('Letter', fontsize=14)       # Labels the x-axis
plt.title('Probability Distribution for English', weight='bold')
plt.bar(range(len(english_map)), values, tick_label=names, facecolor = 'lightcoral', edgecolor='navy', width = 1, linewidth=1.5 )   # Plots a bar chart
plt.ylim(0, 0.14)
plt.show()

fig1.savefig('probabilitydistenglish.svg', bbox_inches='tight')  # Save image as an svg file


# In[6]:


x = input()  

x = ''.join(e for e in x if e.isalnum())  
x = (''.join([i for i in x if not i.isdigit()])).lower()# Ensures string is free of numbers, special charcters and spaces
x = unidecode.unidecode(x)
    

p_english = 1
p_spanish = 1

for i in x: # For each character in map, multiply probability and add to result
    p_english *= english_map[i]

for j in x: 
    p_spanish *= spanish_map[j]
    
    
if p_english > p_spanish: # If probability of english is higher than spanish, print english, else print spanish
    print('English')

else:
    print('Spanish')

