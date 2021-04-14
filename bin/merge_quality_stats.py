#!/usr/bin/env python

import sys


def table(dictionary):
	seq_len = [i[2] for i in dictionary.values()]
	print("<tr>")
	print("<td>Sequence length</td>")
	for element in seq_len:
		print(f"<td>{element}</td>")
	print("</tr>")

	total_seq = [i[3] for i in dictionary.values()]
	print("<tr>")
	print("<td>Total Sequences</td>")
	for element in total_seq:
		print(f"<td>{element}</td>")
	print("</tr>")

	gc_content = [i[4] for i in dictionary.values()]
	print("<tr>")
	print("<td>%GC</td>")
	for element in gc_content:
		print(f"<td>{element}</td>")
	print("</tr>")

	return

file = sys.argv[1]

pre_dict = {}
post_dict = {}


with open(file,"r") as infile:
	infile = infile.readlines().sort()


# 0: prepost, 1: filename, 2: seqlen, 3: nseqs, 4: gc_content, 5: path
for samplename,prepost,filename,seqlen,nseqs,gc_content,path in infile:
	pre_dict[samplename] = []
	post_dict[samplename] = []

	if prepost == "pre":
		pre_dict[samplename].append([filename,seqlen,nseqs,gc_content,path])

	if prepost == "post":
		post_dict[samplename].append([filename,seqlen,nseqs,gc_content,path])


print("<table class='table'>\
		 			<tr>\
            <thead>\
              <th>Sample</th>")


for key in pre_dict.keys():
	print(f"<th>{key}</th>")
print("</thead><tbody></tr>")
print(f"<tr><td colspan='{len(pre_dict.keys())+1}' class='info'>Pre-Filter</td></tr>")
table(pre_dict)

print(f"</tr><tr><td colspan='{len(post_dict.keys())+1}'class='info'>Post-Filter</td></tr>")
table(post_dict)

print("</tbody></table></div><div><br>")

print ("<p>Pre-Filter Reports:</p><ul>")
for key in pre_dict.keys():
	print(f"<li><a target='_blank' href='{pre_dict[key][-1]}'>{key}</a></li>")
print("</ul>")

print("<p>Post-Filter Reports:</p><ul>")
for key in post_dict.keys():
	print(f"<li><a target='_blank' href='{post_dict[key][-1]}'>{key}</a></li>")
print("</ul>")






