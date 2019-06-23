def create_heroes(headers, h):
	hero = {}
	for i,hdr in enumerate(headers):
		#Strip white space
		hero[hdr].strip() = h[i];
		
	print(hero)
	return hero
	
with open('heroes.csv') as heroes:
	headers = None
	for i,h in enumerate(heroes):
		if i == 0:
			headers = h.split(',')
		else:
			hero_list = create_heroes(headers, h.split(','))
