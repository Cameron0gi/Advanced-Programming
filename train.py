'''
Authors: Cameron Ogiugo & Divine Okanume

The input should go:
python train.py (spanishtextfilename) (englishtextfile)

This program takes two command line arguments and write their respective probability distributions to two text files
(G109Phase1_English and G109Phase1_Spanish).

We are making use of the unidecode module in order to convert accented characters, in order to run this module 
should be installed, by running (pip install unidecode) in the shell.


'''
import unidecode
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

def load_text(x):  # Creates function to load text 


    with open(x, encoding="utf-8") as file:  # Loads in text file and temporarily stores it in variable, removing newlines
        data = file.read().replace('\n', '')
    return(data)


# In[5]:


spanish_text = load_text(str(arg1)) 
spanish_text = ''.join(e for e in spanish_text if e.isalnum())
spanish_text = (''.join([i for i in spanish_text if not i.isdigit()])).lower()  # Removes all numbers from text
spanish_text = unidecode.unidecode(spanish_text)


# In[21]:


english_text = load_text(str(arg2))
english_text = ''.join(e for e in english_text if e.isalnum())
english_text = (''.join([i for i in english_text if not i.isdigit()])).lower()
english_text = unidecode.unidecode(english_text)


# In[22]:


def write_dist(x, y):  # Creates function to write the distributions to their respective text files
    totalletters = float(len(x))  # counts total number of letters in word
    f = open(y, "a")  #opens file in order to append

    i = 96  
    while i < 122:  #Counts in unicode in order to iterate from a to z
        i = i + 1
        z = x.count(chr(i))
        a = (z + 1)/ totalletters #Divides count of letter by total number of letters
        language = y[11:18]
        f.write(f"P({chr(i)} | {language}) = {a}\n") #writes the probability of the letter on file for each letter
    f.close()
    
write_dist(spanish_text, "G109Phase1_Spanish.txt")   # Writes Spanish Distribution
write_dist(english_text, "G109Phase1_English.txt")   # Writes English Distribution

