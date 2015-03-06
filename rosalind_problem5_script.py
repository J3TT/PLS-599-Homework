#!bin/user/python
# Opens ROSALIND file containing lines

#Generate counter variable
counter = 0

#Open file and create output file
with open('rosalind_ini5.txt', 'r') as inpt:
	with open('rosalind_ini5_answers.txt', 'w') as otpt:
	
# Loop for printing
		for line in inpt:
			counter += 1
			if counter % 2 == 0:
				otpt.write(line)