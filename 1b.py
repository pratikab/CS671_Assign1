#!/usr/bin/python2
import fileinput
import re
def my_replace(match):
	match = match.group()
	return "<s> "+match+" </s>"
out_file = open('1b_output.txt', 'w')
in_file = open('test.txt', 'r')
data = in_file.read()
data2 = data.split('\n\n')
regex = r'[\'"]?[A-Z]([^A-Z]|[A-Z](.|\s){2,2}?){2,}?([\.!?]|--(\n|\'\n))[\'"]?(?=(\s)*?[\'"]?([A-Z]|$))'
out_data = ''
for i in range(len(data2)):
	feed = '\n'+data2[i]+'\n'
	replacement = re.sub(regex , my_replace, feed)
	out_data += replacement[1:]+'\n'
out_file.write("%s\n" % out_data)
