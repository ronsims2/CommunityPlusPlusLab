def create_heroes(headers, h, f, p):
	hero = {}
	for i,hdr in enumerate(headers):
		#Strip white space
		hero[hdr.strip()] = h[i].strip(); 
	
	hero['friends'] = f[hero['id']]
	hero['powers'] = p[hero['id']]
	print(hero)
	return hero
	
def map_key_pairs_to_list(filename):
	item_map = {}
	with open(filename) as items:
		for item in items:
			it = item.strip().split(',')
			if item_map.get(it[0]):
				item_map[it[0]].append(it[1])
			else:
				item_map[it[0]] = [it[1]]
		
	return item_map
	
	
friend_ref = map_key_pairs_to_list('heroes_friends.csv')
power_ref = map_key_pairs_to_list('heroes_powers.csv')

#print(friend_ref)
#print(power_ref)
	
with open('heroes.csv') as heroes:
	headers = None
	for i,h in enumerate(heroes):
		if i == 0:
			headers = h.split(',')
		else:
			hero_list = create_heroes(headers, h.split(','), friend_ref, power_ref)
