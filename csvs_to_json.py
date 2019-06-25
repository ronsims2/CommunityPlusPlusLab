def create_heroes(headers, h, f):
	hero = {}
	for i,hdr in enumerate(headers):
		#Strip white space
		hero[hdr.strip()] = h[i].strip(); 
	
	hero['friends'] = f[hero['id']]
	print(hero)
	return hero
	
def preprocess_friends():
	friend_map = {}
	with open('heroes_friends.csv') as friends:
		for f in friends:
			f_vals = f.strip().split(',')
			if friend_map.get(f_vals[0]):
				friend_map[f_vals[0]].append(f_vals[1])
			else:
				friend_map[f_vals[0]] = [f_vals[1]]
		
	return friend_map
	
	
friend_ref = preprocess_friends()

print(friend_ref)
	
with open('heroes.csv') as heroes:
	headers = None
	for i,h in enumerate(heroes):
		if i == 0:
			headers = h.split(',')
		else:
			hero_list = create_heroes(headers, h.split(','), friend_ref)
