def main():
	return "hello world"
strs = "000000000000000000000000"
#print(len(strs))
combinationSet = set([])
combinationSet.add("000000000000000000000000")#yes
combinationSet.add("111111000000000000000000")#yes
combinationSet.add("000000000000000001111110")#no 


def filterSolutions(comboSet, minOn, minOff):
	remainingSet = set([])
	for schedule in comboSet: 
		index = 0
		passed = True
		limit = 23 - minOn + minOff
		while passed and index < limit:
			if schedule[index] == "1":
				minHours = index + minOn
				while index <= minHours and index < limit:
					if schedule[index] == "1":
						index += 1
						print(index)
					else:
						passed = False
						
				while passed and schedule[index] == "1":
					index += 1
					print("here")
					print(index)
				minHours = index + minOff
				print(index)
				while passed and index <= minHours and index < limit:
					if schedule[index] == "0":
						index += 1
						print(index)
					else: 
						passed = False
						break
				
			else:
				index += 1
		if passed:
			remainingSet.add(schedule)
	return remainingSet


print(filterSolutions(combinationSet, 4, 2))






if __name__ == '__main__':
	main()