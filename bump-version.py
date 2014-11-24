#!/usr/bin/python
my-input = raw_input("Enter git annotated tag version: ")
def GetVersion(my-input):
for i in my-input:
        if i == - :
           new-version = my-input.replace("v", "")
           version = new-version.split("-")[0] + "-SNAPSHOT"
           #bump-version = version[5+1] + "-SNAPSHOT"
           print version
        else:
           version = input.replace("v", "")
           print version
