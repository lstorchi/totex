import sys 
import numpy
import pandas
import os.path

sys.path.append("./")
import baseutiltex


file = ""

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    print "Usage ", sys.argv[0] , " filename "
    exit(1)

df = pandas.read_excel(file, header=1)

cnames = df.columns

#Header 

for cn in cnames[:-1]:
    for c in cn:
        sys.stdout.write("%s"%(baseutiltex.translatec(c)))
    sys.stdout.write(" & ")

for c in cnames[-1]:
    sys.stdout.write("%s"%(baseutiltex.translatec(c)))

sys.stdout.write(" \\\\ \n")

#Data 

allcolumn = []
for cn in cnames:
    colum = []
    for v in df[cn].values:
        if type(v) is int:
            vstr = str(v)
        elif type(v) is float:
            vstr = str(v)
        elif type(v) is numpy.float64:
            vstr = str(v)
        elif type(v) is numpy.int64:
            vstr = str(v)
        else:
            vstr = v
        
        colum.append(vstr)

    allcolumn.append(colum)

for c in allcolumn[1:]:
    if len(c) != len(allcolumn[0]):
        print "Error in column dimension"
        exit(1)

cols = len(allcolumn)
rows = len(allcolumn[0])

for i in range(rows):
    baseutiltex.write_char_by_char_all(allcolumn[0][i])
    sys.stdout.write(" & ")
    for j in range(1,cols-1):
        baseutiltex.write_char_by_char (allcolumn[j][i])
        sys.stdout.write(" & ")
    baseutiltex.write_char_by_char_cite (allcolumn[-1][i])
    sys.stdout.write(" \\\\ \n ")
