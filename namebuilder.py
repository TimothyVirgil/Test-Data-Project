'''This takes a .txt file of names,
splits them into lists of first and last names.
Then it generates random student id #'s for them.
Then I compile all this into a .csv file
I generated a random list using a site I forgot.
The scripting may need to change a bit depending on
the formatting of names.'''

import os
import random
import csv

##Create lists of names and Ids

os.chdir('Current Path') #insert Current Path here

full_names = []
first_names = []
last_names = []

with open('filename','r') as file: #extract names from file
    lines = file.readlines()

    for x in lines:
        full_names += [x[:-4]]

for x in full_names: #create lists of first and last names
	first_name = ''
	last_name = ''
	name_list = 'first'
	for a in x:
		if a == ' ':
			first_names += [first_name]
			name_list = 'last'
			continue
		elif name_list == 'first':			
			first_name += a
		elif name_list == 'last':
			last_name += a
	else:
		last_names += [last_name]

stud_id = random.sample(list(range(100000,999999)), len(first_names)) #generate 6 digit student ids

##Import into CSV file

headers = ['Student_Id', 'Last_Name', 'First_Name']
csv_rows = []

for a in range(len(first_names)): #generate rows for csv
	csv_rows += [[stud_id[a], last_names[a], first_names[a]]]

with open('students.csv', 'w', newline='') as csvfile: #create my csv and write headers, names, ids
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(headers)
	csvwriter.writerows(csv_rows)