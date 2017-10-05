#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:41:18 2017

@author: Laura
"""

#opens file and stores in the variable lb
lb = open("/Users/useruser/Downloads/Pita_MakerAlignments.gff3", "r")
#stores lines from lb into list called lines
gfflines=lb.readlines()
#print gfflines
Genes=[]
#calculating number of genes
TotalNumGenes=0
for line in gfflines:
    if line[0]!="#":
        column=line.split("\t")
        #print column[0]
        if column[2]== "gene" :
            Genes.append(column[8])
            TotalNumGenes=TotalNumGenes+1
print "This is the number of genes:", TotalNumGenes  

#calculating the number of exons per gene and exon lengths
Exons=[int]*(TotalNumGenes)
ExonLength=[]
NumGenes=0
NumExons=0
#Short_MultiexonicGenes=0
for line in gfflines:
    if line[0]!="#":
        column=line.split("\t")
        #print column[0]
        if column[2]== "gene" :
           if NumGenes==0:
               NumGenes=NumGenes+1
               NumExons=0
           else:
                Exons[NumGenes-1]=NumExons
                NumGenes=NumGenes+1
                NumExons=0
        elif column[2]=="exon":
            NumExons=NumExons+1
            ExonLength.append(int(column[4]) - int(column[3]))
#            for n in ExonLength < 20:
#                    Short_MultiexonicGenes.append(Genes[n])
#        if column[2]=="CDS":
Exons[NumGenes-1]=NumExons
            #Exons.append(NumExons)
            #ExonLength.append(column[3] - column[4])
#print "This is the number of genes:", NumGenes       
print "These are the exons:", NumExons
#print "These are exon lengths", ExonLength

#calculating number of monoexonic and multiexonic genes
monoexonic=0
multiexonic=0
multiexonic_genes=[]
for g in Exons:
    if g==1:
        monoexonic=monoexonic+1
    elif g > 1:
        multiexonic=multiexonic+1
        multiexonic_genes.append(Genes[g])
print "This is the number of monoexonic genes", monoexonic
print "This is the number of multiexonic genes", multiexonic


#calculating minimum and maximum exon length 
#also calculating average exon length
max_value=0
min_value=1000000 
average_value=0
sums=0     
for b in ExonLength:
    if b > max_value:
        max_value=b
    if b < min_value:
        min_value=b
    sums=sums+b
average_value=sums/len(ExonLength)
print "This is the maximum exon length:", max_value
print "This is the minimum exon length:", min_value
print "This is the average exon length:", average_value 

#calculating median exon length
median_value=0  
median_value=((ExonLength[2653])+ (ExonLength[2654]))/2
print "This is the median exon length:", median_value

#finding genes that are less than 20 bp and putting them in a separate list
Short_MultiexonicGenes=[]
for n in ExonLength:
    if n < 20:
        Short_MultiexonicGenes.append(Genes[n])
        
#creating a file with the multiexonic gene names excluding multiexonic genes that are less than 20 bp
with open("/Users/useruser/Desktop/problem_5.gff3", "w") as variable:
    for x in gfflines:
        if column[8]!=Short_MultiexonicGenes:
            variable.write(x)
     