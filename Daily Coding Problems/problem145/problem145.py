def swap_every_two(lst):
	if lst.next == None:
		return lst

	next_node = lst.next
	temp = next_node.next
	next_node.next = lst

	if temp:
		temp = swap_every_two(temp)

	lst.next = temp
	return lst

def main():
	pass

if __name__ == '__main__':
	main()