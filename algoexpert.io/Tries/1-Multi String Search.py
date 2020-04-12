class TrieNode:
	#map<char, TrieNode>
	def __init__(self):
		self.children = {}
		self.endOfWord = True

def multiStringSearch(bigString, smallStrings):
	rootNode = TrieNode()
	bigString = bigString.split()
	#Trie insertion
	for bs in bigString:
		node_pointer = rootNode
		for s in bs:
			if s not in node_pointer.children:
				node_pointer.children[s] = TrieNode()
				node_pointer.endOfWord = False
			node_pointer = node_pointer.children[s]
	
	result = []
	result_index = 0
	#Trie searching
	for ss in smallStrings:
		node_pointer = rootNode
		result.append(True)
		for s in ss:
			if s in node_pointer.children:
				node_pointer = node_pointer.children[s]
			else:
				result[result_index] = False
				break
		result_index = result_index + 1
	return result


print(multiStringSearch('Mary goes to the shopping center every week', 
['to', 'Mary', 'centers', 'shop', 'shopping', 'string', 'kappa']))