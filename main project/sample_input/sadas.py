f = open('output.txt','r')
fout = open('serikkumout','w')

for line in f:
	for i in range( len( line) ):
		if line[i] == "\'":
			if  line[i+1] == ',':
				#i = i + 2
				fout.write('\n')
		else:
			fout.write(line[i])