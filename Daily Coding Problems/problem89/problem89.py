def isBinTree(root):
	# If root has no children
	if not root.left and not root.right:
		return True

	# If root has only the right child
	elif not root.left:
		if root.right.data < root.data:
			return False
		else:
			return isBinTree(root.right)

	# If root has only the left child
	elif not root.right:
		if root.left.data > root.data:
			return False
		else:
			return isBinTree(root.left)

	# Root has two children
	else:

		if root.left.data > root.data or root.right.data < root.data:
			return False
		else:
			return isBinTree(root.right) and isBinTree(root.left)

def main():
	pass

if __name__ == '__main__':
	main()