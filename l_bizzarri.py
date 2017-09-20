#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:55:27 2017

@author: Laura
"""

#opens file and stores in the variable lb
lb = open("/Users/useruser/Downloads/PitaIlluminaGeneSet.fasta", "r")
#stores lines from lb into list called lines
lines=lb.readlines()

#Calculating number of genes
NumGenes=0
SeqNames=[]
for l in lines:
    #print l
    if l[0]==">":
        print l[1:-1]
        SeqNames.append(l[1:-1])
        NumGenes=NumGenes+1
print "This is the number of genes:"        
print NumGenes

#printing every other line from 'list' gives me the list of sequence names, just don't know how to put it in a list of its own
#print lines[0::2]

#Tried to create a list with items from another list, it didn't work
#SeqNames = [lines[0], lines[], lines[979]]
#print SeqNames 
# 

Sequences=[]
SeqLength=[]
for s in lines:
    if s[0]!=">":
        temp=s[:-1]
        Sequences.append(temp)
        #print temp
        SeqLength.append(len(temp))

max_value=0
min_value=1000000 
average_value=0
sums=0      
for b in SeqLength:
    if b > max_value:
        max_value=b
    if b < min_value:
        min_value=b
    sums=sums+b
average_value=sums/len(SeqLength)
print "This is the average sequence length:"
print average_value    
    
    
max_index=SeqLength.index(max_value)
min_index=SeqLength.index(min_value)
max_seq=SeqNames[max_index]
min_seq=SeqNames[min_index]
print "This is the maximum value:"
print max_value
print "This is the minimum value:"
print min_value
print "This is the maximum sequence name:"
print max_seq
print "This is the minimum sequence name:"
print min_seq        

#a is a list of indices
#m is (before running) any number number in list a
#because list a is the list of indeces of the SeqLength list
#m will be an index from SeqLength
#this was done to make sure that if there are two sequences w/ the same length, they're both included 
a=range(len(SeqLength))
short_seq=0
with open("/Users/useruser/Downloads/problem_4.fasta", "w") as variable:        
    for m in a:
        if SeqLength[m] < 500:
          variable.write(SeqNames[m]+"\n")
          variable.write(Sequences[m]+"\n")
          short_seq=short_seq+1
print "This is the number of sequences with less than 500 base pairs:"
print short_seq