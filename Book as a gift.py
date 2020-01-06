#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import random
#The most wished books was parsed from Amazon https://www.amazon.com/gp/most-wished-for/books
file = "https___www.amazon.com_gp_most.xlsx"
df = pd.read_excel(file, sheet_name=0)
books = df['Book'].tolist()
friend_name=input("Please enter the name of your friend: ")
print("What book you can gift to {}?".format(friend_name))
random_books = random.choice(books)
print(f"You can gift to {friend_name} the book {random_books}")

