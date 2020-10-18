# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mmBQXuTa3TqPVyMcVuJXzlUl1wYIcP5z
"""

import numpy as np
import re
from numpy import asarray



import tensorflow_hub as hub


embed = hub.load('https://tfhub.dev/google/universal-sentence-encoder/4')
def get_features(x):
    embeddings = embed(x)
    return asarray(embeddings)



def cosines(v1, v2):
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    if (not mag1) or (not mag2):
        return 0
    return np.dot(v1, v2) / (mag1 * mag2)


def test_similarity(text1, text2):
    vec1 = get_features(text1)[0]
    vec2 = get_features(text2)[0]
    return cosines(vec1, vec2)

import pandas as pd
data =pd.read_csv("train.csv" ,usecols=["description_x" ,"description_y"])
k= []

for x in range(len(data["description_x"])):
  k.append(test_similarity([data["description_x"][x]],[data["description_y"][x]]))


import pandas as pd
from numpy import asarray
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import tensorflow as tf

def get_keras_model():
    """Define the model."""
    model = Sequential()
    model.add(Dense(128, input_shape=[x_train.shape[1]], activation='relu'))
    model.add(Dropout(0.1))

    model.add(Dense(2, activation='sigmoid'))

    model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
    model.summary()
    return model

categories=pd.read_csv("train.csv" ,usecols=["same_security"])
k=pd.DataFrame(k,columns=["k"])

x_train, x_test, y_train ,y_test =train_test_split(k, categories, shuffle=True)

y_train = asarray(y_train, dtype="float32")
y_test = asarray(y_test, dtype="float32")
model = get_keras_model()

model.fit(x_train, y_train, epochs=50, validation_split=0.2)

!pip install textract

import textract
def __text_process(text_dir):
        ext = str(text_dir).split(".")[-1]

        if ext=='txt':
            with open(text_dir,mode='r') as f:
                text = f.read()
        elif ext=='docx':
            text = textract.process(text_dir).decode('utf-8')
        elif ext=='pdf':
            text = textract.process(text_dir).decode('ascii')
        elif ext=='png':
            text =pytesseract.image_to_string(Image.open(text_dir))
        else:
            raise Exception("Unsupported filetype")
        return text

a=input('file/text 1: ')
b=input('file/text 2: ')
import os
if os.path.isfile(a):
    a=__text_process(a)
if os.path.isfile(b):
    b=__text_process(b)
sim=test_similarity([a], [b])
a = model.predict([float(sim)])
if a[0][1] > 0.46:
        output='same'
else:
        output='diff'


print(output)

!pip install google

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = input('document you wrote about')
l=[]
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 
    l.append(j)

s=input('select the website: (enter 1-10)')
s=int(s)-1
l[s]

import requests

page = requests.get(l[s])
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

p = soup.find_all('p')
paragraphs = []
for x in p:
    paragraphs.append(str(x))
j=''
for i in paragraphs:
  j+=(i[3:-4])

a=input('input file path or text')

import os
if os.path.isfile(a):
    a=__text_process(a)


sim=test_similarity([a], [j])
a = model.predict([float(sim)])
if a[0][1] > 0.46:
          output=a[0][1]
else:
          output='different'
print(output)

from zipfile import ZipFile
file_name="/content/archive.zip"
with ZipFile(file_name,'r') as zip:
  zip.extractall()
  print('done')

!pip install pytesseract

!pip install Image

!pip install tesseract

!sudo apt install tesseract-ocr

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image

extractedInformation = pytesseract.image_to_string(Image.open('img1.png'))
print(extractedInformation)

extractedInformation2 = pytesseract.image_to_string(Image.open('img2.png'))
print(extractedInformation2)

sim=test_similarity([extractedInformation2], [extractedInformation2])
a = model.predict([float(sim)])
if a[0][1] > 0.46:
        output='same'
else:
        output='diff'


print(output)