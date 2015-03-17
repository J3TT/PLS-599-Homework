#!/usr/bin/python
# Import RegEx module
import re
# Record job title as jobid
jobid = input("Enter job title: ")
# Identify sequence file to be used in analysis
sequence = input("Enter sequence file name: ")
# Opens file
with open(sequence, "r") as inpt:
    #with open(jobid + " AGO Hook results.txt", "w") as otpt:
        for line in inpt:
            line_count = 0
            if line.startswith(">"):
                line_count += 1
            elif line_count % 2 == 0:
                print(line)
                Protein_sequence = line
        AGO_Hook = re.compile('(GWG|WG|GW)', re.IGNORECASE)
        for ago_hook in AGO_Hook.finditer(Protein_sequence):
            print(ago_hook.span(), ago_hook.group())
            #Add code to write AGO Hooks to output file