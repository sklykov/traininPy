# -*- coding: utf-8 -*-
"""
Demo - handling DNA information from a sample (NCBI)
@author: ssklykov (credits also to the associated edX course)
"""
# %% Demo reading the file txt and storing the info at once
with open("dna_sample.txt",'r') as dna:
    readed_lines = []
    for line in dna:
        readed_lines.append(line)

# %% Handling the read data
one_line = "" # empty string for concatenation
for i in range(len(readed_lines)):
    one_line += readed_lines[i] # maybe not so memory efficient, but the quick way to concatenate strings

# %% Removing all redundant symbols / characters
print("collected nucleotids + extra symbols are equal to",len(one_line))
one_line = one_line.replace("\n","")
one_line = one_line.replace("\r","")
print("after removing of extra ones",len(one_line))
one_line = one_line[20:938] # actual encoding sequence

# %% Importing of a table for associations
from tableCod import codons

# %% Association nucleotids - codons
def associate(codons:dict,seq:str)->str:
    result = ""
    if len(seq) % 3 == 0:
        for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            result += codons[codon]
    return result

# %% Testing
cod1 = associate(codons,"ATTGAAACA")
cod2 = associate(codons,"GCC")
cod3 = associate(codons,one_line)