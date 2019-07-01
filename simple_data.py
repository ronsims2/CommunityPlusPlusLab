# Think of headers as keys in a simple dictionary

heroes =  """id, name, alias
A, Alpha, alef
B, Beta, bet
G, Gamma, gimmel"""
 
hero_list = heroes.split('\n')

data = []
headers = None

for i, line in enumerate(hero_list):
	if i == 0:
		# create headers
		headers = line.strip().split(',')
	else:
		# build object
		d = {}
		l = line.strip().split(',')
		for j, h in enumerate(headers):
			d[h] = l[j]
		
		data.append(d)
		
	
	print(data)
