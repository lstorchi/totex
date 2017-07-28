import sys 

CHARCOUNT = 15

###############################################################################

def translateuc (c):

    if c == u'\xa0':
        return " "
    elif c == u'\u2013':
        return "-"
    elif c == u'\u2212':
        return "-"
    elif c == u'\u2009':
        return " "
    elif c == u'\u0394':
        return "D"
    elif c == u'\u2a7d':
        return "<="
    elif c == u'\u223c':
        return "~"

    return c

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

    sys.stdout.write("}")

#####################################################################

def write_char_by_char_all (line):
    for c in line:
        sys.stdout.write("%s"%(translatec(c)))

#####################################################################

