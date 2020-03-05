from collections import Counter

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
LAYER_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

def get_image():
	with open("input.txt", "r") as file:
		image = list(file.read())
	image.pop()
	image = [int(digit) for digit in image]
	return image

def least_zeros(): # part 1 of question
	with open("input.txt", "r") as file:
		image = list(file.read())
	image.pop()
	image = [int(digit) for digit in image]

	least_zeros = float("inf")
	num1_times_num2 = None
	i = 0
	while i < len(image):
		layer_counts = Counter()
		while True:
			layer_counts[image[i]] += 1
			i += 1
			if i % LAYER_SIZE == 0:
				break

		if layer_counts[0] < least_zeros:
			least_zeros = layer_counts[0]
			num1_times_num2 = layer_counts[1] * layer_counts[2]

	return num1_times_num2

def decode():
	with open("input.txt", "r") as file:
		image = list(file.read())
	image.pop()
	image = [int(digit) for digit in image]

	num_layers = len(image) // LAYER_SIZE
	decoded = [[2]*IMAGE_WIDTH for i in range(IMAGE_HEIGHT)]

	for pixel in range(LAYER_SIZE):
		curr_width = pixel % IMAGE_WIDTH
		curr_height = pixel // IMAGE_WIDTH
		for layer in range(num_layers):
			if decoded[curr_height][curr_width] == 2:
				decoded[curr_height][curr_width] = image[layer*LAYER_SIZE + pixel]

	return decoded



def main():
	print(least_zeros())

if __name__ == '__main__':
	main()