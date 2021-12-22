import re

with open('strings-acu_nilai.txt', 'r') as f:
	raw = f.read()

repair = re.sub(r'\t', '\n', raw)

with open('kamus-indonesia.txt', 'w') as f:
	f.write(repair)