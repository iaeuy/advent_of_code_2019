from queue import Queue

class IntcodeComputer():
	OP_LEN = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 1}

	def __init__(self, intcode, inputs = []):
		self.intcode = intcode
		self.ip = 0 # instruction pointer
		self.rbp = 0 # relative base pointer
		self.inputs = Queue()
		self.receive_inputs(inputs)
		self.outputs = Queue()
		self.halted = False

		self.run_code()

	def read(self, i):
		if i < 0:
			print("Cannot access negative index")
			return 
		return self.intcode[i] if i < len(self.intcode) else 0

	def write(self, val, i):
		if i >= len(self.intcode):
			self.intcode += [0] * (i - len(self.intcode) + 1)
		self.intcode[i] = val

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

			if op == 99: # halt
				self.halted = True
				break
			elif op == 1: # add
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				address = self.get_param(param_modes[2], self.ip+3, address=True)
				self.write(in1 + in2, address)
			elif op == 2: # multiply
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				address = self.get_param(param_modes[2], self.ip+3, address=True)
				self.write(in1 * in2, address)
			elif op == 3: # write input
				if not self.inputs.empty():
					address = self.get_param(param_modes[0], self.ip+1, address=True)
					self.write(self.inputs.get_nowait(), address)
				else:
					break
			elif op == 4: # output value at given address
				address = self.get_param(param_modes[0], self.ip+1, address=True)
				self.outputs.put(self.read(address))
			elif op == 5: # jump-if-true
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				if in1:
					self.ip = in2
					self.ip -= self.OP_LEN[op] + 1
			elif op == 6: # jump-if-false
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				if not in1:
					self.ip = in2
					self.ip -= self.OP_LEN[op] + 1
			elif op == 7: # less-than
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				address = self.get_param(param_modes[2], self.ip+3, address=True)
				self.write(1 if in1 < in2 else 0, address)
			elif op == 8: # eqals
				in1 = self.get_param(param_modes[0], self.ip+1)
				in2 = self.get_param(param_modes[1], self.ip+2)
				address = self.get_param(param_modes[2], self.ip+3, address=True)
				self.write(1 if in1 == in2 else 0, address)
			elif op == 9: # adjust relative base
				in1 = self.get_param(param_modes[0], self.ip+1)
				self.rbp += in1
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

	def get_param(self, param_mode, i, address=False):
		# address is True if parameter is meant to be interpreted as address, rather than a value
		if not address:
			if param_mode == 0:
				return self.read(self.read(i))
			elif param_mode == 1:
				return self.read(i)
			elif param_mode == 2:
				return self.read(self.read(i) + self.rbp)
			else: 
				print("Invalid param mode")
				return
		else:
			if param_mode == 0:
				return self.read(i)
			elif param_mode == 1:
				print("Write-to parameters cannot be in mode 1")
				return 
			elif param_mode == 2:
				return self.read(i) + self.rbp
			else: 
				print("Invalid param mode")
				return