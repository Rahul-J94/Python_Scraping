import pyexcel as p
from openpyxl import Workbook
import xlrd
import csv
ary = []
pit = {}

#for csv file reading and inserting it into ary array
with open("City_wise_data (1).csv", "r") as fb:
	reader = csv.reader(fb)
	for i in reader:
		#print(" ".join(i))
		# print ("||||||||||")
		# print (i)
		if i[1] not in ary:
			ary.append(i[1])
		# print (i[1])
		# if i[1] != '':
		# 	ary.append(i[1])
	# print(ary)
	ary.pop(0)
	print (ary)

	for i in ary:
		pit[i] = []

print(pit)
# for i in pit:
# 	for x in pit[i]