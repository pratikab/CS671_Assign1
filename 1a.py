#!/usr/bin/python2
import fileinput
import re
def my_replace(match):
	match = match.group()
	temp = match.split("\'")
	temp2 = '\''.join(temp[1:len(temp)-1])
	temp3 = temp[0]+'\"'+temp2+'\"'+temp[len(temp)-1]
	return temp3
out_file = open('output.txt', 'w')
in_file = open('test.txt', 'r')
data = in_file.read()
data2 = data.split('\n\n')
regex = r'\s\'([^\']|(\w\')|(\s\'(.|\s)*?\'(\s|;)))*?[?.!,-]\'\s'
out_data = ''
for i in range(len(data2)):
	feed = '\n'+data2[i]+'\n'
	replacement = re.sub(regex , my_replace, feed)
	out_data += replacement[1:]+'\n'
out_file.write("%s\n" % out_data)
