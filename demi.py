#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:13:12 2017

@author: Laura
"""
#This script calculates GC content

#opens the file and stores in the variable fh
fh = open("/Users/useruser/Downloads/demo.fasta", "r")
#store lines from fh into list called lines
lines=fh.readlines()

NumGenes=0
for l in lines:
    #print l
    if l[0]==">":
        NumGenes=NumGenes+1
print NumGenes

countA=0
countG=0
countC=0
countT=0
nucleotides=0
for l in lines:
    if l[0]!=">":
        for nuc in l:
            if nuc=="A":
                countA=countA+1
                nucleotides=nucleotides+1
            elif nuc=="G":
                countG=countG+1
                nucleotides=nucleotides+1
            elif nuc=="C":
                countC=countC+1
                nucleotides=nucleotides+1
            elif nuc=="T":
                countT=countT+1
                nucleotides=nucleotides+1
            else:
                print "it's probably a new line character"                
print "A:", countA
print "G:", countG
print "C:", countC
print "T:", countT
print nucleotides
print countA+countG+countC+countT

GC=(countG+countC)/float(nucleotides)
print "GC content is: ", GC
