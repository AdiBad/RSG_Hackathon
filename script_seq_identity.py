#Original edit by Nil Fernandez Lojo

#Access the calulate function from calc_seq_identity.py and apply on all gene families in given cluster

from calc_seq_identity import calculate_seq_identity
import os
import time
import numpy as np
import re

list_families = []
class_list_families = []

output_file = "seq_identity.tsv"
step_write = 100

data_file = "data_repartition.tsv"
f=open(data_file, "r")
f1= f.readlines()
f.close() 
for line in f1:
	data_input = re.split("\t+", line)
	list_families.append(data_input[0])
	class_list_families.append(int(data_input[2]))

list_seq_identity = []
for i in range(len(list_families)):
	if(i%step_write == 0 and i != 0):
		print("Percentage calculation = ", i/len(list_families))
		f = open(output_file,"a")
		for j in range(i-step_write,i):
			f.write(list_families[j]+"\t"+str(list_seq_identity[j])+"\n")
		f.close()
	file_name = list_families[i]+".trimmed_alg.faa.gz"
	list_seq_identity.append(calculate_seq_identity(file_name))
