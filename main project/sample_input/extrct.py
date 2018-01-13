import re

with open("data_prep.txt",'r') as fin:
	content = fin.read()
match1 = re.findall("[^'']+",content)

fout = open("out.txt",'w')
fout.write(str(match1))
