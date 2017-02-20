#!/usr/bin/python

import csv

print('\n')
af = raw_input('Which dat files would you like to convert: ')

with open(af, 'r') as input_file:
    afLines = input_file.readlines()
    newLines = []
    for line in afLines:
        newLine = line.strip('\t').split()
        newLines.append(newLine)

with open('newFile.csv', 'w') as output_file:
    file_writer = csv.writer(output_file)
    file_writer.writerows(newLines)
