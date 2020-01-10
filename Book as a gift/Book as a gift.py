#!/usr/bin/env python
# coding: utf-8


"""This script takes the name of your friend
and suggest you gift him the book
from the top of most wished books"""

import pandas as pd
import random

"""The most wished books were parsed from Amazon amazon.com/gp/most-wished-for/books.
You can download it from my GitHub
https://github.com/Evdokimoff/onemonth_python/blob/master/amazon_most_wished_books100_122019.xlsx
and then put it in the directory where you trying run the script."""

file = "amazon_most_wished_books100_122019.xlsx"
df = pd.read_excel(file, sheet_name=0)
books = df['Book'].tolist()
random_books = random.choice(books)
friend_name = input("Please enter the name of your friend: ")
print(f"What book you can gift to {friend_name}?")
print(f"You can gift to {friend_name} the book {random_books}")
# We can also add to this result the link to buy
