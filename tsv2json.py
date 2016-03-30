#!/usr/bin/python

y1931_table = {}
y1932_table = {}

barley = []

f = open("barley.tsv",'r')
for line in f:
	line =line.rstrip()
	#print line
	(yyield, variety, year, site) = line.split('\t')
	if yyield == 'yield': continue
	if year == '1931':
		y1931_table[(site, variety)] = yyield
	if year == '1932':
		y1932_table[(site, variety)] = yyield
	#print y1931_table
	#print y1932_table
f.close()

for key in y1931_table:
	site, variety = key
	each_point = []
	each_point.append(site)
	each_point.append(variety)
	each_point.append(y1932_table[key])
	each_point.append(y1931_table[key])
	barley.append(each_point)

f = open('new_barley.tsv','w')
line = 'site\tvariety\tx\ty\n'
f.write(line)
for data in barley:
	(site, variety, x, y) = data
	line = '%s\t%s\t%s\t%s\n'%(site,variety,x,y)
	f.write(line)
f.close()


