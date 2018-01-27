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
out_data = re.sub(r'\W\'(.|\s)*?\'\s', my_replace, data)
out_file.write("%s\n" % out_data)
