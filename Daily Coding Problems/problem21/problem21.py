from sys import argv

def min_classrooms(intervals):
	queue = intervals
	queue.sort()

	classrooms = [[queue[0]]]

	for time_slot in queue[1:]:
		found = False

		for room in classrooms:
			if room[-1][1] <= time_slot[0]:
				found = True
				room.append(time_slot)

		if not found:
			classrooms.append([time_slot])

	return len(classrooms)


def main():
	if (len(argv) < 2):
		print('Not enough arguments')
		return

	intervals = []

	for arg in argv[1:]:
		arg = arg.split(',')

		x = int(arg[0])
		y = int(arg[1])

		intervals.append((x,y))

	rooms_needed = min_classrooms(intervals)

	print('{}'.format(rooms_needed))
	
if __name__ == '__main__':
	main()
