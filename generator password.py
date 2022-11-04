import string
import random
a = input("YOUR NAME: ").lower()

print("")
b= input("YOUR SURNAME: ").lower()
print("")
########### making pasword

def useing_key():
  char = ((string.ascii_letters)+(string.ascii_uppercase)+(string.digits)+(string.hexdigits)+(string.punctuation))
  key_words=(list(char))
  return key_words
global key
key = (useing_key())

def between():
    bet_3 = (string.digits)
    ps_bt = ""
    for i in range(7):
        bet = random.choice(bet_3)
        ps_bt = str(ps_bt) + str(bet)
    return ps_bt
global pl2
pl2 = (between())


def PASSWORD():
    pasword = ""
    for i in range(16):
        pasword_gen = random.choice(key)
        pasword = (pasword)+(pasword_gen)
    return pasword

global pasword_1
pasword_1=(PASSWORD())
########## for making in between

class EMAIL_why:

    def __init__(self,name,last):
        self.name = name
        self.last = last
        self.email = name+last+str(pl2)+("@gmail.com")
        self.pasw = str(pasword_1)
    

email_c = EMAIL_why(a,b)
print("--"*50)
print("Email ID = ",email_c.email)
print("")
print("PASSWORD:",email_c.pasw)
print("--"*50)
print ("")