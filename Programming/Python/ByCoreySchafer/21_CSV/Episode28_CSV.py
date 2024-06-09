#csv stands for comma seperated values
#File datalist has camma delimeter for seperation
import csv

with open('names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)

	#Shows the location where the reader is available
	print(csv_reader)

	#To show the list formation
	for line in csv_reader:
		print(line)

with open('names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)
	print(csv_reader)

	#To see only email addresses
	for line in csv_reader:
		print(line[2])

with open('names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)
	print(csv_reader)

	#Doesnt show the first line of the email address
	print("Doesnt show the first line of the email address")
	next(csv_reader)

	for line in csv_reader:
		print(line[2])

with open('names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)
	with open('new_names.csv','w') as new_file:

		#Turns comma into '-' delimiter
		csv_writer=csv.writer(new_file,delimiter= '-')

		for line in csv_reader:
			csv_writer.writerow(line)	

with open('names.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file)
	with open('new_namestab.csv','w') as new_file:

		#Turns comma into '\t' delimiter
		csv_writer=csv.writer(new_file,delimiter= '\t')

		for line in csv_reader:
			csv_writer.writerow(line)

#Print in the format of dictionary
with open('names.csv','r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	for line in csv_reader:
		print(line)

#To print the email
with open('names.csv','r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	for line in csv_reader:
		print(line['email'])

#Writing field names
with open('names.csv','r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	with open('new_namestab.csv','w') as new_file:
		field_names=['first_name','last_name','email']
		csv_writer=csv.DictWriter(new_file,fieldnames=field_names,delimiter= '\t')
		csv_writer.writeheader()
		for line in csv_reader:
			csv_writer.writerow(line)

#See the writing file to see result
with open('names.csv','r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	with open('new_namestab1.csv','w') as new_file:
		field_names=['first_name','last_name']
		csv_writer=csv.DictWriter(new_file,fieldnames=field_names,delimiter= '\t')
		csv_writer.writeheader()
		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)