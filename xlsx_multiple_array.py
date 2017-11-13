import xlrd
ary = {}
testere = []
reader = xlrd.open_workbook("Infobox2.xlsx")
workbook = reader.sheet_by_index(0)
#workbook2 = reader.sheet_by_index(1)
#print (reader.sheet_by_index(0))

#for j in workbook2.col(0):
#	print (j.value)
#	tester.append[j.value]
for j in workbook.col(1):
	#print (j.value)
	testere.append(j.value)
print (testere)
for i in workbook.col(0):
	#print (i.value)
	if isinstance(i.value, str):
		ary[i.value] = []
		for f in testere[1: ]:
			print (f)
			if f != '':
				ary[i.value].append(f)
				testere.remove(f)
			else:
				testere.remove(f)
				pass		
			#while(f != ''):
			#	ary[i.value].append(f)
				#testere.remove(f)
			
			#	print (ary[i.value])


print (ary)
