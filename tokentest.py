import tokenize
from token import *
f = open("test.py","r")
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

def analyze():
    for t in tokenize.generate_tokens(f.readline):
        if tok_name[t[0]] == 'NAME':
            if t[1] not in reserved:
                names.add(t[1])
                print(t[1])
tmp = 0
for w in names:
    tmp += len(w)
tmp /= len(names)
penalty += tmp*3.0
print(penalty)
