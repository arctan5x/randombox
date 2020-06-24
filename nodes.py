from collections import deque

class Node:
	def __init__(self, val, l=None, r=None):
		self.val = val
		self.l = l
		self.r = r

	def print_by_level(self):
		queue = deque()
		queue.append((self, 0))
		curr_level = 0
		curr_nodes = []
		while queue:
			node, level = queue.popleft()

			if curr_level != level:
				if any(curr_nodes):
					print(curr_nodes)
				curr_nodes = []
				curr_level = level

			if node:
				curr_nodes.append(node.val)
			else:
				curr_nodes.append(None)

			if node:
				queue.append((node.l, level+1))
				queue.append((node.r, level+1))

		if any(curr_nodes):
			print(curr_nodes)

	def print_paths_target(self, target):
		path_to_target = []

		def dfs_path(root, target, path, depth=0):
			if root:
				path = path + [root]
				nonlocal path_to_target

				if root.val == target:
					path_to_target = path
				
				l = dfs_path(root.l, target, path, depth+1)
				r = dfs_path(root.r, target, path, depth+1)
				root.sum = depth + l[0] + r[0]
				root.num_of_nodes = 1 + l[1] + r[1]
				return root.sum, root.num_of_nodes
			return 0, 0

		dfs_path(self, target, [])
		total_nums = self.sum
		overal = self.num_of_nodes

		for path in path_to_target[1:]:
			total_nums = total_nums - path.num_of_nodes + (overal - path.num_of_nodes)
		
		print(total_nums)





			
root = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3, Node(6), Node(7)))
root.print_by_level()
root.print_paths_target(9)



