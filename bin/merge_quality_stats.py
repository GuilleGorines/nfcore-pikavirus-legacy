#!/usr/bin/env python

import sys


def table(dictionary):
	for key,values in dictionary.items():
		if values[0] == "paired":
			for sublist in values[1:]:
				filename = [i[0] for i in sublist]
				print("<tr>")
				print("<td>Filename</td>")
				for element in filename:
					print(f"<td>{element}</td>")
				print("</tr>")

				seq_len = [i[1] for i in sublist]
				print("<tr>")
				print("<td>Sequence length</td>")
				for element in seq_len:
					print(f"<td>{element}</td>")
				print("</tr>")

				total_seq = [i[2] for i in sublist]
				print("<tr>")
				print("<td>Total Sequences</td>")
				for element in total_seq:
					print(f"<td>{element}</td>")
				print("</tr>")

				gc_content = [i[3] for i in sublist]
				print("<tr>")
				print("<td>%GC</td>")
				for element in gc_content:
					print(f"<td>{element}</td>")
				print("</tr>")
		else:
			filename = [i[0] for i in values]
			print("<tr>")
			print("<td>Filename</td>")
			for element in filename:
				print(f"<td>{element}</td>")
			print("</tr>")

			seq_len = [i[1] for i in values]
			print("<tr>")
			print("<td>Sequence length</td>")
			for element in seq_len:
				print(f"<td>{element}</td>")
			print("</tr>")

			total_seq = [i[2] for i in values]
			print("<tr>")
			print("<td>Total Sequences</td>")
			for element in total_seq:
				print(f"<td>{element}</td>")
			print("</tr>")

			gc_content = [i[3] for i in values]
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
	infile = sorted(infile.readlines())
	infile = [element.replace("\n","") for element in infile]
	infile = [element.split(",") for element in infile]



# 0: prepost, 1: filename, 2: seqlen, 3: nseqs, 4: gc_content, 5: path
for sample in infile:
	samplename = sample[0]
	end = sample[1]
	prepost = sample[2]
	filename = sample[3]
	seqlen = sample[4]
	nseqs = sample[5]
	gc_content = sample[6]
	path = sample[7]

	if end == "single_end":
		if prepost == "pre":
			pre_dict[samplename] = [filename,seqlen,nseqs,gc_content,path]

		if prepost == "post":
			post_dict[samplename] = [filename,seqlen,nseqs,gc_content,path]
	
	else:
		pre_dict[samplename] = ["paired"]
		post_dict[samplename] = ["paired"]

		if prepost == "pre":
			pre_dict[samplename].append([filename,seqlen,nseqs,gc_content,path])

		if prepost == "post":
			post_dict[samplename].append([filename,seqlen,nseqs,gc_content,path])

print("<table class='table'>\
		 			<tr>\
            <thead>\
              <th>Sample</th>")

col_number = 0
for key,values in pre_dict.items():

	if values[0] == "paired":
		col_number += 2
		print(f"<th>{key}</th>")
		print(f"<th>{key}</th>")

	else:
		col_number += 1
		print(f"<th>{key}</th>")

print("</thead><tbody></tr>")
print(f"<tr><td colspan='{col_number}' class='info'>Pre-Filter</td></tr>")
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






