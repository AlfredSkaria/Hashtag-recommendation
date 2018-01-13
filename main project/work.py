import re
with open("432", 'r') as f:
    content = f.read()
match1 = re.findall('Text:(.*)[\n]', content)
match2 = re.findall('Type:(.*)[\n]', content)
match3 = re.findall('Origin:(.*)[\n]', content)
match4 = re.findall('ID:(.*)[\n]', content)
match5 = re.findall('Hashtags:(.*)[\n]', content)
match6 = re.findall('Time:(.*)[\n]', content)
fopen = open("output.txt",'w')
fopen.write(match1)

#print(match1)
