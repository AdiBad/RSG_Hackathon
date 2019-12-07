# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:58:30 2019

@author: Aditya
"""
import pandas as pd
from statistics import median
members = pd.DataFrame.from_csv(r"C:\Users\Aditya\Downloads\bacteria\2_members.tsv\2_members.tsv", sep = '\t');

#Store genefamily as key and frequency in that cluster as value
genefamily_dict = {}

#Actual list of gene ids  can be read from a text file
gene_ids = "2Z7I0,2Z7ID,2Z7J0,2Z7JT,2Z7MS,2Z7N8";

for i in range(1,len(members)):

    #these gene_ids belong to gene families with known functional feature (not S) so dataset size reduces for the best
    if(str(members.iloc[i,0]) in str(gene_ids)):
        print(i)
        split_bycom = str(members.iloc[i,3]).split(',');
        for fam in range(len(split_bycom)):
            split_bydot = split_bycom[fam].split('.');
            for fam_gene in range(0,len(split_bydot),2):
                #print(split_bydot[fam_gene])
                try:
                    genefamily_dict[split_bydot[fam_gene]] += 1;
                except KeyError:
                    genefamily_dict[split_bydot[fam_gene]] = 1;
        
        med_this = median(genefamily_dict.values());
        v =  variance(genefamily_dict.values());
        
        f = open("medvar_genefam.txt", "a")  
        f.write(str(members.iloc[i,0])+","+str(med_this)+","+str(v)+"\n");
        f.close();  
        
        f = open("store_genefam.txt", "a")  
        storethis_cluster = {members.iloc[i,0]: genefamily_dict}  
        f.write(str(storethis_cluster)+"\n");
        f.close();
        
        genefamily_dict.clear();
 
