pat = """\t\t<Transform translation="%0.2f 0 0">\n\t\t<Shape use="white_key">\n\t\t</Shape>\n\t\t</Transform>\n\n"""
pat2 = """\t\t<Transform translation="%0.2f 0 0">\n\t\t<Shape use="black_key">\n\t\t</Shape>\n\t\t</Transform>\n\n"""

with open('out.txt', 'w') as f:
	for i in range(1, 52):
		diff = i * 0.15
		res = pat % diff
		
		# f.write(res)

	
with open('out2.txt', 'w') as f2:
	
	for i in range(50):
		if i % 7 == 3 or i % 7 == 0:
			continue
		diff = (i + 1) * 0.15
		res = pat2 % diff
		
		f2.write(res)