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

for t in tokenize.generate_tokens(f.readline):
    if tok_name[t[0]] == 'NAME':
        if t[1] not in reserved:
            names.add(t[1])
            print(t[1])
tmp = 0
for w in names:
	if len(w)>=3 and len(w)<=20:
		tmp+=10
tmp /= len(names)
penalty += tmp
print(penalty)
