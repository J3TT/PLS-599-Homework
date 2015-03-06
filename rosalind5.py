#!bin/user/python
#Generate counter variable
counter = 0

#Opens Rosalind file and creates new output file
with open('rosalind_ini5.txt', 'r') as inpt:
	with open('rosalind_ini5_answers.txt', 'w') as otpt:
	
# Loop for printing
		for line in inpt:
			counter += 1
			if counter % 2 == 0:
				otpt.write(line)