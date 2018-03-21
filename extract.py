#!/usr/bin/python
###############################################################################
#Given a data file, the starting and ending position, and the periodicity 'p',# 
#the python code extracts data every 'p' lines between the initial and        #
#final positions, and writes to a new file.                                   #
#If ending position is given as 0, program will go till end of file           #
###############################################################################



import numpy as np
import sys
import math as m

l = len(sys.argv)

if l<7:
    print("\n Correct syntax is [extract.py][Name of output file] [no.of lines per entry] [start_line] [end_line] [periodicity] [Input file] \n")
    exit(0)

else :
    nlines = 0;

name_op = sys.argv[1];
opfile = open(name_op,"w")
nfac=int(sys.argv[2]);
ipos=int(sys.argv[3]);
fpos=int(sys.argv[4]);
p=int(sys.argv[5]);

num_lines = sum(1 for line in open(sys.argv[6]));

print "No. of entries in input file = ",(num_lines/nfac)
#print "Good till here.."
if fpos == 0:
    fpos=num_lines;

#print fpos;

#sys.exit(0);

flag=0;
inpfile=open(sys.argv[6],"r")
n_entries=0;
nsamp=0; #number of lines in output file
for i in inpfile:
    nlines+=1    
    if nlines%nfac == 0:
        if nlines == ipos:
            nsamp+=1;   
            opfile.write(i);
        if nlines > ipos:
            n_entries+=1;
            if n_entries%p == 0:
                opfile.write(i);
                if nlines == fpos :
                    flag=1;        #print "reached end by div" 
                nsamp+=1;
        if nlines == fpos:
            nsamp+=1;
            if flag == 0:
                opfile.write(i);   #print "reached eof.."
            break 

nsamp=nsamp-flag;
print "No. of entries in output file = ",(nsamp)


#print "nlines at the end of loop : "
#print nlines
#print "value of flag is : ",flag

inpfile.close()
opfile.close()



