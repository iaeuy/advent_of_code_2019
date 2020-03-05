def get_asteroids():
	with open("input.txt", "r") as file:
		region_map = file.read().split('\n')
		region_map.pop()

	asteroids = []
	for i in range(len(region_map)):
		for j in range(len(region_map[0])):
			if region_map[i][j] == '#':
				asteroids.append((j, i))
	return asteroids

def most_monitored(asteroids):
	monitored = {}
	for a in asteroids:
		slopes = set() # slope along with whether other asteroid is to left or right
		for b in asteroids:
			if a == b:
				continue
			if a[0] == b[0]:
				direction = "up" if a[1] < b[1] else "down"
				slopes.add((float("inf"), direction))
			else:
				direction = "right" if a[0] < b[0] else "left"
				slope = (b[1] - a[1]) / (b[0] - a[0])
				slopes.add((slope, direction))
		monitored[a] = slopes
	best = max(asteroids, key = lambda a: len(monitored[a]))
	return best, len(monitored[best])

def vaporize_asteroids(asteroids, station):
	slopes = set()
	asteroids_by_slope = {}

	for a in asteroids:
		if a == station:
			continue
		if a[0] == station[0]:
			direction = 1 if a[1] < station[1] else 0
			slope = float("inf")
		else:
			direction = 0 if a[0] < station[0] else 1
			slope = (a[1] - station[1]) / (station[0] - a[0])
		slopes.add((direction, slope))
		if (direction, slope) in asteroids_by_slope:
			asteroids_by_slope[(direction, slope)].append(a)
		else:
			asteroids_by_slope[(direction, slope)] = [a]

	slopes = list(slopes)
	slopes.sort(reverse=True)
	def dist(asteroid, station):
		return (a[0] - station[0])**2 + (a[1] - station[1])**2
	for s in asteroids_by_slope:
		asteroids_by_slope[s].sort(key=lambda a: dist(a, station), reverse=True)

	vaporized = []
	i = 0
	while len(vaporized) < len(asteroids) - 1:
		s = slopes[i]
		if asteroids_by_slope[s]:
			vaporized.append(asteroids_by_slope[s].pop())
		i = (i + 1) % len(slopes)

	return vaporized

		

def main():
	asteroids = get_asteroids()
	station = most_monitored(asteroids)[0]
	vaporize_asteroids(asteroids, station)
	# print(vaporize_asteroids(asteroids, station)[199], station)

if __name__ == '__main__':
	main()