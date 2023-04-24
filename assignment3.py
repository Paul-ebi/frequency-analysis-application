#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import string

def analyze(cipher_text):
    count = {}
    for c in cipher_text:
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count


# In[2]:


def replace(cipher_text, rule):
    plain_text = ""
    for c in cipher_text:
        if c in rule:
            plain_text += rule[c]
        else:
            plain_text += c
    return plain_text


# In[3]:


def print_analysis(count):
    print("Analysis:")
    for c in sorted(count.keys()):
        if c in string.ascii_letters:
            print("{}->{}".format(c, count[c]))


# In[4]:


def main():
    if len(sys.argv) != 2:
        print("Usage: python analysis.py cipher.txt")
        return
    
with open("cipher.txt", "r") as f:
    cipher_text = f.read().strip()
    
    count = analyze(cipher_text)
    print("Cipher Text:\n\n{}".format(cipher_text))
    print_analysis(count)


# In[5]:


while True:
       print("\nOptions:\n1) Take replace rule\n2) Exit\n")
       option = input("Option> ")
       if option == "1":
           rule = {}
           rule_input = input("Enter replacement rule-> ")
           pairs = rule_input.strip().split(",")
           for pair in pairs:
               cipher_char, plain_char = pair.split(":")
               rule[cipher_char.strip()] = plain_char.strip()
           plain_text = replace(cipher_text, rule)
           print("\nPlain Text:\n\n{}".format(plain_text))
       elif option == "2":
           break
       else:
           print("Invalid option")

if __name__ == "__main__":
   main()


# In[ ]:




