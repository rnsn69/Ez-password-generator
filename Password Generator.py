import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number = "0123456789"
Symbol = "@#$!"

All = lower + upper + Number + Symbol
length = 15
password = "".join(random.sample(All,length))
print("Your password is: ", password)