import re
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

temp = []
pres = []
kine = []
csvl = []
mxwt = []
dhvl = []

for i in range(rows):
    for j in range(2,8):
        s = re.sub('\[[^\]]+\]', '', allcolumn[j][i])
        news = ""
        for k in range(len(s)):
            news += baseutiltex.translateuc(s[k])
        
        if j == 2:
            temp.append(news)
        elif j == 3:
            pres.append(news)
        elif j == 4:
            kine.append(news)
        elif j == 5:
            csvl.append(news)
        elif j == 6:
            mxwt.append(news)
        elif j == 7:
            dhvl.append(news)

#        sys.stdout.write(news + " | ")
#    sys.stdout.write("\n")

# example 
equilibrium = []
for t in temp:
    tokens = t.split(",")
    tequilibrium = False
    for v in tokens:
        if "(e)" in v:
            nv = re.sub('\([^\)]+\)', '', v)
            equilibrium.append(nv)
            tequilibrium = True

    if not tequilibrium:
        equilibrium.append("")

for e in equilibrium:
    print e
