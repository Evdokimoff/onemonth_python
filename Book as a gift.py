"""
This script takes the name of your friend 
and suggest you gift him the book 
from the top of most wished books
"""

import pandas as pd
import random

"""
The most wished books was parsed from Amazon amazon.com/gp/most-wished-for/books. 
You can download it from my GitHub  
https://github.com/Evdokimoff/onemonth_python/blob/master/https___www.amazon.com_gp_most.xlsx 
and then put it in the directory where you trying run the script.
"""

file = "https___www.amazon.com_gp_most.xlsx"
df = pd.read_excel(file, sheet_name=0)
books = df['Book'].tolist()
friend_name=input("Please enter the name of your friend: ")
print(f"What book you can gift to {friend_name}?")
random_books = random.choice(books)
print(f"You can gift to {friend_name} the book {random_books}")   #We can also add to this result the link to buy
