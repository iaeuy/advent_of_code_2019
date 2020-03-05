from intcode_computer import IntcodeComputer

class EHP_Robot(): 
	"""
	Emergency hull painting robot. Runs intcode problem.
	Intcode program takes color of current panel as input. 
	Outputs color to paint panel and direction to turn. Robot
	then moves.
	"""
	CODE = [3,8,1005,8,342,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,29,2,1006,19,10,1,1005,19,10,2,1102,11,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,62,2,1009,15,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,88,2,1101,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,114,1,105,8,10,1,1102,18,10,2,6,5,10,1,2,15,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,153,1,105,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,178,1,1006,15,10,1006,0,96,1006,0,35,1,104,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,214,1006,0,44,2,1105,17,10,1,1107,19,10,1,4,16,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,252,1006,0,6,1,1001,20,10,1006,0,45,2,1109,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,287,2,101,20,10,2,1006,18,10,1,1009,9,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,321,101,1,9,9,1007,9,1031,10,1005,10,15,99,109,664,104,0,104,1,21102,48210117528,1,1,21102,1,359,0,1105,1,463,21102,932700763028,1,1,21102,370,1,0,1105,1,463,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,179557207079,1,21102,417,1,0,1105,1,463,21102,1,28994202816,1,21101,0,428,0,1105,1,463,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,709580710756,1,21102,1,451,0,1106,0,463,21102,825016201984,1,1,21101,462,0,0,1106,0,463,99,109,2,21201,-1,0,1,21102,40,1,2,21101,0,494,3,21102,1,484,0,1105,1,527,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,489,490,505,4,0,1001,489,1,489,108,4,489,10,1006,10,521,1101,0,0,489,109,-2,2105,1,0,0,109,4,1201,-1,0,526,1207,-3,0,10,1006,10,544,21102,1,0,-3,21202,-3,1,1,22102,1,-2,2,21102,1,1,3,21102,563,1,0,1105,1,568,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,591,2207,-4,-2,10,1006,10,591,21202,-4,1,-4,1105,1,659,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,610,1,0,1106,0,568,21201,1,0,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,629,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,651,21202,-1,1,1,21102,1,651,0,106,0,526,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

	def __init__(self):
		self.intcode = IntcodeComputer(self.CODE)
		self.white_panels = set() # set of white tiles
		self.painted_panels = set() # set of tiles painted at least once
		self.position = (0, 0) # start at origin
		self.direction = (0, 1) # direction vector; start facing up

	def change_direction(self, orientation):
		"""
		Rotate direction vector counterclockwise (turn left) if orientation == 0:
		Rotate clockwise (turn right) if orientation == 1
		"""
		x, y = self.direction
		if orientation == 0:
			self.direction = (-y, x)
		else:
			self.direction = (y, -x)


	def paint(self):
		while not self.intcode.halted:
			curr_pos_color = 1 if self.position in self.white_panels else 0
			self.intcode.receive_inputs([curr_pos_color])
			self.intcode.run_code()

			new_color, orientation = self.intcode.broadcast_outputs()
			if new_color == 1:
				self.white_panels.add(self.position)
			else:
				self.white_panels.discard(self.position)
			self.painted_panels.add(self.position)

			self.change_direction(orientation)
			self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])



def main():
	r = EHP_Robot()
	
	# part 1
	# r.paint()
	# print(len(r.painted_panels))

	# part 2
	r.white_panels.add((0,0))
	r.paint()
	x_max = max([x for (x,y) in r.white_panels])
	x_min = min([x for (x,y) in r.white_panels])
	y_max = max([y for (x,y) in r.white_panels])
	y_min = min([y for (x,y) in r.white_panels])

	x_range = x_max - x_min + 1
	y_range = y_max - y_min + 1

	image = [[0]*x_range for y in range(y_range)]
	for y in range(len(image)):
		for x in range(len(image[0])):
			if (x + x_min, y_max - y) in r.white_panels:
				image[y][x] = '#'
			else:
				image[y][x] = '.'

	for row in image:
		print(row)

if __name__ == '__main__':
	main()



