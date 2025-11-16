import time
import os

#Write a program to print Twinkle Twinkle Little Star poem
print("Twinkle, twinkle, little star,")
time.sleep(0.5)
print("How I wonder what you are!")
time.sleep(0.5)
print("Up above the world so high,")
time.sleep(0.5)
print("Like a diamond in the sky.")
time.sleep(0.5)
print("Twinkle, twinkle, little star,")
time.sleep(0.5)
print("How I wonder what you are")
time.sleep(1)

#Print the table of 5
for i in range (1,11):
	print("5 * ",i ,"= ",5*i)
    
#Write a program to print the contents of a directory using os module
directory = '/home/sunless/Codes/PyLearn_v2'
print("Contents of the directory:", directory)
for item in os.listdir(directory):
    print(item)