#!/usr/bin/env python
# coding: utf-8

# In[1]:


#นางสาว กวินนา พลเสน 362515241001 EE36241N
M=input("Username :")
N=input("Password :")
if M=="milk" and N=="0804":
    print("Welcome to Kawin Shop.")
else :
    print("Error ,please try again.")
C=20
P=50
T=30
G=40
B=60
print("-------------------Menu-------------------")
print("Welcome to Kawin Shop")
print("1. Chili 20 THB")
print("2. Potato 50 THB")
print("3. Tomoto 30 THB")
print("4. Garlic 40 THB")
print("5. Bean 60 THB")
Kawin=int(input("What do you want?(1-5) : "))
number=int(input("How many do you want? : "))
if Kawin==1:
    print("You order ",number," of Chili ",C*number, " THB")
elif Kawin==2:
    print("You order ",number," of Potato  ",P*number, " THB")
elif Kawin==3:
    print("You order ",number," of  Tomoto  ",T*number, " THB")
elif Kawin==4:
    print("You order ",number," of Garlic ",G*number, " THB")
elif Kawin==5:
    print("You order ",number," of Bean ",B*number, " THB")


# In[ ]:




