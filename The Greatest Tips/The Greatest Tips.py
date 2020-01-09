#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This program helps the user to decide how much he should tip.
The principle is simple: the quality of service has a margin cost
and percent of the amount not necessarily increase with increasing amount.
But if you want, you can leave an extra tip.
"""
bill = int(input("Please enter the amount of your bill: ")) #We take the user's amount of bill
tip_for_big = 0.15 #defining tip for the big amount
tip_for_mid = 0.18 #defining tip for the middle amount
tip_for_bit = 0.20 #defining tip for the small amount

if bill < 50: #defining conditions for the small amount
    tip = bill*tip_for_bit #if amount is small, we multiplies the bill on recommended percent
elif (bill > 50) or (bill < 101): #defining conditions for the middle amount
    tip = bill*tip_for_mid #if amount is middle, we multiplies the bill on recommended percent
else: #if the amount is bigger than middle, we conduct it's as a big amount
    tip = bill*tip_for_big #if amount is big, we multiplies the bill on recommended percent
print(f"You should tip ${tip:.0f}") #showing the recommended tip for user

#We take the user's input for the computation of extra tip
extra_question = input("Do you want to leave the extra tip (+10%)? Answer YES or NO: ")

if extra_question == "yes" or "YES" or "Yes": #indentifying user's wish to extra tip
    extra_tip = tip + (bill*0.1) #compute extra tip if user wants this
    print(f"You will be the greatest if tip ${extra_tip:.0f}") #showing the recommended tip for user
else: #if user don't want to extra tip, we return the regular tip
    print(f"Ok. You should tip ${tip:.0f}") #showing the recommended tip for user