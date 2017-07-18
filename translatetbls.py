import sys 
import numpy
import pandas
import os.path

CHARCOUNT = 15

#####################################################################

def translatec (c):

    if c == u'\xb0':
        return "$\\deg$ "
    elif c == u'\xa0':
        return " "
    elif c == u'\u0394':
        return "$\\Delta$ "
    elif c == '%':
        return "$\\%$ "
    elif c == '@':
        return "$@$"
    elif c == '/':
        return "\\textbackslash "
    elif c == '\\':
        return "\\ "
    elif c == u'\u2013':
        return "-"
    elif c == u'\u2192':
        return "$\\rightarrow$"
    elif c == u'\u223c':
        return "$\\sim$"
    elif c == u'\u2212':
        return "-"
    elif c == u'\u2009':
        return " "
    elif c == u'\xb7':
        return "$\\cdot$"
    elif c == u'\u2a7d':
        return "$\\leq$"
    elif c == u'\u03b1':
        return "$\\alpha$"
    elif c == u'\u03b2':
        return "$\\beta$"
    elif c == '{':
        return "$\\{$"
    elif c == '}':
        return "$\\}$"
    elif c == '[':
        return "$[$"
    elif c == ']':
        return "$]$"
    elif c == '&':
        return "\&"
    elif c == u'\u2032':
        return "\\\'"
 

    return c

#####################################################################

def write_char_by_char (line):
    if len(line) > CHARCOUNT:
        sys.stdout.write("\\footnote{")

    for c in line:
        sys.stdout.write("%s"%(translatec(c)))

    if len(line) > CHARCOUNT:
        sys.stdout.write("}")

#####################################################################

def write_char_by_char_cite (line):
    sys.stdout.write("\\cite{")

    for c in line:
        sys.stdout.write("%s"%(translatec(c)))

    if len(line) > 10:
        sys.stdout.write("}")

#####################################################################

def write_char_by_char_all (line):
    for c in line:
        sys.stdout.write("%s"%(translatec(c)))

#####################################################################


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
        sys.stdout.write("%s"%(translatec(c)))
    sys.stdout.write(" & ")

for c in cnames[-1]:
    sys.stdout.write("%s"%(translatec(c)))

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
    write_char_by_char_all(allcolumn[0][i])
    sys.stdout.write(" & ")
    for j in range(1,cols-1):
        write_char_by_char (allcolumn[j][i])
        sys.stdout.write(" & ")
    write_char_by_char_cite (allcolumn[-1][i])
    sys.stdout.write(" \\\\ \n ")
