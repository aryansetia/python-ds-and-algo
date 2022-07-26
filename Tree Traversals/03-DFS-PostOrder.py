class Node:
	def __init__(self, value):
		self.value = value 
		self.left = None 
		self.right = None 


class BinarySearchTree:
  	def __init__(self):
  		self.root = None 


  	def insert(self, value):
  		new_node = Node(value)
  		if self.root is None:
  			self.root = new_node
  			return True 
  		temp = self.root 
  		while(True):
  			if new_node.value == temp.value:
  				return False 
  			if new_node.value < temp.value:
  				if temp.left is None:
  					temp.left = new_node
  					return True 
  				temp = temp.left 
  			else:
  				if temp.right is None:
  					temp.right = new_node
  					return True 
  				temp = temp.right


  	def contains(self, value):
  		if self.root is None: # if tree is empty we will return false
  			return False
  		temp = self.root 
  		while(temp is not None):
  			if value < temp.value:
  				temp = temp.left 
  			elif value > temp.value:
  				temp = temp.right 
  			else:
  				return True

  		return False


  	def min_value_node(self, current_node):
  		while current_node.left is not None:
  			current_node = current_node.left 
  		return current_node
  	 		

  	# dfs postorder traversal 
  	def PostOrder(self):
  		results = []

  		def traverse(current_node):
  			if current_node.left is not None:
  				traverse(current_node.left)
  			if current_node.right is not None:
  				traverse(current_node.right)
  			results.append(current_node.value)

  		traverse(self.root)
  		return results
  	

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.PostOrder())