from math import gcd
from functools import reduce

class Moon():
	def __init__(self, position, velocity = [0, 0, 0]):
		# TODO
		self.position = position
		self.velocity = velocity

	def potential_energy(self):
		return sum([abs(coord) for coord in self.position])

	def kinetic_energy(self):
		return sum([abs(coord) for coord in self.velocity])

	def energy(self):
		return self.potential_energy() * self.kinetic_energy()

	def apply_gravity(self, other):
		"""
		Change velocity of other based on effect of gravity from self
		"""
		def sign(num):
			if num > 0:
				return 1
			elif num < 0:
				return -1
			else:
				return 0

		other.velocity = [other.velocity[i] + sign(self.position[i] - other.position[i]) for i in range(3)]


	def apply_velocity(self):
		self.position = [sum(z) for z in zip(self.position, self.velocity)]


class System():
	def __init__(self, moons):
		self.moons = moons
		self.periodicity_starts = [None] * 3
		self.prev_states = [{} for i in range(3)]
		self.periods = [0] * 3
		self.time = 0

	def energy(self):
		return sum([moon.energy() for moon in self.moons])

	def update(self):
		for moon1 in self.moons:
			for moon2 in self.moons:
				moon1.apply_gravity(moon2)

		for moon in self.moons:
			moon.apply_velocity()

		self.time += 1

	def get_state(self, coord):
		return tuple((moon.position[coord], moon.velocity[coord]) for moon in self.moons)

	def found_periods(self):
		starts = self.periodicity_starts
		return starts[0] != None and starts[1] != None and starts[2] != None

	def find_periodicity(self):
		while not self.found_periods():
			for coord in range(3):
				if self.periodicity_starts[coord] != None:
					continue

				curr_state = self.get_state(coord)
				if curr_state in self.prev_states[coord]:
					start = self.prev_states[coord][curr_state]
					period = self.time - start
					self.periodicity_starts[coord] = start
					self.periods[coord] = period
				else:
					self.prev_states[coord][curr_state] = self.time
			self.update()

		periodicity_start = max(self.periodicity_starts)
		period = reduce(lambda x, y: x*y // gcd(x, y), self.periods)
		return periodicity_start + period

def init_jupiter():
	Io = Moon([10, 15, 7])
	Europa = Moon([15, 10, 0])
	Ganymede = Moon([20, 12, 3])
	Callisto = Moon([0, -3, 13])
	return System([Io, Europa, Ganymede, Callisto])

def init_example1():
	Io = Moon([-1, 0, 2])
	Europa = Moon([2, -10, -7])
	Ganymede = Moon([4, -8, 8])
	Callisto = Moon([3, 5, -1])
	return System([Io, Europa, Ganymede, Callisto])

def main():
	JupiterOrbit = init_jupiter()

	# # part 1
	# for i in range(1000):
	# 	JupiterOrbit.update()
	# print(JupiterOrbit.energy())

	# part 2
	print(JupiterOrbit.find_periodicity())

if __name__ == '__main__':
	main()