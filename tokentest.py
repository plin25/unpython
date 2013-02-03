import sys
import tokenize
from token import *

penalty = 0
names = set()
builtin = set()

map(lambda x:builtin.add(x), [
"abs","divmod","input","open","staticmethod",
"all","enumerate","int","ord","str",
"any","eval","isinstance","pow","sum",
"basestring","execfile","issubclass","print","super",
"bin","file","iter","property","tuple",
"bool","filter","len","range","type",
"bytearray","float","list","raw_input","unichr",
"callable","format","locals","reduce","unicode",
"chr","frozenset","long","reload","vars",
"classmethod","getattr","map","repr","xrange",
"cmp","globals","max","reversed","zip",
"compile","hasattr","memoryview","round","__import__",
"complex","hash","min","set","apply",
"delattr","help","next","setattr","buffer",
"dict","hex","object","slice","coerce",
"dir","id","oct","sorted","intern"])

reserved = set()

map(lambda x:reserved.add(x), [
"and","del","from","not","while",
"as","elif","global","or","with",
"assert","else","if","pass","yield",
"break","except","import","print",
"class","exec","in","raise",
"continue","finally","is","return",
"def","for","lambda","try"])

tok_names = {0: 'ENDMARKER',
 256: 'NT_OFFSET',
 2: 'NUMBER',
 3: 'STRING',
 4: 'NEWLINE',
 5: 'INDENT',
 6: 'DEDENT',
 7: 'LPAR',
 8: 'RPAR',
 9: 'LSQB',
 10: 'RSQB',
 11: 'COLON',
 12: 'COMMA',
 13: 'SEMI',
 14: 'PLUS',
 15: 'MINUS',
 16: 'STAR',
 17: 'SLASH',
 18: 'VBAR',
 19: 'AMPER',
 20: 'LESS',
 21: 'GREATER',
 22: 'EQUAL',
 23: 'DOT',
 24: 'PERCENT',
 25: 'BACKQUOTE',
 26: 'LBRACE',
 27: 'RBRACE',
 28: 'EQEQUAL',
 29: 'NOTEQUAL',
 30: 'LESSEQUAL',
 31: 'GREATEREQUAL',
 32: 'TILDE',
 33: 'CIRCUMFLEX',
 34: 'LEFTSHIFT',
 35: 'RIGHTSHIFT',
 36: 'DOUBLESTAR',
 37: 'PLUSEQUAL',
 38: 'MINEQUAL',
 39: 'STAREQUAL',
 40: 'SLASHEQUAL',
 41: 'PERCENTEQUAL',
 42: 'AMPEREQUAL',
 43: 'VBAREQUAL',
 44: 'CIRCUMFLEXEQUAL',
 45: 'LEFTSHIFTEQUAL',
 46: 'RIGHTSHIFTEQUAL',
 47: 'DOUBLESTAREQUAL',
 48: 'DOUBLESLASH',
 49: 'DOUBLESLASHEQUAL',
 50: 'AT',
 1: 'NAME',
 52: 'ERRORTOKEN',
 53: 'N_TOKENS',
 51: 'OP'}

b=0
bc=0
bd=0
bpenalty=0
cpenalty=0
tpenalty=0
semis = 0
indents = dict()
def analyze(f):
    global b,bc,bd,bpenalty,cpenalty,tpenalty,semis
    indspaces = 0
    curindent = -1
    for t in tokenize.generate_tokens(f.readline):
        print(t)
        tok_type = tok_name[t[0]]
        print(tok_type)
        if (tok_type == 'NAME'):
            if t[1] not in reserved:
                names.add(t[1])
            elif t[1]=="if" or t[1]=="elif":
                b=1
            if t[1]=='try':
                tpenalty += 10
        elif tok_type == 'OP':
            if t[1] == ';':
                semis += 1
        elif tok_type == 'INDENT':
            if curindent != len(t[1]):
                if len(t[1]) not in indents:
                    indents[len(t[1])] = 1
                else:
                    indents[len(t[1])] += 1
                curindent = len(t[1])
        elif tok_type == 'COMMENT' or (tok_type == 'STRING' and "\"\"\"" in t[1]):
            #print(t)
            """
                STUFF
            """
            cpenalty+=10;
        if b and (t[1]=="==" or t[1]==">" or t[1]==">=" or t[1]=="<=" or t[1]=="<" or t[1]=="!="):
            bc+=1
        elif b and (t[1]=="True" or t[1]=="is" or t[1]=="False"):
            bd+=1
        elif b and t[1]==':':
            if bc <=5:
               bpenalty+=10
            bpenalty-=bd*10
            bd=0   
            bc=0
            b=0

def indents_gcd():
    import fractions
    seen = set()
    for i in indents.keys():
        r = 1
        for s in seen:
            if i%s==0:
                r = 0
                break
        if r == 1:
            seen.add(i)
    return len(seen)


lp = 0 #lines greater than 80 chars
wspb = 0 # bad white space
def lines(f):
    import re
    global lp, wspb
    for l in f.readlines():
        if len(l) > 79:
            lp +=      1
        wspb +=  len(re.findall('[([{] ',l))
        wspb  +=  len(re.findall(' [([)\]}]'   ,l)   )
        wspb += len(re.findall(' ,;:',l))
        wspb += len(re.findall('  +[=<>*+-/%]',l))
        wspb += len(re.findall('[=<>*+-/%]  +',l))
    return (lp,wspb)


def main(argv):
    global semis
    global penalty
    source_path = argv[1]
    f = open(source_path,"r")
    analyze(f)
    tmp = 0
    print(indents_gcd()) #TODO punish this
    f.seek(0)
    global lp,wspb #TODO punish this
    lines(f)
    for w in names:
    #    print w
        if len(w)>=3 and len(w)<=20:
            tmp+=10
    #tmp /= len(names)
    penalty += tmp
    print(penalty)
    print(bpenalty)
    print(cpenalty)
    print(tpenalty)


if __name__ == "__main__":
    main(sys.argv)
