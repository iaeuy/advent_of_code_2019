INTCODE = [3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]
OP_LEN = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 1}


def run_code(intcode):
	iterable = iter(intcode)
	outputs = []
	i = 0 # instruction pointer

	while i < len(intcode):
		op, param_modes = parse_opcode(intcode[i])

		if op == 99:
			break
		elif op == 1:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			intcode[intcode[i+3]] = in1 + in2
		elif op == 2:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			intcode[intcode[i+3]] = in1 * in2
		elif op == 3:
			intcode[intcode[i+1]] = 5 # hardcoded input of 5 for part 2 now
		elif op == 4:
			outputs.append(intcode[intcode[i+1]])
		elif op == 5:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			if in1:
				i = in2
				i -= OP_LEN[op] + 1
		elif op == 6:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			if not in1:
				i = in2
				i -= OP_LEN[op] + 1
		elif op == 7:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			intcode[intcode[i+3]] = 1 if in1 < in2 else 0
		elif op == 8:
			in1 = get_input(param_modes[0], intcode, i+1)
			in2 = get_input(param_modes[1], intcode, i+2)
			intcode[intcode[i+3]] = 1 if in1 == in2 else 0
		else:
			print("Invalid opcode")
			return

		i += OP_LEN[op] + 1

	return outputs

def parse_opcode(opcode):
	# return opcode and parameter modes
	opcode = str(opcode) 
	op = int(opcode[-2:])
	param_modes = opcode[:-2][::-1]
	param_modes = [int(c) for c in param_modes]
	while len(param_modes) < OP_LEN[op]:
		param_modes.append(0)
	return op, param_modes 

def get_input(param_mode, intcode, i):
	if param_mode == 0:
		return intcode[intcode[i]]
	elif param_mode == 1:
		return intcode[i]
	else: 
		print("Invalid param mode")
		return

def main():
	print(run_code(INTCODE))
	# run_code(INTCODE) # part 1
	# print(INTCODE[0])

if __name__ == '__main__':
	main()