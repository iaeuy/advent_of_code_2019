INTCODE = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

def run_code(intcode):
	iterable = iter(intcode)
	for opcode in iterable:
		if opcode == 99:
			return
		elif opcode == 1:
			op = lambda x,y: x + y
		elif opcode == 2:
			op = lambda x,y: x * y
		else:
			print("Invalid opcode")
			return

		in1 = next(iterable)
		in2 = next(iterable)
		out = next(iterable)

		intcode[out] = op(intcode[in1], intcode[in2])

OUTPUT = 19690720
def find_inputs(intcode, output):
	for noun in range(100):
		for verb in range(100):
			copy = list(intcode)
			copy[1] = noun
			copy[2] = verb
			run_code(copy)
			if copy[0] == output:
				return 100 * noun + verb
	print("No answer found")


def main():
	print(find_inputs(INTCODE, OUTPUT))
	# run_code(INTCODE) # part 1
	# print(INTCODE[0])

if __name__ == '__main__':
	main()