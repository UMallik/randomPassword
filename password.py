import random
import string

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase
punctuations = string.punctuation
password_combo = lower_case_letters + upper_case_letters + punctuations
f = open('passwords.txt','w')
for _ in (range(int(input("How many random passwords do you want to generate? ")))):
    for j in random.sample(password_combo,16):
        f.write("".join(j))
    f.write("\n")

f.close()