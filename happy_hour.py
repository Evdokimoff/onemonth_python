import pandas as pd
import random

file = "https___www.amazon.com_gp_most.xlsx"
xl = pd.ExcelFile(file)
df = xl.parse(Sheet1)
df = list(df)
print(df[0:10]

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samule L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_persons = random.sample(people,k=2)

print(f"How about you go to {random_bar} with {random_persons}")
