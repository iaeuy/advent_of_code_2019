from itertools import permutations
from intcode_computer import IntcodeComputer

AMPCODE = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]
# AMPCODE = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
OP_LEN = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 1}

def best_setting_thrust():
	max_thrust = float("-inf")
	# perms = permutations([0, 1, 2, 3, 4])
	perms = permutations([5, 6, 7, 8, 9]) # part 2
	for p in perms:
		# max_thrust = max(max_thrust, chained_amplifiers(p))
		max_thrust = max(max_thrust, feedback_loop_amplifiers(p))
	return max_thrust

def feedback_loop_amplifiers(phase_settings):
	curr_output = 0
	amplifiers = []
	for i in range(5): # initial loop
		amp = IntcodeComputer(list(AMPCODE), [phase_settings[i], curr_output])
		amplifiers.append(amp)
		curr_output = amp.broadcast_outputs()[0]
	amp_e = amplifiers[4]
	last_amp_e_output = curr_output 
	i = 0
	while not amp_e.halted:
		amplifiers[i].receive_inputs([curr_output])
		amplifiers[i].run_code()
		curr_output = amplifiers[i].broadcast_outputs()[0]
		if i == 4:
			last_amp_e_output = curr_output
		i = (i + 1) % 5 
	return last_amp_e_output


def chained_amplifiers(phase_settings):
	curr_output = 0
	for i in range(5):
		amp = IntcodeComputer(list(AMPCODE), [phase_settings[i], curr_output])
		curr_output = amp.broadcast_outputs()[0]
	return curr_output

# def chained_amplifiers(phase_settings):
# 	curr_output = 0
# 	for i in range(5):
# 		amp = list(AMPCODE)
# 		curr_output = run_code(amp, [phase_settings[i], curr_output])[0]
# 	return curr_output

# def run_code(intcode, inputs):
# 	outputs = []
# 	i = 0 # instruction pointer
# 	j = 0 # input pointer

# 	while i < len(intcode):
# 		op, param_modes = parse_opcode(intcode[i])

# 		if op == 99:
# 			break
# 		elif op == 1:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			intcode[intcode[i+3]] = in1 + in2
# 		elif op == 2:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			intcode[intcode[i+3]] = in1 * in2
# 		elif op == 3:
# 			intcode[intcode[i+1]] = inputs[j]
# 			j += 1
# 		elif op == 4:
# 			outputs.append(intcode[intcode[i+1]])
# 		elif op == 5:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			if in1:
# 				i = in2
# 				i -= OP_LEN[op] + 1
# 		elif op == 6:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			if not in1:
# 				i = in2
# 				i -= OP_LEN[op] + 1
# 		elif op == 7:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			intcode[intcode[i+3]] = 1 if in1 < in2 else 0
# 		elif op == 8:
# 			in1 = get_input(param_modes[0], intcode, i+1)
# 			in2 = get_input(param_modes[1], intcode, i+2)
# 			intcode[intcode[i+3]] = 1 if in1 == in2 else 0
# 		else:
# 			print("Invalid opcode")
# 			return

# 		i += OP_LEN[op] + 1

# 	return outputs

# def parse_opcode(opcode):
# 	# return opcode and parameter modes
# 	opcode = str(opcode) 
# 	op = int(opcode[-2:])
# 	param_modes = opcode[:-2][::-1]
# 	param_modes = [int(c) for c in param_modes]
# 	while len(param_modes) < OP_LEN[op]:
# 		param_modes.append(0)
# 	return op, param_modes 

# def get_input(param_mode, intcode, i):
# 	if param_mode == 0:
# 		return intcode[intcode[i]]
# 	elif param_mode == 1:
# 		return intcode[i]
# 	else: 
# 		print("Invalid param mode")
# 		return

def main():
	print(best_setting_thrust())

if __name__ == '__main__':
	main()