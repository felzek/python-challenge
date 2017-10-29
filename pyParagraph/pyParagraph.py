import csv
import os

filepath = os.path.join("raw_data","paragraph_1.txt")

with open(filepath,"r") as txtfile: 
    
    textfile = txtfile.read()

    word_count = len(textfile.split(" "))

    sentence_count_2 = len(textfile.split("."))

    charaters= len(textfile)

    word = len(textfile)

    spaces = textfile.count(' ')

print("Paragraph Analysis")

print("-------------------\n")

print("Approximate Word Count:" + str(word_count))

print("Approximate Sentence Count:" + str( sentence_count_2 ))

print((word-spaces)/word_count)

print((word_count/sentence_count_2))




    #x = txtfile.split(" ")

#print(x)