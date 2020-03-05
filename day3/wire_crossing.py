def closest_intersection():
	with open("example2.txt", "r") as file:
		wires = file.read().split('\n')
		wires.pop()
	wire1_h, wire1_v = wire_to_lines(wires[0].split(','))
	wire2_h, wire2_v = wire_to_lines(wires[1].split(','))
	closest_dist = float("inf")

	for h in wire1_h:
		for v in wire2_v:
			closest_dist = min(closest_dist, manhat_distance(intersection(h, v)))
	for h in wire2_h:
		for v in wire1_h:
			closest_dist = min(closest_dist, manhat_distance(intersection(h, v)))

	return closest_dist


def wire_to_lines(wire):
	"""
	Given wire, return list of horizontal and vertical line segments
	Segments are represented as a pair of endpoints (x1, y1, x2, y2).
	They always go left to right or bottom to top.
	"""
	horizontal_lines = vertical_lines = []
	curr_start = (0,0)
	for s in wire:
		direction = s[0]
		length = float(s[1:])
		if direction == 'R':
			new_start = (curr_start[0] + length, curr_start[1])
			horizontal_lines.append(curr_start + new_start)
		elif direction == 'L':
			new_start = (curr_start[0] - length, curr_start[1])
			horizontal_lines.append(new_start + curr_start)
		elif direction == 'U':
			new_start = (curr_start[0], curr_start[1] + length)
			vertical_lines.append(curr_start + new_start)
		elif direction == 'D':
			new_start = (curr_start[0], curr_start[1] - length)
			vertical_lines.append(new_start + curr_start)
		else:
			print("Invalid direction")
			return
		curr_start = new_start

	# horizontal_lines = sorted(horizontal_lines)
	# vertical_lines = sorted(vertical_lines, key = lambda line: line[1])
	return horizontal_lines, vertical_lines

def intersection(h_seg, v_seg):
	# intersection point of horizontal seg with vertical seg, or (inf, inf) if invalid
	intersection = (0, 0)
	x = v_seg[0]
	y = h_seg[1]
	if h_seg[0] <= x and x <= h_seg[2] and v_seg[1] <= y and y <= v_seg[3]:
		intersection = (x, y)

	if intersection == (0, 0):
		return (float("inf"), float("inf"))
	else:
		return intersection


def manhat_distance(point1, point2 = (0,0)):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def main():
	print(closest_intersection())

if __name__ == '__main__':
	main()