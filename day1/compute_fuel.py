def compute_fuel1(): # part 1 of question
	with open("input.txt", "r") as file:
		masses = file.read().split('\n')
		masses.pop()
		fuel = 0
		for m in masses:
			fuel += int(m) // 3 - 2
		return fuel

def compute_fuel2(): # part 2
	with open("input.txt", "r") as file:
		masses = file.read().split('\n')
		masses.pop()
		total = 0
		for m in masses:
			m = int(m)
			while m:
				m = fuel(m)
				total += m
		return total

def fuel(mass): 
	return max(0, mass // 3 - 2)

def main():
	print(compute_fuel2())

if __name__ == '__main__':
	main()