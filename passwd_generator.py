import random

print(" ____  __  ____ ____ _  _ ____     ___ ____ __ _ ____ ____  __ ____ __ ____ ")
print("(  _ \/ _\/ ___) ___) )( (    \   / __|  __|  ( (  __|  _ \/ _(_  _)  (  _ \\")
print(" ) __/    \___ \___ \ /\ /) D (  ( (_ \) _)/    /) _) )   /    \)((  O )   /")
print("(__) \_/\_(____(____(_/\_|____/   \___(____)_)__|____|__\_)_/\_(__)\__(__\_)")

uppr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = uppr.lower()
num = "0123456789"
sym = "!@#$%^&*()_+><?=-;:"

Length_of_Password = 18
No_of_Password = int(input("Enter number of passwd you want"))
op_strings = uppr + lower + num + sym

for x in range (No_of_Password):
    passwd = "".join(random.sample(op_strings, Length_of_Password))
    print(passwd)

