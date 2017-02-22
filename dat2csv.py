#Created by Kevin Figueroa & Dickson Kwong 
#MLresearchLab.com
#Python 2.7 run inside of Jupyter Notebook
#[Purpose]
#Convert downloaded Threat Intel .dat file(s) into a .csv file

#MTI LICENSE

#Copyright (c) 2017 Kevin Figueroa & Dickson Kwong

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#!/usr/bin/python

#python CSV library
import csv

#print new line character for easier readability
print('\n')

#ask users which .dat file would be converted
af = raw_input('Which dat files would you like to convert: ')

#open user's requested file
with open(af, 'r') as input_file:

    #read each line into the variable
    afLines = input_file.readlines()

    #empty list
    newLines = []

    #for loop to read each line within afLines
    for line in afLines:

        #Strip tab and append in variable
        newLine = line.strip('\t').split()
        newLines.append(newLine)

#open new file called newFile.csv, which will be written to
with open('newFile.csv', 'w') as output_file:

    #variable contain the csv write function 
    file_writer = csv.writer(output_file)

    #write information with variable "newLines"
    file_writer.writerows(newLines)

#END
