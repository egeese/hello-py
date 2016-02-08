#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# ln -sprint 'Argument List:', str(sys.argv)
text = []
para = []
paras = []
choice = 0
if len(sys.argv) < 5:
    if len(sys.argv) > 0:
        choice = int(sys.argv[1])
    else:
        choice = 0
else:
    choice = -1

if choice == 0:
    text.append("Hello World")
    text.append("Says Python")
elif choice == -1:
    text.append(sys.argv[1] + " " + sys.argv[2])
    text.append(sys.argv[3] + " " + sys.argv[4])
elif choice == 1:
    text.append("Fitze Fatze")
    text.append("Matze Witze")
elif choice == 2:
    text.append("Zicke Zacke")
    text.append("Hühner Kacke")
else:
    text.append("Fitze Fatze")
    text.append("Matze Witze")
    text.append("Hatse Ritze")
	
for item in text:
    for splitItem in item.split():
        sys.stdout.write(str(splitItem) + " ")
        n = len(item.split())
        for i in range(0, n + 1):
            if len(paras) < n + 1: paras.append([])
            paras[i].insert(i, splitItem)
print ""
for para in paras:
    for item in para:
        sys.stdout.write(str(item) + " ")
    print ""
print ""
paras.reverse()
for para in paras:
    para.reverse()
    for item in para:
        sys.stdout.write(str(item) + " ")
    print ""
