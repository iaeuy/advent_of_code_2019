def closest_intersection():
	with open("input.txt", "r") as file:
		wires = file.read().split('\n')
		wires.pop()
	wire1 = wire_to_lines(wires[0].split(','))
	wire2 = wire_to_lines(wires[1].split(','))
	closest_dist = float("inf")

	# curr_dist = 0
	# for seg1 in wire1:
	# 	curr_wire_dist = curr_dist
	# 	for seg2 in wire2:
	# 		closest_dist = min(closest_dist, intersection_dist(seg1, seg2, curr_wire_dist))
	# 		curr_wire_dist += seg_length(seg2)
	# 	curr_dist += seg_length(seg1)


	# more verbose but more optimized
	curr_dist = 0
	i = 0
	while closest_dist == float("inf"): # first find earliest intersection of wire1 with wire2
		curr_seg = wire1[i]
		curr_wire_dist = curr_dist
		j = 0

		while closest_dist == float("inf") and j < len(wire2):
			other_seg = wire2[j]
			closest_dist = min(closest_dist, intersection_dist(curr_seg, other_seg, curr_wire_dist))
			curr_wire_dist += seg_length(other_seg)
			j += 1

		curr_dist += seg_length(curr_seg)
		i += 1

	curr_dist = 0
	k = 0
	while curr_dist < closest_dist and k < j: # now go back through wire2 to check no shorter intersections
		curr_seg = wire2[k]
		curr_wire_dist = curr_dist
		for other_seg in wire1:
			closest_dist = min(closest_dist, intersection_dist(curr_seg, other_seg, curr_wire_dist))
			curr_wire_dist += seg_length(other_seg)
			if curr_wire_dist >= closest_dist:
				break
		curr_dist += seg_length(curr_seg)
		k += 1

	return closest_dist


def wire_to_lines(wire):
	"""
	Given wire, return list of line segments in order.
	Segments are represented as (x1, y1, x2, y2, direction).
	Points are listed left to right and top to bottom
	"""
	lines = []
	curr_start = (0,0)
	for s in wire:
		direction = s[0]
		length = float(s[1:])
		if direction == 'R':
			new_start = (curr_start[0] + length, curr_start[1])
			lines.append(curr_start + new_start + (direction,))
		elif direction == 'L':
			new_start = (curr_start[0] - length, curr_start[1])
			lines.append(new_start + curr_start + (direction,))
		elif direction == 'U':
			new_start = (curr_start[0], curr_start[1] + length)
			lines.append(curr_start + new_start + (direction,))
		elif direction == 'D':
			new_start = (curr_start[0], curr_start[1] - length)
			lines.append(new_start + curr_start + (direction,))
		else:
			print("Invalid direction")
			return
		curr_start = new_start

	return lines

def intersection_dist(seg1, seg2, prev_distance):
	# length of wires to intersection point of horizontal seg with vertical seg, or inf if invalid
	# prev_distance is distance to start of h_seg and v_seg
	start1 = start(seg1)
	start2 = start(seg2)
	point = (float("inf"), float("inf"))
	if (seg1[4] == 'R' or seg1[4] == 'L') and (seg2[4] == 'U' or seg2[4] == 'D'):
		point = intersection(seg1, seg2) 
	elif (seg1[4] == 'U' or seg1[4] == 'D') and (seg2[4] == 'R' or seg2[4] == 'L'):
		point = intersection(seg2, seg1)
	return prev_distance + manhat_distance(start1, point) + manhat_distance(start2, point)

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

def start(seg):
	# starting point of segment
	if seg[4] == 'R' or seg[4] == 'U':
		return seg[:2]
	elif seg[4] == 'L' or seg[4] == 'D':
		return seg[2:4]
	else:
		print("Invalid direction")
		return

def seg_length(seg):
	return manhat_distance(seg[:2], seg[2:4])

def manhat_distance(point1, point2 = (0,0)):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def main():
	print(closest_intersection())

if __name__ == '__main__':
	main()