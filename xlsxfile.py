import pyexcel as p
from openpyxl import Workbook
import xlrd
import csv
ary = []

#for csv file reading and inserting it into ary array
#with open("0446030001504358163_0.csv", "r") as fb:
#	reader = csv.reader(fb)
#	for i in reader:
#		#print(" ".join(i))
#		print ("||||||||||")
#		print (i)
#		print (i[1])
#		if i[1] != '':
#			ary.append(i[1])




reader = xlrd.open_workbook("New List (Updated).xlsx")
worksheet = reader.sheet_by_index(0)
# print (reader.sheet_names())
# for i in worksheet.col(1):
# 	print (i.value)
#	if i.value != '':
#		ary.append(i.value)
#print (ary)

main_ary = []
for i in worksheet.col(0):
	# print (i.value)
# 	ary = []
# 	m = i.value.split(',')
# 	arb = []
# 	for i in m:
# 		i = i.strip()
# 		# print(i)

		
# 		arb.append(i)

# 	# print(m)
# 	# b = m.strip()
# 	# print(b)
# 	main_ary.append(arb)
# # print(arb)
# # 	ary.push(m)
# # 	main_ary.push(ary)

# print(main_ary)
	print (type(i.value))
	print ("{{{{{{{{{{{{")
	print (isinstance(i.value, str))
	if isinstance(i.value, str):
		print (i.value)
		i.value = []
		for j in worksheet.col(1):
			i.value.append(j)

		print (i.value)