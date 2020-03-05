def num_orbits():
	with open("input.txt", "r") as file:
		direct_orbits = file.read().split('\n')
		direct_orbits.pop()

	# create adjacency table
	edges = {}
	for orbit in direct_orbits:
		p1, p2 = orbit.split(')')
		if p1 in edges:
			edges[p1].append(p2)
		else:
		 	edges[p1] = [p2]

	# DFS while counting distances
	count = 0
	stack = [("COM", 0)]
	while stack:
		curr_obj, curr_dist = stack.pop()
		count += curr_dist
		if curr_obj in edges:
			for other in edges[curr_obj]:
				stack.append((other, curr_dist + 1))

	return count

def orbit_transfers():
	with open("input.txt", "r") as file:
		direct_orbits = file.read().split('\n')
		direct_orbits.pop()

	# create adjacency table
	edges = {}
	for orbit in direct_orbits:
		p1, p2 = orbit.split(')')
		
		if p1 in edges:
			edges[p1].append(p2)
		else:
		 	edges[p1] = [p2]

		if p2 in edges:
			edges[p2].append(p1)
		else:
			edges[p2] = [p1]

	# BFS
	steps = 0
	fringe = {"YOU"}
	visited = set()
	while fringe:
		new_fringe = set()
		for obj in fringe:
			if obj == "SAN":
				return steps - 2
			if obj not in visited:
				visited.add(obj)
				for other in edges[obj]:
					new_fringe.add(other)
		fringe = new_fringe
		steps += 1

	print("SAN not found")
	return


def main():
	print(orbit_transfers())

if __name__ == '__main__':
	main()