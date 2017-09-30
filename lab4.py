import re

filevar = open("mbox-short.txt")

list_of_nums = []
for line in filevar.readlines():
	line = line.rstrip()
	temp_numbers = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(temp_numbers) != 1: continue 
	num = float(temp_numbers[0])
	list_of_nums.append(num)

print("Number of Values =", len(list_of_nums))
print("Max =", max(list_of_nums))
print("Min =", min(list_of_nums))
print("Average =", sum(list_of_nums)/len(list_of_nums))