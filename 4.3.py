from collections import deque

def createLevelLinkedLists(root, lists, level):
	if root == None:
	# Base case
		return
	list = None

	if len(lists) == level:
	# Level not contained in list
		list_ = deque()
		list_.append(root)
		lists.append(list_)
	else:
		list_ = lists[level]
	list_.append(root)
	#level += 1
	createLevelLinkedLists(root.left, lists, level + 1)
	createLevelLinkedLists(root.right, lists, level + 1)
		

class Node:
	def __init__(self, value = None, left = None, right = None, parent = None):
		self.left = left
		self.right = right
		self.parent = parent
		self.value = value

	def __str__(self):
		return '(' + str(self.left) +':L ' + "V:" + str(self.value) + " R:" + str(self.right) +')'
	
	def insert(self, value):
		if value <= self.value:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)


n = Node(55)
n.insert(11)
n.insert(60)
n.insert(8)
n.insert(70)
n.insert(20)
n.insert(63)
n.insert(99)
n.insert(12)
n.insert(101)

print(n)
lists = []
createLevelLinkedLists(n, lists, 0)

print('\n')
print(len(lists))
for i in range(len(lists)):
	print('level: ', i)
	for n in lists[i]:
		print('nodes: ', n)
