#!/usr/bin/python
####author = Lokesh Pathak <pathak.lokesh@hotmail.com>
####Python script which reads a file and prints the number of times a word is present in the file. 
####This program also consider words with case sensitivity to be different.

dict = { }

fileName = input("Please supply name of input file: ")
gotIt = False
try :
    f = open(fileName)
    gotIt = True
except IOError as e :
    print("Failed to open", fileName)

if gotIt :
    for line in f :
        words = line.lower.split()
        for word in words:
            if word in dict :
                dict[word] = dict[word]+1
            else :
                dict[word] = 1

    f.close()

    for i in dict.items() :
        word, oc = i
        print("The number of occurrences of", word, "was", oc)