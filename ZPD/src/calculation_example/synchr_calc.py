import time
import math

def make_calculation(line):
	line = line.split(' ')
	line = [int(x) for x in line]
	func = math.pow(line[3],2)*math.log(line[1]) * math.log10(line[0]) * math.sqrt(line[2])
	func = func * math.pi
	return func

file = open("data.txt", 'r')

start = time.time()

for line in file:
	make_calculation(line)

end = time.time()

print("Time:", end-start)


file.close()