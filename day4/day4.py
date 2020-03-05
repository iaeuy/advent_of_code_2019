ALLOWED = (387638, 919123)

def num_valid(allowed):
	count = 0
	for i in range(allowed[0], allowed[1]):
		if valid2(i):
			count += 1
	return count

def valid(num):
	as_str = str(num)
	if len(as_str) != 6:
		return False
	has_repeat = False
	for i in range(1, len(as_str)):
		if as_str[i] < as_str[i-1]:
			return False
		if as_str[i] == as_str[i-1]:
			has_repeat = True
	return has_repeat

def valid2(num):
	as_str = str(num)
	if len(as_str) != 6:
		return False
	has_repeat = False
	for i in range(1, len(as_str)):
		if as_str[i] < as_str[i-1]:
			return False
		if as_str[i] == as_str[i-1] and (i + 1 == len(as_str) or as_str[i+1] != as_str[i]) and (i == 1 or as_str[i-2] != as_str[i]):
			has_repeat = True
	return has_repeat


def main():
	print(num_valid(ALLOWED))

if __name__ == '__main__':
	main()