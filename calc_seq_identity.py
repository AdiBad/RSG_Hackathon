#Original edit by Nil Fernandez Lojo

#Calculate mean of most frequent residues at each position of multiple alignment file for given protein
import gzip
import numpy as np
from collections import Counter


def calculate_seq_identity (file_name):
	file_name = "2/"+file_name
	
	try:
		f=gzip.open(file_name)
	except:
		return(-1)

	f1= f.readlines()
	f.close()
	length_alignment = len(f1[1])-1

	charar = np.chararray((int(len(f1)/2.0), length_alignment))
	list_alignments = []
	j = 0
	for i in range(1, len(f1), 2):
		alignment = f1[i].decode("utf-8")
		alignment = alignment[0:len(alignment)-1]
		alignment_2 = list(alignment)
		charar[j,] =  alignment_2
		j+=1
	number_sequences = j

	list_most_common = []
	list_percentage = []
	for i in range(length_alignment):
		letter_counts = Counter(charar[:,i])
		list_most_common.append(letter_counts.most_common(1)[0][0])	
		count_most_common = letter_counts.most_common(1)[0][1]
		list_percentage.append(count_most_common/number_sequences)

	list_percentage_not_gap = []

	for i in range(len(list_percentage)):
		if (list_most_common[i] != b'-'):
			list_percentage_not_gap.append(list_percentage[i])
	return(np.mean(list_percentage_not_gap))
