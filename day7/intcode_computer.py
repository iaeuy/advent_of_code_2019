# OUTDATED; USE INTCODE_COMPUTER.PY IN PARENT FOLDER

from queue import Queue

class IntcodeComputer():
	OP_LEN = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 1}

	def __init__(self, intcode, inputs = []):
		self.intcode = intcode
		self.ip = 0 # instruction pointer
		self.inputs = Queue()
		self.receive_inputs(inputs)
		self.outputs = Queue()
		self.halted = False

		self.run_code()

	def receive_inputs(self, inputs):
		for inp in inputs:
			self.inputs.put(inp)

	def broadcast_outputs(self):
		out = []
		while not self.outputs.empty():
			out.append(self.outputs.get_nowait())
		return out

	def run_code(self):
		if self.halted:
			return 
		while self.ip < len(self.intcode):
			op, param_modes = self.parse_opcode(self.intcode[self.ip])

			if op == 99:
				self.halted = True
				break
			elif op == 1:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				self.intcode[self.intcode[self.ip+3]] = in1 + in2
			elif op == 2:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				self.intcode[self.intcode[self.ip+3]] = in1 * in2
			elif op == 3:
				if not self.inputs.empty():
					self.intcode[self.intcode[self.ip+1]] = self.inputs.get()
				else:
					break
			elif op == 4:
				self.outputs.put(self.intcode[self.intcode[self.ip+1]])
			elif op == 5:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				if in1:
					self.ip = in2
					self.ip -= self.OP_LEN[op] + 1
			elif op == 6:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				if not in1:
					self.ip = in2
					self.ip -= self.OP_LEN[op] + 1
			elif op == 7:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				self.intcode[self.intcode[self.ip+3]] = 1 if in1 < in2 else 0
			elif op == 8:
				in1 = self.get_input(param_modes[0], self.intcode, self.ip+1)
				in2 = self.get_input(param_modes[1], self.intcode, self.ip+2)
				self.intcode[self.intcode[self.ip+3]] = 1 if in1 == in2 else 0
			else:
				print("Invalid opcode")
				return

			self.ip += self.OP_LEN[op] + 1

	def parse_opcode(self, opcode):
		# return opcode and parameter modes
		opcode = str(opcode) 
		op = int(opcode[-2:])
		param_modes = opcode[:-2][::-1]
		param_modes = [int(c) for c in param_modes]
		while len(param_modes) < self.OP_LEN[op]:
			param_modes.append(0)
		return op, param_modes 

	def get_input(self, param_mode, intcode, i):
		if param_mode == 0:
			return self.intcode[self.intcode[i]]
		elif param_mode == 1:
			return self.intcode[i]
		else: 
			print("Invalid param mode")
			return