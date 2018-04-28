# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:36:46 2016

@author: WELG
"""

data = []

file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail

gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])            # This will raise a value error if the student does not have a grade
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[:], []])  # The student does not have a grade, create an empty list for this student

for i in data:
    print(i)

print("----------")

for i in gradesData:
    print(i)