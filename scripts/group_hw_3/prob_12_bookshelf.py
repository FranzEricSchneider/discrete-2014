#!/usr/bin/env python

#A shelf holds 12 different books lined up on the shelf. You want to pick a collection of 5 books, but you can't choose any adjacent books. How many choices do you have for this collection?  (The order in which you choose the books does not matter; it is only the books themselves that matter, and you are not lining up your chosen books.) Explain all reasoning and work.

import sys 
import os
import itertools

if __name__ == '__main__':
	sys.path.append(os.path.relpath("../"))
	from example_code import nCr

book_list = range(1, 13)
poss = itertools.combinations(book_list, 5)
poss_list = list(poss)

success_list = []
for combination in poss_list:
	# print "Testing combination" + str(combination)
	for i in range(len(combination) - 1):
		# print "Testing element %d" % i
		flag = False
		if i == 0:
			if combination[i] == combination[i+1] - 1:
				flag = True
				break
		else:
			if (combination[i] == combination[i+1] - 1 or 
					combination[i] == combination[i-1] + 1):
				flag = True
				break
	if not flag:
		# print "Appending"
		# print combination
		success_list.append(combination)

print len(success_list)
print success_list
